from django.contrib import admin
from django.urls import path, include
# from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Kabu Kabu Backend API",
      default_version='v1',
      description="Backend API for a transport booking web app ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ezekieleyitayo2020@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('auth/', include('authentication.urls')),
    path('business/', include('business.urls')),

]
