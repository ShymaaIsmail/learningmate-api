# The code snippet you provided is a URL configuration for a Django project named
# `learningmateapi`. In Django, the `urlpatterns` list is used to route URLs to views within the
# project.
"""
URL configuration for learningmateapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Create schema view instance
schema_view = get_schema_view(
    openapi.Info(
        title="Learningmate Platform API",
        default_version='v1',
        extra="Shymaa M. Ismail",
        description="Learningmate Platform API description",
        terms_of_service="https://www.shymaaismai.tech",
        contact=openapi.Contact(email="shymaa.m.ismail@gmail.com"),
        license=openapi.License(name="Shymaa Mohamed Ismail -ALX SWE Program- Cohort 19"),
    ),
    public=True,
    url='http://localhost:8000/learningmate-api/',  # This sets the base URL for the API

)


urlpatterns = [
    # Admin APIs
    path('auth/', include('learningmateapi.api_urls.auth_urls')),
    path('learning_categories/', include('learningmateapi.api_urls.learning_categories_urls')),
    # Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
