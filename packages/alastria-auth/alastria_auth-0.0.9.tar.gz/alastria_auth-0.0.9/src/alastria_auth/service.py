from django.conf import settings
from uuid import uuid4
from .models import ApiSession, RequestSession
from django.utils.timezone import now
import jwt
from PIL import Image, ImageDraw
from django.core.files import File
from io import BytesIO
import qrcode
from .abstractions import AAlastriaAuthService
from web3 import Web3
from eth_keys import keys
from eth_utils import decode_hex
from alastria_identity.services import TokenService
from django.http.response import HttpResponseBadRequest
from rest_framework.response import Response
from alastria_service_client.client import AClient, Client
from typing import Any
from django.core.exceptions import PermissionDenied
from alastria_service_client.validators import (
    NetworkValidator,
    OnlyNetworkValidator,
    Address,
)
from alastria_identity.types import JwtToken, AlastriaToken
from network_service_client.client import (
    AClient as ANetworkClient,
    Client as NetworkClient,
    Network as NetworkDTO,
    NetworksNames,
)
from network_service_client.enums import ContractsNames


class AlastriaAuthService(AAlastriaAuthService):
    @staticmethod
    def public_key_to_address(public_key: str) -> str:
        return Web3.toChecksumAddress(
            keys.PublicKey(decode_hex(public_key[2:])).to_address()
        )

    @staticmethod
    def get_did(address: str) -> str:
        alastria_service_client: AClient = Client(
            service_host=settings.ALASTRIA_SERVICE_HOST
        )
        network_data: NetworkDTO = NetworkClient(
            service_host=settings.NETWORK_SERVICE_HOST
        ).get_network_by_name(NetworksNames.AlastriaDefaultName)
        network_body = NetworkValidator(
            provider=network_data.node["path"],
            identity_manager_contract_address=list(
                filter(
                    lambda contract: contract["name"]
                    == ContractsNames.AlastriaIdentityManager.value,
                    network_data.contracts,
                )
            )[0]["address"],
            identity_manager_contract_abi=list(
                filter(
                    lambda contract: contract["name"]
                    == ContractsNames.AlastriaIdentityManager.value,
                    network_data.contracts,
                )
            )[0]["abi"],
            public_key_registry_contract_address="",
            public_key_registry_contract_abi="",
            credential_registry_contract_abi="",
            credential_registry_contract_address="",
            chainId=network_data.chain_id,
        )
        return alastria_service_client.identity_keys(
            address=Address(address), body=OnlyNetworkValidator(network=network_body)
        ).response

    @staticmethod
    def validate_permission(token: str) -> None:
        token_service = TokenService(settings.ISSUER_PRIVATE_KEY)
        decoded = token_service.decode_jwt(token)
        session_id: str = decoded.get("payload").get("session_id")

        aps: ApiSession = ApiSession.objects.filter(pk=session_id).first()

        if not aps:
            return PermissionDenied

        if aps.expiration_date < now():
            raise PermissionDenied

        if not token_service.verify_jwt(token, settings.ISSUER_PUBLIC_KEY):
            raise PermissionDenied

    @staticmethod
    def get_request_session_serializer(subject_did: str) -> RequestSession:
        rs: RequestSession = RequestSession(
            request_date=now(),
            requested_by=subject_did,
            confirm_url="/alastria/alastria-auth/confirm",
        )
        rs.save()
        network_data: NetworkDTO = NetworkClient(
            service_host=settings.NETWORK_SERVICE_HOST
        ).get_network_by_name(NetworksNames.AlastriaDefaultName)
        at: dict = AlastriaToken(
            network_data.did_prefix
            + AlastriaAuthService.get_did(settings.ISSUER_ADDRESS)[2:],
            network_data.node["path"],
            "/alastria/alastria-auth/confirm",
            settings.ALASTRIA_T_NETWORK_ID,
            1,
        ).build_jwt()
        at["payload"].update(
            {
                "signature_url": "/alastria/alastria-auth/signature",
                "request_session_id": rs.pk,
            }
        )
        token_service = TokenService(settings.ISSUER_PRIVATE_KEY)
        signed = token_service.sign_jwt(JwtToken(**at))
        qr_image = qrcode.make(signed)
        qr_offset = Image.new("RGB", (910, 910), "white")
        ImageDraw.Draw(qr_offset)
        qr_offset.paste(qr_image)
        file_name = f"{rs.requested_by}-{uuid4()}qr.png"
        stream = BytesIO()
        qr_offset.save(stream, "PNG")
        rs.qr_code.save(file_name, File(stream), save=False)
        qr_offset.close()
        rs.save()
        return rs

    @staticmethod
    def validate_did(did, response):
        if did and did[:4] != "0x00":
            return response
        else:
            return HttpResponseBadRequest("Not an alastria subject.")

    @staticmethod
    def validate_request_session(rs: RequestSession, format_did: str, response):
        if (
            rs
            and rs.requested_by == format_did
            and rs.expiration_date > now()
            and not rs.completed
        ):
            token_service = TokenService(settings.ISSUER_PRIVATE_KEY)

            rs.completed = True
            rs.save()
            aps: ApiSession = ApiSession(request_session_id=rs.pk)
            aps.save()
            header = {"alg": "ES256K", "typ": "JWT"}
            payload = {
                "expire_date": str(aps.expiration_date),
                "session_id": aps.pk,
                "request_session_id": aps.request_session_id,
            }
            signed = token_service.sign_jwt(JwtToken(header=header, payload=payload))
            aps.token = signed
            aps.save()
            return response
        else:
            return HttpResponseBadRequest("The request session is not valid.")

    @staticmethod
    def validate_signature(token: str) -> Any:
        token_service = TokenService(settings.ISSUER_PRIVATE_KEY)
        decoded = token_service.decode_jwt(token)
        alastria_token_decoded = token_service.decode_jwt(
            decoded["payload"].get("alastriaToken")
        )
        if not token_service.verify_jwt(
            decoded["payload"].get("alastriaToken"), settings.ISSUER_PUBLIC_KEY
        ):
            return HttpResponseBadRequest("Invalid Alastria Token.")
        public_key: str = decoded.get("payload").get("pku")
        request_session_id: int = alastria_token_decoded.get("payload").get(
            "request_session_id"
        )
        if token_service.verify_jwt(token, public_key):
            address: str = AlastriaAuthService.public_key_to_address(public_key)
            did: str = AlastriaAuthService.get_did(address)
            rs: RequestSession = RequestSession.objects.filter(
                pk=request_session_id
            ).first()
            network_data: NetworkDTO = NetworkClient(
                service_host=settings.NETWORK_SERVICE_HOST
            ).get_network_by_name(NetworksNames.AlastriaDefaultName)
            format_did: str = network_data.did_prefix + did[2:]

            return AlastriaAuthService.validate_request_session(
                rs,
                format_did,
                AlastriaAuthService.validate_did(did, Response({"response": "OK"})),
            )

        else:
            return HttpResponseBadRequest("Invalid Token.")
