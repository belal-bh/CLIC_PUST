from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import (
    Book,
    Resource,
    Author,
)


def book_list(request):
    today = timezone.now().date()
    queryset_list = Book.objects.all()

    query = request.GET.get("q")
    by = request.GET.get("by")

    if query:
        if by == 'title':
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)
            ).distinct()
        elif by == 'author':
            queryset_list = queryset_list.filter(
                Q(author__name__icontains=query) |
                Q(author__nicname__icontains=query)
            ).distinct()
        elif by == 'accession_number':
            queryset_list = queryset_list.filter(
                Q(accession_number__icontains=query)
            ).distinct()
        elif by == 'call_number':
            queryset_list = queryset_list.filter(
                Q(call_number__icontains=query)
            ).distinct()
        else:
            queryset_list = queryset_list.filter(
                Q(isbn__icontains=query)
            ).distinct()

    paginator = Paginator(queryset_list, 5)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "Books",
        "page_request_var": page_request_var,
        "today": today,
    }
    # print(context)
    return render(request, "book_list.html", context)


def book_detail(request, id):
    instance = get_object_or_404(Book, id=id)
    # query = request.GET.get("q")
    # print('query:', query)
    # if not query:
    #     return redirect('/resource/book/')
    context = {
        "instance": instance,
        "title": "Book Detail",
    }
    return render(request, "book_detail.html", context)


def resource_list(request):
    today = timezone.now().date()
    queryset_list = Resource.objects.all()

    query = request.GET.get("rq")
    by = request.GET.get("by")
    res_type = request.GET.get("rt")

    if query:
        if res_type != 'all':
            queryset_list = queryset_list.filter(
                Q(resource_type__icontains=res_type)
            ).distinct()
        if by == 'title':
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)
            ).distinct()
        elif by == 'accession_number':
            queryset_list = queryset_list.filter(
                Q(accession_number__icontains=query)
            ).distinct()
        elif by == 'call_number':
            queryset_list = queryset_list.filter(
                Q(call_number__icontains=query)
            ).distinct()

    paginator = Paginator(queryset_list, 5)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "Resources",
        "page_request_var": page_request_var,
        "today": today,
    }
    # print(context)
    return render(request, "resource_list.html", context)


def resource_detail(request, id):
    instance = get_object_or_404(Resource, id=id)
    context = {
        "instance": instance,
        "title": "Resource Detail",
    }
    return render(request, "resource_detail.html", context)


def resource_doclist(request):
    return render(request, "under_constraction.html", {})


def resource_newspaperlist(request):
    return render(request, "under_constraction.html", {})
