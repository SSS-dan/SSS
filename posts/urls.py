from django.urls import path
from . import views

urlpatterns = [
    path('nickname/', views.nickname, name='nickname'),

    # 게시글 목록 페이지
    path('<int:mod>/', views.post_list, name='post_list'),

    path('create/', views.create_post, name='create_post'),

    # 게시글 상세 페이지
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),

    # 게시글 삭제
    path('delete_post/<int:item_id>/', views.delete_post, name='delete_post'),

    # 댓글 삭제
    path('delete_comment/<int:item_id>/', views.delete_comment, name='delete_comment'),

    path('post/upvote/<int:post_id>/', views.upvote_post, name='upvote_post'),
]
