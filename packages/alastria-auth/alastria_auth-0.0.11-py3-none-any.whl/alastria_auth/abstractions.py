from django.conf import settings
from .models import RequestSession
from abc import ABC, abstractmethod
from typing import Any


class AAlastriaAuthService(ABC):
    @staticmethod
    @abstractmethod
    def validate_permission(token: str) -> None:
        ...

    @staticmethod
    @abstractmethod
    def get_did(address: str) -> str:
        ...

    @staticmethod
    @abstractmethod
    def validate_signature(token: str) -> Any:
        ...

    @staticmethod
    @abstractmethod
    def public_key_to_address(public_key: str) -> str:
        ...

    @staticmethod
    @abstractmethod
    def get_request_session_serializer(subject_did: str) -> RequestSession:
        ...

    @staticmethod
    @abstractmethod
    def validate_did(did, response):
        ...

    @staticmethod
    @abstractmethod
    def validate_request_session(rs: RequestSession, format_did: str, response):
        ...
