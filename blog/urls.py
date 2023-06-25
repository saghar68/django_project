from django.urls import path
from .views import Post_list,Post_Detail,Post_Create,Post_Update,Post_Delete


urlpatterns = [
    path('',Post_list,name='home'),
    path('<int:pk>/',Post_Detail.as_view(),name='detail'), 
    path('add/',Post_Create.as_view(),name='add'),
    path('<int:pk>/edit/',Post_Update.as_view(),name='edit'),
    path('<int:pk>/delete',Post_Delete.as_view(),name="delete"),
    
    
]




