"""
URL configuration for cs415 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from cs415.views import WebUserAPIView, AddressTypeAPIView, UserAddressAPIView, PhoneTypeAPIView, UserPhoneAPIView, UserInfoAPIView, PageDataAPIView
from cs415.views import (
    SingleWebUserAPIView,
    SingleAddressTypeAPIView,
    SingleUserAddressAPIView,
    SinglePhoneTypeAPIView,
    SingleUserPhoneAPIView,
    SingleUserInfoAPIView,
    SinglePageDataAPIView,
)

## for swagger documentation
schema_view = get_schema_view(
   openapi.Info(
      title="cs415 REST API Endpoints",
      default_version='1.0',
      description="API Documentation for cs415 Website API Project",
   ),
   public=True,
)

urlpatterns = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('users/', WebUserAPIView.as_view()),
    path('address-types/', AddressTypeAPIView.as_view()),
    path('addresses/', UserAddressAPIView.as_view()),
    path('phone-types/', PhoneTypeAPIView.as_view()),
    path('phones/', UserPhoneAPIView.as_view()),
    path('user-infos/', UserInfoAPIView.as_view()),
    path('pages/', PageDataAPIView.as_view()),
    path('users/user/<int:web_user_id>', SingleWebUserAPIView.as_view()),
    path('address/type/<int:address_type_id>', SingleAddressTypeAPIView.as_view()),
    path('users/address/<int:user_address_id>', SingleUserAddressAPIView.as_view()),
    path('phone/type/<int:phone_type_id>', SinglePhoneTypeAPIView.as_view()),
    path('users/phone/<int:user_phone_id>', SingleUserPhoneAPIView.as_view()),
    path('users/info/<int:user_info_id>', SingleUserInfoAPIView.as_view()),
    path('page/data/<int:page_data_id>', SinglePageDataAPIView.as_view()),
    path('api/webuser/', WebUserAPIView.as_view(), name='webuser'),
]

