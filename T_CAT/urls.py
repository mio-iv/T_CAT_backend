from django.urls import include, path
from T_CAT import views

app_name = "T_CAT"

urlpatterns = [
    path("", views.main, name="main"),
]