from django.urls import path
from .views import lecture_list, lecture_detail, lecture_new, lecture_edit, lecture_delete

urlpatterns = [
    path('', lecture_list, name='lecture_list'),
    path('<int:lecture_id>/', lecture_detail, name='lecture_detail'),
    path('new/', lecture_new, name='lecture_new'),
    path('<int:lecture_id>/edit/', lecture_edit, name='lecture_edit'),
    path('<int:lecture_id>/delete/', lecture_delete, name='lecture_delete'),
]