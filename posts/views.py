
from django.http import JsonResponse
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post , Like , Comment

@login_required
def feed(request):
    posts = Post.objects.all().order_by('-id')
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

def like_post(request, post_id):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'not logged in'}, status=403)
    
    post = get_object_or_404(Post, id=post_id)

    like , created = Like.objects.get_or_create(
        user = request.user,
        post = post
    )

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({
        'liked': liked, 
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
