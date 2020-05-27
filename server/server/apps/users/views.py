from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from . import serializers

# Create your views here.
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication, jwt_decode_handler

from .models import User


class MobileCountView(APIView):
    """
    GET /api/mobiles/count/
    判断手机号是否存在， 查询手机号数量
    """

    def get(self, request, *args):
        params = request.query_params.dict()
        mobile = params.get('mobile', '')
        count = User.objects.filter(mobile=mobile).count()
        data = {
            'mobile': mobile,
            'count': count
        }
        return Response(data, status=status.HTTP_200_OK)


class CurrentUserView(APIView):
    """
    GET /api/currentUser
    """

    # serializer_class = serializers.CurrentUserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args):
        params = request.query_params.dict()

        user = self.request.user
        print(user.is_superuser)

        user_role = 'user'
        if user.is_superuser:
            user_role = 'admin'

        ret_data = dict(
            name=user.username,
            email=user.email,
            currentAuthority=user_role
        )

        return Response(ret_data, status=status.HTTP_200_OK)

