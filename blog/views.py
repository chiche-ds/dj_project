from django.shortcuts import render

# Create your views here.

posts =[
    {
    'author':'CoreyMs',
    'title':'blog psot 1',
    'content': 'first post content',
    'date_posted':'april 15, 2022'

    },
    {
    'author':'jane Doe',
    'title':'blog psot 2',
    'content': 'second post content',
    'date_posted':'april 12, 2022'

    }

]

def home(request):
    content = {
        'posts':posts
    }
    return render(request, 'blog/home.html',content)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})

def contact(request):
    return HttpResponse('<h1> Blog contact </h1>')
