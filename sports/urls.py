from django.urls import path
from .views import sports,News
app_name='sports'
urlpatterns=[
    path('',sports,name="home"),
    path('<str:data>/',News,name='news'),
]