from django.db import models

# Create your models here.


class UsersModel(models.Model):

    user_rid = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=100, null=False)
    user_mobile = models.CharField(max_length=10, null=True)
    user_created_datetime = models.DateTimeField(null=False)
    user_modified_datetime = models.DateTimeField(null=True)
    user_active = models.SmallIntegerField(default=1)  # Active is 1

    class Meta:
        db_table = 'users'

