from django.urls import path
from . import views

urlpatterns=[
      path('index',views.index,name='index'),
      path('login',views.login),
      path('index2',views.index2),
      path('index3',views.index3),
      path('index4',views.index4),
      path('index5',views.index5),
      ]

