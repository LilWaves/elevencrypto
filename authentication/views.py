from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from authentication.forms import SignupForm
from django.urls import reverse

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('auth:login'))
        else:
            return render(request, 'authentication/signup.html', {'form': form})
    else:
        form = SignupForm()

        args = {'form': form}
        return render(request, 'authentication/signup.html', args)
