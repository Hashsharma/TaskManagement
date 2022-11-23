import datetime
import json

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Users.UsersSerializer import UserSerializer
from Users.models import UsersModel


# Create your views here.


class Users:

    @api_view(['POST'])
    def create_user(request):
        try:
            req = json.loads(request.body)
            user_model = UsersModel()
            user_data = Users.get_user_by_mobile(req)
            if user_data is not None:
                user_serializer = UserSerializer(user_data, many=True)
                return Response(user_serializer.data, status=status.HTTP_200_OK)

            else:
                user_model.user_name = req.get('userName')
                user_model.user_mobile = req.get('userMobile')
                user_model.user_created_datetime = datetime.datetime.now()

                user_model.save()
                user_data = Users.get_user_by_mobile(req)
                user_serializer = UserSerializer(user_data, many=True)
                return Response(user_serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print('Failed to create user' + str(e))
            return Response('Failed to Create User', status=status.HTTP_400_BAD_REQUEST)

    def get_user_by_mobile(req):
        try:
            query_set = UsersModel.objects.filter(user_mobile=req.get('userMobile'))
            return query_set
        except Exception as ex:
            print('Failed to fetch user' + str(ex))
            return None


