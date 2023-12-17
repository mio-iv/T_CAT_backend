from drf_spectacular.utils import extend_schema
from rest_framework import status, views
from rest_framework.response import Response

from T_CAT.serializers import OpenAIAPIBatchUpdateSerializer

@extend_schema(
    tags=["OpenAIAPI"],
    request=OpenAIAPIBatchUpdateSerializer,
    responses=OpenAIAPIBatchUpdateSerializer,
    )

class OpenAIAPIBatchUpdateView(views.APIView):
    "openAIへのリクエストを受け付ける"

    def post(self, request, *args, **kwargs):
        serializer = OpenAIAPIBatchUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)