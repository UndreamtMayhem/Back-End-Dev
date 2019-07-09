from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Topic, Post
from django.contrib.auth import authenticate, login, logout

def check_user_auth(user):
    if user.is_authenticated:
        return True
    else:
        return False

def logout_view(request):
    logout(request)
    return redirect('main')

def index(request):
    topics = Topic.objects.all()
    
    ctx = {'topics': topics, 'user_login':check_user_auth(request.user)}

    return render(request, 'topic-list.html', ctx)

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('main')
    else:
        return redirect('main')

def new_topic(request):
    if request.method == 'POST':
        topic_name = request.POST['topic_name']
        newTopic = Topic()
        newTopic.title = topic_name
        newTopic.save()
        return redirect('main')
    else:
        return redirect('main')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        newUser = User()
        newUser.username = username
        newUser.set_password(password)
        newUser.save()
        return render(request, 'signup-complete.html', {})
    return render(request, 'signup.html', { 'user_login':check_user_auth(request.user)})

def topic_detail(request, topic_id=None):
    topic = Topic.objects.get(id=topic_id)
    ctx = {'topic':topic, 'user_login':check_user_auth(request.user), 'posts':topic.post_set.all(), 'user':request.user}
    return render(request, 'topic-detail.html', ctx)

def add_post(request):
    if request.method == 'POST':
        post_content = request.POST['post_content']
        post_topic = Topic.objects.get(id=request.POST['topic_id'])
        newPost = Post()
        newPost.author = request.user
        newPost.content = post_content
        newPost.topic = post_topic
        newPost.save()
        return redirect('topic-detail', topic_id=post_topic.id)
    else:
        return redirect('main')
    
def delete_post(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        cPost = Post.objects.get(id=post_id)
        topic_id = cPost.topic.id
        cPost.delete()
        return redirect('topic-detail', topic_id=topic_id)
    else:
        return redirect('main')