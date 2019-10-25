from django.shortcuts import render


def notice_list(request):
    return render(request, "under_constraction.html", {})
