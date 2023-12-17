from django.db import models
import uuid


class OoenAIAPI(models.Model):
    "openAIへのリクエスト"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    input_message = models.CharField(max_length=500, blank=True)
    add_message = models.CharField(max_length=200, blank=True)
    output_message = models.CharField(max_length=500, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "openai_api"
        verbose_name = verbose_name_plural = "openAIへのリクエスト"
        ordering = ["create_at"]

    def __str__(self):
        return str(self.id)