from django.shortcuts import render

posts = [
    {
        'author': 'CMS',
        'title': 'blog post 1',
        'date_posted': 'august 27, 2018',
    },
    {
        'author': 'RFT',
        'title': 'blog post 2',
        'date_posted': 'august 28, 2018',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

