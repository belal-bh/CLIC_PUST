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

from wishlist.models import (
    BookCart,
    ResourceCart
)

from .forms import (
    BookForm,
    ResourceForm
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
    cart_added =  BookCart.objects.all().filter(book=instance, user=request.user).first()

    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid() and not cart_added:
        cart_instance = form.save(commit=False)
        cart_instance.book = instance
        cart_instance.user = request.user
        cart_instance.save()
        print("Submitted BookCart", form)
        # message success
        # messages.success(request, "Successfully Added to BookCart")

    context = {
        "instance": instance,
        "title": "Book Detail",
        "form": form,
        'cart_added': cart_added,
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

    cart_added =  ResourceCart.objects.all().filter(resource=instance, user=request.user).first()

    form = ResourceForm(request.POST or None, request.FILES or None)
    if form.is_valid() and not cart_added:
        cart_instance = form.save(commit=False)
        cart_instance.resource = instance
        cart_instance.user = request.user
        cart_instance.save()
        print("Submitted ResourceCart", form)

    context = {
        "instance": instance,
        "title": "Resource Detail",
        "form": form,
        'cart_added': cart_added,
    }
    return render(request, "resource_detail.html", context)


def resource_doclist(request):
    return render(request, "under_constraction.html", {})


def resource_newspaperlist(request):
    return render(request, "under_constraction.html", {})
