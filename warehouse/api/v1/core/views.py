from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from warehouse.api.v1.core.serializers import (
    InputSerializer,
    OutputSerializer,
)
from warehouse.api.v1.core.service import Service


class ResultViewSet(viewsets.ViewSet):
    @swagger_auto_schema(request_body=InputSerializer, responses={200: OutputSerializer(many=True)})
    @action(methods=['post'], detail=True)
    def process(self, request, *args, **kwargs):
        serializer = InputSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        data = Service.process(data)
        return Response(status=status.HTTP_200_OK, data=data)
