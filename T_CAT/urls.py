from django.urls import path
from T_CAT import views

urlpatterns = [
    path("v1/openAIAPI", views.OpenAIAPIBatchUpdateView.as_view()),
    
]