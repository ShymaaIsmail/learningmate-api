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
    url='http://localhost:8000/api/v1/',  # This sets the base URL for the API
)

urlpatterns = [
    # User APIs
    path('api/v1/auth/', include('learningmateapi.api_urls.auth_urls')),
    #Learning Categories APIs
    path('api/v1/learning_categories/', include('learningmateapi.api_urls.learning_categories_urls')),
    #Courses APIs
    path('api/v1/courses/', include('learningmateapi.api_urls.courses_urls')),
    # Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
