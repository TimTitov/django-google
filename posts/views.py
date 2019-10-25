from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.
#@login_required
def test(request):
    import pprint
    pprint.pprint(request.user)
    return HttpResponse('zzzzzzzz')# + json.dumps((request.user)))