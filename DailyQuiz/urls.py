"""DailyQuiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

#SWAGGER
openapi_info = openapi.Info(
    title='DailyQuiz',
    default_version='v1',
    description='simple quiz api for study by JamesKim'
)

schema_view = get_schema_view(
    openapi_info,
    public=True,
    url=os.getenv('SWAGGER_ROOT_URL'),
    permission_classes=(permissions.AllowAny,),
)
#JWT


urlpatterns = [
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0),name='schema-json'),
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
    path('api/', include('common.app_urls', namespace='common_urls'))
]
