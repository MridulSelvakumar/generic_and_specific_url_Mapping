from django.urls import path
from shiva.views import *
app_name="shiva_G"
urlpatterns=[
    path('shiva/',shiva,name='shiva'),
]