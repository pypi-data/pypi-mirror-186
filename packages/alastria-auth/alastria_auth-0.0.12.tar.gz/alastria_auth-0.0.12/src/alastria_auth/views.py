from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import (
    RequestSessionSerializer,
    SignatureSerializer,
    ConfirmResponseSerializer,
    SuccessResponseSerializer,
    ConfirmSerializer,
)
from rest_framework.decorators import action
from .models import RequestSession
from rest_framework.response import Response
from .service import AlastriaAuthService
from .models import ApiSession
from .decorators import requires_alastria_auth
from waffle.decorators import waffle_switch
from .enums import AlastriaAuthSwitches


class AlastriaAuthView(ViewSet):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        method="get",
        manual_parameters=[
            openapi.Parameter(
                "subject_did",
                openapi.IN_QUERY,
                description="Subject Alastria DID",
                type=openapi.TYPE_STRING,
            )
        ],
        responses={200: openapi.Response("", RequestSessionSerializer)},
    )
    @waffle_switch(AlastriaAuthSwitches.auth.value)
    @action(detail=False, methods=["get"])
    def auth(self, request):
        subject_did: str = request.GET["subject_did"]
        rs: RequestSession = AlastriaAuthService.get_request_session_serializer(
            subject_did
        )
        rss: RequestSessionSerializer = RequestSessionSerializer(rs)
        return Response(rss.data)

    @swagger_auto_schema(
        operation_description="""
        Token field is a jwt signed by the subjet and signature alg should be ES256K.
        Example:
        {
            "header": {
                "alg": "ES256K",
                "typ": "JWT",
                "jwk": "0x03fdd57adec3d438ea237fe46b33ee1e016eda6b585c3e27ea66686c2ea5358479"
            },
            "payload": {
                "@context": ["https://alastria.github.io/identity/artifacts/v"],
                "iss": "did:ala:quor:redT:dc4eeee191cf4b1adeee4e91b25dec6dd8ec79c4",
                "pku": "",
                "iat": 1585128712,
                "nbf": 1585139712,
                "alastriaToken": "",
                "jti": "ze298y42sba"
            }
        }
        """,
        method="post",
        request_body=SignatureSerializer,
        responses={200: openapi.Response("", SuccessResponseSerializer)},
    )
    @waffle_switch(AlastriaAuthSwitches.auth.value)
    @action(detail=False, methods=["post"])
    def signature(self, request):
        token: str = request.data["token"]
        return AlastriaAuthService.validate_signature(token)

    @swagger_auto_schema(
        method="post",
        request_body=ConfirmSerializer,
        responses={200: openapi.Response("", ConfirmResponseSerializer)},
    )
    @waffle_switch(AlastriaAuthSwitches.auth.value)
    @action(detail=False, methods=["post"])
    def confirm(self, request):
        request_session_id: str = request.data["request_session_id"]
        api_session: ApiSession = ApiSession.objects.get(
            request_session_id=request_session_id
        )
        return Response({"response": api_session.token})

    @swagger_auto_schema(
        method="post", responses={200: openapi.Response("", SuccessResponseSerializer)}
    )
    @requires_alastria_auth
    @waffle_switch(AlastriaAuthSwitches.auth.value)
    @action(detail=False, methods=["post"])
    def log_out(self, request):
        return Response({"response": "OK"})
