from django.http import HttpResponse
from django.shortcuts import render
import qr_app


def index(request):
    return HttpResponse("test")