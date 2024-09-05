from django.shortcuts import render
from django.http import HttpResponse


def test_view(request):
    return HttpResponse("httpresponse")


def main_page_view(request):
    return render(request, 'home.html')
# Create your views here.
