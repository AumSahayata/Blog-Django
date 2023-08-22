from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as authlogin
from django.contrib.auth import logout as authlogout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post,Comment

# Create your views here.
@login_required(login_url='login')
def index(request):
    posts = Post.objects.order_by('-id')
    return render(request,"blog/index.html",{
        "posts":posts
    })

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwrd = request.POST.get('password')
        user = authenticate(request,username=username,password=passwrd)

        if user is not None:
            authlogin(request,user)
            return redirect("index")
        else:
            return render(request,"blog/login.html",{
                "message":"Incorrect credentials!!"
            })

    return render(request,"blog/login.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        passwrd = request.POST.get('password')
        conpasswrd = request.POST.get('conpassword')

        if passwrd == conpasswrd:
            new_user = User.objects.create_user(username,email,passwrd)
            new_user.save()

            return redirect('/')
        else:
            return render(request,"blog/signup.html",{
                "message":"Password does not match!!"
            })

    return render(request,"blog/signup.html")

def logout(request):
    authlogout(request)
    return redirect('/')

@login_required(login_url='login')
def new_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        user = request.user

        post = Post(title=title,post_body=body,username=user)
        post.save()

        return redirect('/home')    

    return render(request,"blog/new_post.html")

def edit_post(request, post_id):
    post = Post.objects.get(id = post_id) #can use pk(primary key) on place of id
    if request.method == 'POST':
        post = Post.objects.get(id = post_id) 
        title = request.POST.get('title')
        body = request.POST.get('body')

        post.title = title
        post.post_body = body
        post.save()
        

        return redirect('/home')
    return render(request,"blog/edit_post.html",{
        "post":post,
    })

def view_post(reqest, post_id):
    post = Post.objects.get(id = post_id) #can use pk(primary key) on place of id

    if reqest.method == 'POST':
        comment_text = reqest.POST.get('comment')
        user = reqest.user
        c_post = Post.objects.get(id = post_id)

        comment = Comment(username = user,comment = comment_text,post = c_post)

        comment.save()

        return HttpResponseRedirect(reverse("view_post",args=(post.id,)))
    
    comments = Comment.objects.filter(post = post.id)
    
    return render(reqest,"blog/post.html",{
        "post":post,
        'comments':comments
    })

def my_posts(request):
    posts = Post.objects.filter(username = request.user)

    return render(request,"blog/my_posts.html",{
        "posts":posts
    })

def delete_post(request,post_id):
    post = Post.objects.get(id = post_id) #can use pk(primary key) on place of id
    post.delete()
    return redirect('/my_posts')