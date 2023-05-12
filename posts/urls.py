from django.urls import path
from . import views

urlpatterns = [
    path('nickname/', views.nickname, name='nickname'),

    # 게시글 목록 페이지
    path('', views.post_list, name='post_list'),

    path('create/', views.create_post, name='create_post'),

    # 게시글 상세 페이지
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
