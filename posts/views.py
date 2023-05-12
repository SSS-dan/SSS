from django.shortcuts import render, get_object_or_404, redirect
from users.models import User as Student
from .models import Post, Comment
from .forms import PostForm, CommentForm


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})


def post_list(request):
    # 모든 게시글을 가져와서 템플릿에 전달합니다.
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, post_id):
    # 특정 게시글을 가져옵니다.
    post = get_object_or_404(Post, id=post_id)
    # 게시글의 댓글들을 가져옵니다.
    comments = post.comments.all()

    if request.method == 'POST':
        # 댓글 폼을 제출한 경우
        form = CommentForm(request.POST)
        if form.is_valid():
            # 폼이 유효한 경우, 댓글을 생성합니다.
            comment = form.save(commit=False)
            comment.post = post
            comment.author = Student.objects.get(id=request.user.username)
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        # GET 요청인 경우
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})
