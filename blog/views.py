from django.shortcuts import render
from blog.data import posts

def blog(request):
    print('blog')

    context={
        # 'text': 'Olá blog',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )

def post(request, id):
    print('post', id)

    context={
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )

def exemplo(request):
    print('exemplo')

    context={
        'text': 'Ola exemplo',
        'title': 'Página'
    }

    return render(
        request,
        'blog/exemplo.html',
        context
    )