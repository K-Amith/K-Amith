from django.urls import path
from resumeApp import views

urlpatterns =[
path('',views.index,name='index'),

]
