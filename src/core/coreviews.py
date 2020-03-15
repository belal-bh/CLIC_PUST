from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

@login_required
def about_pust(request):
    return render(request, "under_constraction.html", {})

@login_required
def about_clic(request):
    return render(request, "under_constraction.html", {})

@login_required
def about_faculty(request):
    return render(request, "under_constraction.html", {})

@login_required
def about_department(request):
    return render(request, "under_constraction.html", {})

@login_required
def about_institute(request):
    return render(request, "under_constraction.html", {})

@login_required
def about_administration(request):
    return render(request, "under_constraction.html", {})

@login_required
def about_dormitory(request):
    return render(request, "under_constraction.html", {})

@login_required
def about_contact(request):
    return render(request, "under_constraction.html", {})

@login_required
def about_underconstruction(request):
    return render(request, "under_constraction.html", {})
