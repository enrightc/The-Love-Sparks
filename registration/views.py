from django.shortcuts import render, redirect
from .forms import LoveRegistrationForm

def register(request):
    if request.method == 'POST':
        form = LoveRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = LoveRegistrationForm()
    return render(request, 'register.html', {'form': form})

def success(request):
    return render(request, '')
