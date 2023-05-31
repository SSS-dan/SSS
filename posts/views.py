from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from .models import Post, Comment
from users.models import User
from .forms import PostForm, CommentForm, NicknameForm


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 현재 인증된 사용자를 작성자로 설정
            post.save()
            return redirect('post_list', mod=post.mod)
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})


def post_list(request, mod):
    # 모든 게시글을 가져와서 템플릿에 전달합니다.
    if request.user.nickname == '':
        return nickname(request)

    if mod == 0:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(mod=mod)

    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, post_id):
    # 특정 게시글을 가져옵니다.
    post = get_object_or_404(Post, id=post_id)
    # 게시글의 댓글들을 가져옵니다.
    comments = post.comments.all()

    if not post.view.filter(student_id=request.user.student_id).exists():
        post.view.add(request.user)
        post.view_num += 1
        post.save()

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

            return redirect('post_list')
    else:
        form = NicknameForm()

    return render(request, 'nickname.html', {'form': form})


def delete_post(request, item_id):
    item = get_object_or_404(Post, pk=item_id)  # 삭제할 데이터베이스 객체를 가져옵니다.
    item.delete_post()
    return redirect('post_list')  # 삭제 성공 후 리다이렉션할 URL을 지정합니다.


def delete_comment(request, item_id):
    item = get_object_or_404(Comment, pk=item_id)  # 삭제할 데이터베이스 객체를 가져옵니다.
    post_id = item.post.id
    item.delete_comment()
    return redirect('post_detail', post_id)  # 삭제 성공 후 리다이렉션할 URL을 지정합니다.


def upvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user_profile = request.user

    already_upvoted = post.upvote.filter(student_id=user_profile.student_id).exists()
    if not already_upvoted:
        post.upvote.add(user_profile)
        post.upvote_num += 1
        post.save()

    return redirect('post_detail', post_id=post.id)
