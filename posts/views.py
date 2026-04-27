
from django.http import JsonResponse
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post , Like , Comment
from django.views.decorators.http import require_POST

@login_required
def feed(request):
    posts = Post.objects.select_related('author').prefetch_related('comment_set', 'like_set').all().order_by('-id')
    comments = Comment.objects.all()

    return render(request, 'feed.html', {
        'posts': posts,
        'comments': comments
    })

@login_required
def create_post(request):
    if request.method == "POST":
        content = request.POST.get('content')
        image = request.FILES.get('image')
        Post.objects.create(author=request.user, content=content, image=image)
        return redirect('feed')
    return render(request, 'create.html')

@require_POST
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )

    if not created:
        like.delete()

    return JsonResponse({
        'total_likes': post.like_set.count()
    })

def add_comment(request, post_id):
    if request.method == "POST":

        if not request.user.is_authenticated:
            return JsonResponse({'error': 'not logged in'}, status=403)

        post = get_object_or_404(Post, id=post_id)
        body = request.POST.get('body')

        if not body or body.strip() == "":
            return JsonResponse({'error': 'empty comment'}, status=400)

        comment = Comment.objects.create(
            user=request.user,
            post=post,
            body=body
        )

        return JsonResponse({
            'user': request.user.username,
            'body': comment.body
        })

    return JsonResponse({'error': 'invalid request'}, status=400)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-id')

    if request.method == "POST":
        if request.user.is_authenticated:
            body = request.POST.get('body')

            Comment.objects.create(
                user=request.user,
                post=post,
                body=body
            )

            return redirect('post_detail', post_id=post_id)

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments
    })