from django.urls import path
from .views import *

urlpatterns = [
    path('', phone_list, name='phone_list'),              
    path('add/', phones_add, name='phone_add'),            
    path('update/<int:pk>/', phone_update, name='phone_update'),  
    path('delete/<int:pk>/', phone_delete, name='phone_delete'),  
]
