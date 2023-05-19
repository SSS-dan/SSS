from django.http import HttpResponse
from django.shortcuts import render
import users


def index(request):
    return HttpResponse("test")