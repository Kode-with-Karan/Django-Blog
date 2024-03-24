from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post, Category, PostImage


# Create your views here.
def home(request):
    posts = Post.objects.all()[:11]

    cats = Category.objects.all()


    data = {
        'posts': posts,
        'cats': cats,
    }
    return render(request, 'home.html', data)

def about(request):
    cats = Category.objects.all()
    return render(request, 'about.html',{'cats': cats})

def datenschutz(request):
    cats = Category.objects.all()
    return render(request, 'datenschutz.html',{'cats': cats})

def fanstand(request):
    cats = Category.objects.all()
    return render(request, 'fanstand.html',{'cats': cats})

def gasteblock(request):
    cats = Category.objects.all()
    return render(request, 'gasteblock.html',{'cats': cats})

def kontakt(request):
    cats = Category.objects.all()
    return render(request, 'kontakt.html',{'cats': cats})

def links(request):
    cats = Category.objects.all()
    return render(request, 'links.html',{'cats': cats})

def supcrew(request):
    cats = Category.objects.all()
    return render(request, 'supcrew.html',{'cats': cats})

def vereinshistorie(request):
    cats = Category.objects.all()
    return render(request, 'vereinshistorie.html',{'cats': cats})


def search(request):
    query = request.GET['query']
    posts = Post.objects.filter(title__icontains=query)
    cats = Category.objects.all()
    return render(request, 'search.html', {'posts': posts, 'cats': cats, 'query':query})


def post(request, url):
    posts = Post.objects.get(url=url)
    related_post = Post.objects.filter(title__icontains=posts.title.split(" ")[0])[0:3]
    cats = Category.objects.all()
    images = PostImage.objects.filter(post=posts)
    related_cat = Category.objects.filter(title__icontains=posts.cat)[0]
    return render(request, 'posts.html', {'post': posts, 'cats': cats, 'related_cat':related_cat, 'images': images, 'related_post':related_post})


def category(request, url):
    cats = Category.objects.all()
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'cats': cats, 'posts': posts})
