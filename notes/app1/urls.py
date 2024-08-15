from django.urls import path
from app1 import views

urlpatterns=[
    path('cls',views.fun1,name="Notes"),
    path('search',views.fun2,name="Notes")
]