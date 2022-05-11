from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


schema_view = get_schema_view(title="Project API")


urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include_docs_urls(title="Project API Documentation")),
        path('schema', schema_view),
        path('accounts/', include('registration.backends.simple.urls')),

        path("app/", include("core.urls", namespace="core")),
        path("users/", include("users.urls", namespace="users")),
        path("services/", include("services.urls", namespace="services")),

        path("api/v1/users/", include("api.v1.users.urls", namespace="api_v1_users")),
        path("api/v1/services/", include("api.v1.services.urls", namespace="api_v1_services")),

        path("sitemap.xml", TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml")),
        path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

admin.site.site_header = "Project Administration"
admin.site.site_title = "Project Admin Portal"
admin.site.index_title = "Welcome to Project Admin Portal"
