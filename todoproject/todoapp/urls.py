from django.urls import path
from . import views

urlpatterns = [
    path('',views.todo,name='todo'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/',views.tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.taskdetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.taskupdate.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.taskdelete.as_view(),name='cbvdelete'),

]
