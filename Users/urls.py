from django.urls import path

from Users.views import Users

urlpatterns = [
    path('create', Users.create_user)
]
