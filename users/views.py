from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from users.forms import RegisterForm, AuthForm


def register_view(request):
  if request.method == 'GET':
    context = {
      'form': RegisterForm
    }
    return render(request, 'users/register.html', context=context)
  elif request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      User.objects.create_user(**form.cleaned_data)
      return redirect('/users/login/')
    else:
      return  render(request, 'users/register.html', context={'form': form})

def login_view(request):
  if request.method == 'GET':
    context = {
      'form': AuthForm
    }
    return render(request, 'users/auth.html', context=context)
  elif request.method == 'POST':
    form = AuthForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']

      user = authenticate(username=username, password=password)

      if user is not None:
        login(request, user)
        return redirect('/products/')
      else:
        form.add_error('username',
                       'user name is incorrect')


    return render(request, 'users/auth.html', context={'form': form})

def logout_view(request):
  logout(request)
  return redirect('/')

def profile_view(request):
  if request.method == 'GET':
    return render(
      request,
      'users/profile.html',
      context={"user": request.user}
    )
