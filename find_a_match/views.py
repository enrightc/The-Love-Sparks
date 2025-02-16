from django.shortcuts import render


def find_a_match(request):
    """
    A view to return the about page
    """
    return render (request, 'find_a_match/find_a_match.html')
