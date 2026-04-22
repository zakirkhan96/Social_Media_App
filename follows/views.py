
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Follow

def follow(request, username):
    user = User.objects.get(username=username)
    Follow.objects.get_or_create(follower=request.user, following=user)
    return redirect('feed')
