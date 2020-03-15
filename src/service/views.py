from django.shortcuts import render

from django.contrib.auth.decorators import login_required

@login_required
def notice_list(request):
    return render(request, "under_constraction.html", {})
