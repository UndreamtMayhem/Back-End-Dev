# DJANGO web dependencies
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404

# DJANGO authentication dependencies
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Local dependencies
from .models import BlogArticle


def check_user_auth(user):
    if user.is_authenticated:
        return True
    else:
        return False

def index(request):
    
    blogs = BlogArticle.objects.order_by('-created')

    if request.method == 'POST':
        
        usname = request.POST['username']
        
        pwd = request.POST['password']

        user = authenticate(username=usname, password=pwd)

        if user is not None:
            
            login(request, user)

        else:
            
            messages.add_message(request, messages.WARNING, 'Incorrect username or password')

            redirect(index)
            
    else:
        
       return render(request, "index.html", {
           'blogs':blogs, 
           'user_login':check_user_auth(request.user)
        })
        
        
def single_blog(request, blog_id):
    
    blog = get_object_or_404(BlogArticle, pk=blog_id)

    return render(request, "single-post.html", {
        'blog':blog, 
        'user_login':check_user_auth(request.user)
    })

@login_required(redirect_field_name='', login_url='/blog/')
def create_blog(request):
    if request.method == 'POST':
        
        newBlog = BlogArticle()

        newBlog.title = request.POST['title']

        newBlog.blog_content = request.POST['blog_content']

        newBlog.author = request.user

        newBlog.save()

        return render(request, "single-post.html",{
            'blog':newBlog, 
            'user_login':check_user_auth(request.user)
        })
    else:
        return render(request, 'add-post.html', {
            'user_login':check_user_auth(request.user)
    })

@login_required(redirect_field_name='', login_url='/blog/')
def logout_view(request):
    
    logout(request)

    blogs = BlogArticle.objects.order_by('created')

    return render(request, "index.html", {
        'blogs':blogs, 
        'user_login':check_user_auth(request.user)
    })