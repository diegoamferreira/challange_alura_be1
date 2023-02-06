from django.urls import path

from users.views import UserCreateAPIView

urlpatterns = [
    path('create-user/', UserCreateAPIView.as_view(), name='create-user'),
]
