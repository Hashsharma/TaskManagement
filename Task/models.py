from django.db import models

from Users.models import UsersModel
from Users.views import Users


# Create your models here.


class TaskModel(models.Model):
    task_rid = models.IntegerField(primary_key=True)
    task_title = models.CharField(max_length=255, null=False)
    task_description = models.TextField(null=True)
    task_created_datetime = models.DateTimeField(null=False)
    task_mod_datetime = models.DateTimeField(null=True)
    task_status = models.IntegerField(default=0)  # 0 Pending, 1 Completed, 2 Deleted
    task_user_rid = models.ForeignKey(UsersModel, on_delete=models.DO_NOTHING, null=False)

    class Meta:
        db_table = 'tasks'




