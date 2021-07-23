from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article, Comments
from django.urls import reverse

# Create your views here.

def index(request):

    articles = Article.objects.order_by('-created_date')[:5]

    
    
    return render(request,"index.html",{"articles":articles})

def about(request):
    return render(request,"about.html")


@login_required(login_url = "user:login")
def dashboard(request):

    articles= Article.objects.filter(author =request.user)

    return render(request,"dashboard.html",{"articles":articles})

@login_required(login_url = "user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    
    if form.is_valid():
        
      article = form.save(commit=False)
      article.author = request.user

      article.save()

      messages.success(request,"Məqalə uğurla əlavə edildi")
      return redirect("index")

    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    
    article = get_object_or_404(Article, id = id)
    comments =article.comments.all()
   
    return render(request,"detail.html",{'article':article,"comments":comments})

@login_required(login_url = "user:login")
def deleteArticle(request,id):

    article = get_object_or_404 (Article,id = id)

    article.delete()

    messages.success(request,"Məqaləniz uğurla silindi")

    return redirect("articles:dashboard")

@login_required(login_url = "user:login")
def updateArticle(request,id):
    
    article =get_object_or_404(Article, id = id)

    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)

    if form.is_valid():

        article = form.save(commit=False)

        article.author = request.user

        article.save()

        messages.success(request, "Məqalə uğurla əlavə edildi")
        return redirect("articles:dashboard")

    
    return render(request,"update.html",{"form":form})

def articles(request):

    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)

        return render(request, "articles.html",{"articles":articles})
    articles = Article.objects.all()


    return render(request, "articles.html",{"articles":articles})

def addComment(request,id):

    article=  get_object_or_404(Article, id = id)

    if request.method == "POST":

        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comments(comment_author = comment_author, comment_content =comment_content)

        newComment.article = article

        newComment.save()

    return redirect(reverse("articles:detail",kwargs = {"id":id}))
