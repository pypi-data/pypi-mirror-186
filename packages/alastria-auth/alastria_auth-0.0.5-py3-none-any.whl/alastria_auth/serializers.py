from rest_framework import serializers
from .models import RequestSession, ApiSession


class RequestSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestSession
        fields = (
            "request_date",
            "expiration_date",
            "requested_by",
            "qr_code",
            "confirm_url",
        )


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiSession
        fields = (
            "token",
            "expiration_date",
            "is_active",
        )


class SignatureSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=1500)


class ConfirmSerializer(serializers.Serializer):
    request_session_id = serializers.IntegerField()


class ConfirmResponseSerializer(serializers.Serializer):
    api_session_token = serializers.CharField(max_length=255)


class SuccessResponseSerializer(serializers.Serializer):
    response = serializers.CharField(max_length=2)
