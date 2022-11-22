import datetime

import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from Task.TaskSerializer import TasksSerializer
from Task.models import TaskModel
from Users.UsersSerializer import UserSerializer
from Users.models import UsersModel


# Create your views here.


class Tasks:

    @api_view(['POST'])
    def create_task(request):
        try:
            req = json.loads(request.body)
            task_model = TaskModel()
            task_model.task_title = req.get('taskTitle')
            task_model.task_description = req.get('taskDescription')
            task_model.task_created_datetime = datetime.datetime.now()
            task_model.task_user_rid = UsersModel.objects.get(user_rid=req.get('userRID'))

            task_model.save()
            return Response('Task Created Successfully', status=status.HTTP_200_OK)

        except Exception as e:
            print('Failed to create ' + str(e))
            return Response('Task Created Failed', status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def get_all_tasks(requests):
        try:
            user_rid = int(requests.GET['id'])
            query_set = TaskModel.objects.filter(task_user_rid_id=user_rid).order_by('task_rid').reverse()
            task_serializer = TasksSerializer(query_set, many=True)
            return Response(task_serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print('Error while fetching task lists', str(e))
            return Response('Error while fetching task lists', status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def get_completed_tasks(requests):
        try:
            user_rid = int(requests.GET['id'])
            query_set = TaskModel.objects.filter(task_user_rid_id=user_rid,
                                                 task_status=1).order_by('task_rid').reverse()  # 1 Completed
            task_serializer = TasksSerializer(query_set, many=True)
            return Response(task_serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print('Error while fetching task lists', str(e))
            return Response('Error while fetching task lists', status=status.HTTP_400_BAD_REQUEST)

    @api_view(['POST'])
    def mark_task_completed(requests):
        try:
            req = json.loads(requests.body)
            query_set = Tasks.get_task_by_id(req)
            if query_set is not None:
                query_set.task_status = 1
                query_set.task_mod_datetime = datetime.datetime.now()
                query_set.save()
                return Response('Task completed successfully', status=status.HTTP_200_OK)
            else:
                return Response('Failed to complete', status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('Failed to complete' + str(e))
            return Response('Failed to complete', status=status.HTTP_400_BAD_REQUEST)

    def get_task_by_id(req):
        try:
            task_rid = req.get('taskRID')
            user_rid = req.get('userRID')
            query_set = TaskModel.objects.filter(task_rid=task_rid,
                                                 task_user_rid_id=user_rid).first()
            return query_set  # Can not have two entries in table with same mobile number and product id

        except Exception as e:
            print('Failed to find task' + str(e))
            return None

    @api_view(['POST'])
    def delete_task(request):
        try:
            req = json.loads(request.body)
            query_set = Tasks.get_task_by_id(req)

            if query_set is not None:
                query_set.task_status = 2
                query_set.save()

                return Response('Task deleted successfully', status=status.HTTP_200_OK)
            else:
                return Response('Failed to delete', status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print('Failed to delete' + str(e))
            return Response('Failed to delete', status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def get_deleted_tasks(requests):
        try:
            user_rid = int(requests.GET['id'])
            query_set = TaskModel.objects.filter(task_user_rid_id=user_rid,
                                                 task_status=2).order_by('task_rid').reverse()  # 1 Completed
            task_serializer = TasksSerializer(query_set, many=True)
            return Response(task_serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print('Error while fetching task lists', str(e))
            return Response('Error while fetching task lists', status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def get_pending_tasks(requests):
        try:
            user_rid = int(requests.GET['id'])
            query_set = TaskModel.objects.filter(task_user_rid_id=user_rid,
                                                 task_status=0).order_by('task_rid').reverse()  # 1 Completed
            task_serializer = TasksSerializer(query_set, many=True)
            return Response(task_serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print('Error while fetching task lists', str(e))
            return Response('Error while fetching task lists', status=status.HTTP_400_BAD_REQUEST)
