from django.urls import path
from .views import RegisterUserView
#from ..myapi.urls import urlpatterns

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register-user'),
]