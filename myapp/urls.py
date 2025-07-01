from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='insert'),
    path('delete/<str:pk>/',views.delete,name='delete'),
    path('update/<str:pk>/',views.update,name='update'),
    path('toggle/<str:pk>/',views.toggle_complete,name='toggle_complete')
]
