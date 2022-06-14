from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from .models import User, Post, Like, Follow
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from django.db.models.base import ObjectDoesNotExist

def index(request):
    # get posts from newest to oldest
    posts = list(Post.objects.order_by("-timestamp"))
    pages = range(1, int(len(posts)/10)+2)
    liked = []
    for post in posts:
        try:
            Like.objects.get(post=post, liker=User.objects.get(id=request.user.id))
            liked.append(True)
        except ObjectDoesNotExist:
            liked.append(False)
    return render(request, "network/index.html", context= {
        "posts": zip(posts, liked),
        "pages": pages
    })

@login_required
@csrf_exempt
def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if (post.poster == User.objects.get(id=request.user.id)):
        if request.method == "PUT":
            data = json.loads(request.body)
            if data.get("content") is not None:
                post.content = data["content"]
            post.save()
            return HttpResponse(status=204)
    else:
        return HttpResponseRedirect(reverse("index"))


@login_required
def follow(request, user_id):
    followee = User.objects.get(id=user_id)
    follower = User.objects.get(id=request.user.id)
    try:
        follow = Follow.objects.get(follower=follower, followee=followee)
        follow.delete()
    except ObjectDoesNotExist:
        follow = Follow(follower=follower, followee=followee)
        follow.save()
    return HttpResponse(status=204)

@login_required
def following(request):
    followed_by_user = [follow.followee for follow in list(Follow.objects.filter(follower = User.objects.get(id=request.user.id)))]
    posts = Post.objects.filter(poster__in=followed_by_user).order_by("-timestamp")
    pages = range(1, int(len(posts)/10)+2)
    liked = []
    for post in posts:
        try:
            Like.objects.get(post=post, liker=User.objects.get(id=request.user.id))
            liked.append(True)
        except ObjectDoesNotExist:
            liked.append(False)
    return render(request, "network/following.html", context= {
        "posts": zip(posts, liked),
        "pages": pages
    })

@csrf_exempt
@login_required
def get_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "GET":
        return JsonResponse(post.post_serialize(), safe=False)

def like(request, post_id):
    post = Post.objects.get(id=post_id)
    try:
        # if post was liked before, unlike it
        like = Like.objects.get(liker = User.objects.get(id=request.user.id), post=post)
        like.delete()
    except ObjectDoesNotExist:
        # if post wasn't liked, like it
        like = Like(liker = User.objects.get(id=request.user.id), post=post)
        like.save()
        # get number of likes on post
    num_likes = Like.objects.filter(post=post).count()
    # update like count on Post object in database
    post.numLikes = num_likes
    post.save(update_fields=['numLikes'])
    # indicates that request was successful, but no need to change pages
    return HttpResponse(status=204)

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def new_post(request):
    content = request.POST["content"]
    poster = User.objects.get(id=request.user.id)
    # save new post to database
    p = Post.objects.create(poster = poster, content = content)
    return HttpResponseRedirect(reverse("index")) 

def profile(request, user_id):
    user_data = User.objects.get(id=user_id)
    me = User.objects.get(id=request.user.id)
    posts = list(Post.objects.filter(poster=User.objects.get(id=user_id)).order_by("-timestamp"))
    my_likes = [like.post for like in me.user_likes.all()]
    my_follows = [follow.followee for follow in me.following.all()]
    if user_data in my_follows:
        followed_by_me = True
    else:
        followed_by_me = False
    liked = []
    liked_for_liked_posts = []
    for post in posts:
        if post in my_likes:
            liked.append(True)
        else:
            liked.append(False)
    posts_zipped = list(zip(posts, liked))
    user_likes = list(user_data.user_likes.all())
    
    for user_like in user_likes:
        if user_like.post in my_likes:
            liked_for_liked_posts.append(True)
        else:
            liked_for_liked_posts.append(False)

    return render(request, "network/profile.html", context = {
        "user": user_data,
        "posts": posts_zipped,
        "followers": list(user_data.followed_by.all()),
        "following": list(user_data.following.all()),
        "user_likes": list(zip(user_likes, liked_for_liked_posts)),
        "num_followers": len(list(user_data.followed_by.all())),
        "num_following": len(list(user_data.following.all())),
        "followed_by_me": followed_by_me
    })

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
