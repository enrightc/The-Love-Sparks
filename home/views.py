from django.shortcuts import render


def index(request):
    """
    A view to return the index page
    """
    context = {'message': 'Hello World'}
    return render (request, 'home/index.html', context)


