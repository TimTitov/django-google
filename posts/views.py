from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.

@login_required
def home(request):
    import pprint
    pprint.pprint(request.user)
    return HttpResponse('HOME')# + json.dumps((request.user)))