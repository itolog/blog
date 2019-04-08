from django.shortcuts import render
from .models import Article

# Create your views here.

# HOME
def home(request):
    return render(request, 'myapp/home.html')


# BLOG
def blog(request):
    data = {
        "title": 'Home',
        "news": Article.objects.all()
    }
    return render(request, 'myapp/blog.html', data)


# CONTACT
def contact(request):
    data = {
        "title": "contact"
    }
    return render(request, 'myapp/contact.html', data)
