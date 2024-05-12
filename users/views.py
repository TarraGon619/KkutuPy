from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from users.forms import UserCreationForm

# Create your views here.
def user_logout(req):
    logout(req)
    return redirect('lobby')

def signup(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(req, user)
            # return render(req, 'main/index.html')
            return redirect('lobby')
    else:
        form = UserCreationForm()
    return render(req, 'users/signup.html', {'form':form})