from django.urls import path
from .views import movies,News
app_name='movies'
urlpatterns=[
    path('',movies,name="home"),
    path('<str:data>/',News,name='news'),
]