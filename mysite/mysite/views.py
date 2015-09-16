from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse  # , Http404


def login_form(request):
    return render(request, 'auth/login.html')


def login_authenticate(request):
    # Retrieve Parameters from the request.
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    # Authenticating the user
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        login(request, user)
        # Redirect to a success page.
        # If he tried to access some protected page, redirect to that page
        # after successfull login. Otherwise redirect to home page.
        if request.POST.get('next', ''):
            return HttpResponseRedirect(request.POST.get('next', ''))
        else:
            return HttpResponseRedirect('/polls/')
    else:
        # Show an error page
        return HttpResponse("Login failed")


def logout_view(request):
    logout(request)
    # Redirect to Home page after Logout.
    return HttpResponseRedirect("/polls/")


# 404 error view
def error404(request):
    return render(request, '404.html', status=404)


# 500 error view
def error500(request):
    return render(request, '500.html', status=404)
