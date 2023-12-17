from django.apps import apps
from django.conf import settings
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import APIException

from T_CAT import models


class OpenAIAPISaveMixin:
    "DB保存する機能を備えたMixin"

    def create(self, data):
        try:
            with transaction.atomic():
                models.OoenAIAPI.objects.create(data)
        except Exception:
            raise APIException("Internal Server Error.")


class OpenAIAPIBatchUpdateSerializer(
    serializers.ModelSerializer, OpenAIAPISaveMixin
):
    "OpenAIのAPIへのリクエスト内容を保存するためのシリアライザ"

    id = serializers.UUIDField(read_only=True)
    input_message = serializers.CharField(
        max_length=200, allow_blank=True    # write_only=True, 
    )
    add_message = serializers.CharField(
        max_length=200, allow_blank=True    # write_only=True, 
    )
    output_message = serializers.CharField(
        read_only=True, max_length=500, allow_null=True
    )
    class Meta:
        model = models.OoenAIAPI
        fields = (
            "id",
            "input_message",
            "add_message",
            "output_message",
            "create_at",
        )

    def to_internal_value(self, data):
        "デシリアライズ（DB保存前（の際に呼ばれる)"
        data = super().to_internal_value(data)
        
        # この時にchatgptを呼び、output_messageにレスポンスを格納する。

        data["output_message"] = ""

        return super().to_internal_value(data)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return super().to_representation(instance)