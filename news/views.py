from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import logout 
from .models import New, Category, Region


def home(request):
    first_news = New.objects.first()
    three_news = New.objects.all()[1:4]
    return render(request, 'home.html', {
        'first_news': first_news,
        'three_news': three_news
    })


def all_news(request):
    all_news = New.objects.all()
    return render(request, 'all-news.html', {
        'all_news': all_news
    })


def detail(request, id):
    news = New.objects.get(id=id)
    category = Category.objects.get(id=news.category.id)
    rel_news = New.objects.filter(category=category).exclude(id=id)
    context = {
        'news': news,
        'category': category,
        'rel_news': rel_news
    }
    return render(request, 'detail.html', context)


def all_category(request):
    cats = Category.objects.all()
    return render(request, 'category.html', {
        'cats': cats
    })


def category(request, id):
    category = Category.objects.get(id=id)
    news = New.objects.filter(category=category)
    return render(request, 'category-news.html', {
        'all_news': news,
        'category': category
    })


def all_region(request):
    regs = Region.objects.all()
    return render(request, 'region.html', {
        'regs': regs
    })


def region(request, id):
    region = Region.objects.get(id=id)
    news = New.objects.filter(region=region)
    return render(request, 'region-news.html', {
        'all_regs': news,
        'region': region
    })

    
def user_logout(request):
    logout(request)
    return render (request, 'registration/logged_out.html')

from django.urls import reverse_lazy

class Create_post(CreateView):
    model = New
    fields = ['category', 'region', 'title', 'text', 'image', 'author']
    template_name = 'create-post.html'

    def get_success_url(self):
        return reverse_lazy('create-post')

class Edit_post(UpdateView):
    model = New
    template_name = 'edit-post.html'
    fields = ['category', 'region', 'title', 'text']

class Delete_post(DeleteView):
    model = New
    template_name= 'delete-post.html'
    success_url = reverse_lazy('home')
