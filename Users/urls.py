from django.urls import path

from Users.views import Users

urlpatterns = [
    path('register', Users.create_user)
]
