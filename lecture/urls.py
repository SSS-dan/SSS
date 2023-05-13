from django.urls import path
from .views import *

urlpatterns = [
    path('', lecture_list, name='lecture_list'),
    path('select/<str:lecture_id>/', lecture_detail, name='lecture_detail'),
    path('new/', lecture_new, name='lecture_new'),
    path('select/', lecture_select, name ='lecutre_select'),
    path('<int:lecture_id>/edit/', lecture_edit, name='lecture_edit'),
    path('<int:lecture_id>/delete/', lecture_delete, name='lecture_delete'),
]