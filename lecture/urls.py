from django.urls import path
from .views import *

urlpatterns = [
    path('', lecture_list, name='lecture_list'),
    path('select/<str:lecture_id>', lecture_select, name='lecture_detail'),
    path('new/', lecture_new, name='lecture_new'),
    path('edit/<str:lecture_id>', lecture_edit, name='lecture_edit'),
    path('delete/<str:lecture_id>', lecture_delete, name='lecture_delete'),
]