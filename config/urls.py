from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("T_CAT/", include("T_CAT.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # 127.0.0.1/8000/api/schema にアクセスでテキストファイルをダウンロード
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # 127.0.0.1/8000/api/docs アクセスでSwaggerUIを表示

]
