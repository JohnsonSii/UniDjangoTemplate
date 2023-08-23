from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import uuid
import os


def test(request):
    if request.method == 'GET':
        return HttpResponse('success!')
