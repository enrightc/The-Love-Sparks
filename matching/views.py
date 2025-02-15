from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def find_a_match(request):
    """
    A view to return the find a match page
    """
    return render (request, 'find_a_match/find_a_match.html')
