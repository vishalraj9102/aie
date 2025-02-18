from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.middleware.csrf import get_token


def get_csrf_token(request):
    return JsonResponse({'csrftoken': get_token(request)})

schema_view = get_schema_view(
    openapi.Info(
        title="Authentication API",
        default_version='v1',
        description="API for user authentication with cookie-based authentication",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),  # Add this line to serve the index.html at '/'
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/csrf/', get_csrf_token),
    
]
