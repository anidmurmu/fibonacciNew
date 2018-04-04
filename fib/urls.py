from django.urls import path
from . import views


app_name = 'fib'
urlpatterns = [
	# /fib/
    path('', views.home, name='index'),

]