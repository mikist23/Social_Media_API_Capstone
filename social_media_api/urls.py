from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Define schema view for API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Social Media API",
        default_version='v1',
        description="API documentation for the Social Media API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@socialmediaapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("accounts.urls")),
    path('api/', include('posts.urls')),
    path('api/', include('notifications.urls')),
    path('swagger/', schema_view.as_view(), name='schema-swagger-ui'),  # Swagger UI for API docs
]

