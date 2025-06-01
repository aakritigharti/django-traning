from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    return HttpResponse("You can view this Response")

def profile(request):
    if  not request.user.is_authenticated:
        return HttpResponse("You are not allowed to view this")


    context ={}
    return render(request, "customauth/profile.html", context) 
 
def newprofile(request):
    if  not request.user.is_authenticated:
        return HttpResponse("You are not allowed to view this")


    context ={
        "message": "You can view this"
    }
    return render(request, "customauth/newprofile.html", context)   
 



    
        