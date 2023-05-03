from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Hello")
    return render(request, "app/index.html", {"a": 1})
