from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Category, Post


# Create your views here.

def home(request):
    # Load all the post from db at start 10 post 
    posts=Post.objects.all()[:5]
    print(posts)

    cats = Category.objects.all() 
    data = {
        "posts":posts,
        "cats":cats
    }
     
    return render(request,'home.html',data)

def post(request,url):
    post=Post.objects.get(url=url)
    cats = Category.objects.all() 
    print(post)
    readmore = {
        "readmore":post,
        "cats":cats
    }
    return render(request,'post.html',readmore)

def category(request,url):
    category = Category.objects.get(url=url) 
    posts = Post.objects.filter(cat=category)

    return render(request,"Category.html",{'cat':category,'posts':posts})



