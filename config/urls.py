from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("t_cat/", include("T_CAT.urls")),
]
