from django.urls import path
from .views import *


urlpatterns = [
    path('',Post_list,name='home'),
    path('<int:post_id>/',detail,name='detail'), 
    path('add',create,name='add'),
    path('<int:post_id>/edit/',Edit,name='edit'),
    path('<int:post_id>/delete',delete,name="delete")
    
    
]




