from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from warehouse.api.core.schemas import AutoSchema
from warehouse.api.core.serializers import (
    InputSerializer,
)
from warehouse.api.core.service import Service


class ResultViewSet(viewsets.ViewSet):
    schema = AutoSchema(tags=['Results'])

    @action(methods=['post'], detail=True, serializer_class=InputSerializer, filter_backends=[])
    def process(self, request, *args, **kwargs):
        serializer = InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        data = Service.process(data)
        return Response(status=status.HTTP_200_OK, data=data)
