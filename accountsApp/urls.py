from django.urls import path
from accountsApp import views


app_name = 'accountsApp'
urlpatterns = [
    path("", views.home, name="home"),
]