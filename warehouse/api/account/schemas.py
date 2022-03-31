from warehouse.api.account.serializers import (
    TokenObtainPairRequestSerializer,
    TokenObtainPairResponseSerializer,
    TokenRefreshRequestSerializer,
    TokenRefreshResponseSerializer
)
from warehouse.api.core.schemas import AutoSchema


class TokenObtainPairSchema(AutoSchema):
    def get_tags(self, path, method):
        return ['Me']

    def get_request_serializer(self, path, method):
        return TokenObtainPairRequestSerializer()

    def get_response_serializer(self, path, method):
        return TokenObtainPairResponseSerializer()


class TokenRefreshSchema(AutoSchema):
    def get_tags(self, path, method):
        return ['Me']

    def get_request_serializer(self, path, method):
        return TokenRefreshRequestSerializer()

    def get_response_serializer(self, path, method):
        return TokenRefreshResponseSerializer()
