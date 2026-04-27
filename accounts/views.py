from django.contrib.auth.models import User
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from posts.models import Post
from follows.models import Follow

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('feed')
    return render(request, 'register.html', {'form': form})

def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile

    posts = Post.objects.filter(author=user)
    followers = Follow.objects.filter(following=user).count()
    following = Follow.objects.filter(follower=user).count()

    # UPDATE PROFILE
    if request.method == "POST" and request.user == user:
        profile.bio = request.POST.get('bio')

        if request.FILES.get('image'):
            profile.image = request.FILES.get('image')

        profile.save()
        return redirect('profile', username=username)

    return render(request, 'profile.html', {
        'profile_user': user,
        'profile': profile,
        'posts': posts,
        'followers': followers,
        'following': following
    })