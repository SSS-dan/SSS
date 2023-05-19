from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from .models import Post, Comment
from .forms import PostForm, CommentForm, NicknameForm


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 현재 인증된 사용자를 작성자로 설정
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})


def post_list(request):
    # 모든 게시글을 가져와서 템플릿에 전달합니다.
    if request.user.nickname == '':
        return nickname(request)

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
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        # GET 요청인 경우
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})


def nickname(request):
    if request.method == 'POST':
        form = NicknameForm(request.POST)
        if form.is_valid():
            nick = request.POST['nickname']
            new_user = request.user
            new_user.nickname = nick
            new_user.save()
            # 닉네임을 활용한 추가 동작 수행
            # 예: 사용자 모델에 닉네임 저장

            return redirect('post_list')  # 닉네임 입력 후 create_post 페이지로 이동
    else:
        form = NicknameForm()

    return render(request, 'nickname.html', {'form': form})
