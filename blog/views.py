from django.shortcuts import render


posts = [
    {
        'author': 'moneeb',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'August 27, 2018',
    },
    {
        'author': 'haris ',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'August 30, 2018',
    }
]

context = {
    'posts': posts
}

def home(request):

    return render(request, 'blog/home.html', context)


def about(request):
     return render(request, 'blog/about.html')
