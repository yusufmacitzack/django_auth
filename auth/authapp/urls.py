from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginPageView.as_view(), name="loginpage" )
]
