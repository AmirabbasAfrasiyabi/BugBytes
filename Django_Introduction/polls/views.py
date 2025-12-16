from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    """processing - database , cache , rendering Html , """
    print(type(request))
    print(request.user)
    # if request.method == "POST":
    return HttpResponse("Hello, world. You're at the polls index 222.")


