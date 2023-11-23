from django.urls import path
from vishnu.views import *
app_name='vishnu_G'
urlpatterns=[
    path('vishnu/',vishnu,name='vishnu')
]