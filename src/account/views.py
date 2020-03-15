from django.contrib.auth import (
    # authenticate,
    # get_user_model,
    login,
    logout,
)
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm, UserUpdateForm
from .models import User


def login_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        next = request.GET.get('next')
        title = "Login"
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user_obj = form.cleaned_data.get("user_obj")
            login(request, user_obj)

            print('user_obj:', user_obj)
            if next:
                return redirect(next)
            return redirect("/account/user")
        return render(request, "login_form.html", {"form": form, "title": title})
    else:
        return redirect("/account/user")


def register_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        next = request.GET.get('next')
        title = "Register"
        # form = RegisterForm(request.POST or None)
        # if form.is_valid():
        #     instance = form.save(commit=False)
        #     instance.save()
        #     if next:
        #         return redirect(next)
        #     return redirect("/login")
        procedure = '''To create an account of CLIC please contact at Central Library & Information Center of Pabna University of Science & Technology.'''
        context = {
            # "form": form,
            "title": title,
            "procedure": procedure,
        }
        return render(request, "registration.html", context)
    else:
        return redirect("/")

@login_required
def logout_view(request):
    logout(request)
    return redirect("/login")


@login_required
def profile_view(request):
    '''
    [user profile]
    [user detal information]
    '''
    if request.user.is_authenticated:
        user_obj = request.user
        context = {
            'instance': user_obj,
            'title': "Profile"
        }
        return render(request, "profile_view.html", context)
    else:
        return redirect("/login")

@login_required
def index_page(request):
    context = {
        'title': 'CLIC, PUST'
    }
    return render(request, "home.html", context)
