from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from cs415.models import (
    Webuser,
    Addresstype,
    Useraddress,
    Userinfo,
    Phonetype,
    Userphone,
    Pagedata,
)
from cs415.serializers import (
    WebUserSerializer,
    WebUserSerializerPost,
    AddressTypeSerializer,
    UserAddressSerializer,
    UserInfoSerializer,
    PhoneTypeSerializer,
    UserPhoneSerializer,
    PageDataSerializer,
)
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class Login(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({'success': False,
                             'error': 'Email and Password must have a value'},
                            status=status.HTTP_400_BAD_REQUEST)

        check_user = Webuser.objects.filter(email=email).exists()
        if check_user == False:
            return Response({'success': False,
                             'error': 'User with this email does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

        check_pass = Webuser.objects.filter(email=email, password=password).exists()
        if check_pass == False:
            return Response({'success': False,
                             'error': 'Incorrect password for user'},
                            status=status.HTTP_401_UNAUTHORIZED)

        user = Webuser.objects.get(email=email, password=password)

        # add last login to User table
        serializer = WebUserSerializer(user, data={'last_login': str(datetime.now())}, partial=True)
        if serializer.is_valid():
            serializer.save()

        if user is not None:
            jwt_token = "<jwt_token_here>"
            data = {
                'token': jwt_token
            }
            return Response({'success': True,
                             'user_id': user.web_user_id,
                             'token': jwt_token},
                            status=status.HTTP_200_OK)
        else:
            return Response({'success': False,
                             'error': 'Invalid Login Credentials'},
                            status=status.HTTP_400_BAD_REQUEST)


# View for WebUser
class WebUserAPIView(APIView):
    def get(self, request):
        users = Webuser.objects.all()
        serializer = WebUserSerializer(users, many=True)
        return Response(serializer.data)
    @swagger_auto_schema(operation_description= "Add New User", request_body=WebUserSerializerPost)
    def post(self, request, *args, **kwargs):
        request.data['created_date'] = str(datetime.now())
        request.data['is_active'] = 1
        serializer = WebUserSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)

# View for AddressType
class AddressTypeAPIView(APIView):
    @swagger_auto_schema(responses={200: WebUserSerializer(many=True)})
    def get(self, request):
        address_types = Addresstype.objects.all()
        serializer = AddressTypeSerializer(address_types, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AddressTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# View for UserAddress
class UserAddressAPIView(APIView):
    @swagger_auto_schema(responses={200: UserAddressSerializer(many=True)})
    def get(self, request):
        user_addresses = Useraddress.objects.all()
        serializer = UserAddressSerializer(user_addresses, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = UserAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# View for UserInfo
class UserInfoAPIView(APIView):
    @swagger_auto_schema(responses={200: UserInfoSerializer(many=True)})
    def get(self, request):
        user_infos = Userinfo.objects.all()
        serializer = UserInfoSerializer(user_infos, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# View for PhoneType
class PhoneTypeAPIView(APIView):
    @swagger_auto_schema(responses={200: PhoneTypeSerializer(many=True)})
    def get(self, request):
        phone_types = Phonetype.objects.all()
        serializer = PhoneTypeSerializer(phone_types, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = PhoneTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# View for UserPhone
class UserPhoneAPIView(APIView):
    @swagger_auto_schema(responses={200: UserPhoneSerializer(many=True)})
    def get(self, request):
        user_phones = Userphone.objects.all()
        serializer = UserPhoneSerializer(user_phones, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = UserPhoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# View for PageData
class PageDataAPIView(APIView):
    @swagger_auto_schema(responses={200: PageDataSerializer(many=True)})
    def get(self, request):
        page_data = Pagedata.objects.all()
        serializer = PageDataSerializer(page_data, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = PageDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# Single Web User API View
class SingleWebUserAPIView(APIView):
    def get(self, request, web_user_id):
        user_data = {}
        user = Webuser.objects.get(web_user_id=web_user_id)
        user_serial = WebUserSerializer(user)
        user_data.update({"user": user_serial.data})
        addresses = UserAddressSerializer(Useraddress.objects.filter(web_user=user), many=True)
        user_data.update({"addresses": addresses.data})
        info = UserInfoSerializer(Userinfo.objects.filter(web_user=user), many=True)
        user_data.update({"info": info.data})
        phone = UserPhoneSerializer(Userphone.objects.filter(web_user=user).select_related(), many=True)
        user_data.update({"phones": phone.data})
        return Response(user_data)
    
    @swagger_auto_schema(operation_description="Update WebUser", request_body=WebUserSerializer)
    def patch(self,request,web_user_id):
        webuser_obj = Webuser.objects.get(web_user_id=web_user_id)
        serializer = WebUserSerializer(webuser_obj, data=request.data,partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# AddressType API View
class SingleAddressTypeAPIView(APIView):
    def get(self, request, address_type_id):
        address_type = Addresstype.objects.get(address_type_id=address_type_id)
        serializer = AddressTypeSerializer(address_type)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update Address Type", request_body=AddressTypeSerializer)
    def patch(self, request, address_type_id):
        address_type = Addresstype.objects.get(address_type_id=address_type_id)
        serializer = AddressTypeSerializer(address_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# UserAddress API View
class SingleUserAddressAPIView(APIView):
    def get(self, request, user_address_id):
        user_address = Useraddress.objects.get(user_address_id=user_address_id)
        serializer = UserAddressSerializer(user_address)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update User Address", request_body=UserAddressSerializer)
    def patch(self, request, user_address_id):
        user_address = Useraddress.objects.get(user_address_id=user_address_id)
        serializer = UserAddressSerializer(user_address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# PhoneType API View
class SinglePhoneTypeAPIView(APIView):
    def get(self, request, phone_type_id):
        phone_type = Phonetype.objects.get(phone_type_id=phone_type_id)
        serializer = PhoneTypeSerializer(phone_type)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update Phone Type", request_body=PhoneTypeSerializer)
    def patch(self, request, phone_type_id):
        phone_type = Phonetype.objects.get(phone_type_id=phone_type_id)
        serializer = PhoneTypeSerializer(phone_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# UserPhone API View
class SingleUserPhoneAPIView(APIView):
    def get(self, request, user_phone_id):
        user_phone = Userphone.objects.get(user_phone_id=user_phone_id)
        serializer = UserPhoneSerializer(user_phone)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update User Phone", request_body=UserPhoneSerializer)
    def patch(self, request, user_phone_id):
        user_phone = Userphone.objects.get(user_phone_id=user_phone_id)
        serializer = UserPhoneSerializer(user_phone, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# UserInfo API View
class SingleUserInfoAPIView(APIView):
    def get(self, request, user_info_id):
        user_info = Userinfo.objects.get(user_info_id=user_info_id)
        serializer = UserInfoSerializer(user_info)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update User Info", request_body=UserInfoSerializer)
    def patch(self, request, user_info_id):
        user_info = Userinfo.objects.get(user_info_id=user_info_id)
        serializer = UserInfoSerializer(user_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# PageData API View
class SinglePageDataAPIView(APIView):
    def get(self, request, page_data_id):
        page_data = Pagedata.objects.get(page_data_id=page_data_id)
        serializer = PageDataSerializer(page_data)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Update Page Data", request_body=PageDataSerializer)
    def patch(self, request, page_data_id):
        page_data = Pagedata.objects.get(page_data_id=page_data_id)
        serializer = PageDataSerializer(page_data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

