from django.http import HttpResponse
import datetime
from todoapp.models import task
from django.contrib.auth import authenticate, login
from django.shortcuts import render

def home(request):
    return HttpResponse("Home Page")

def alltasks(request):
	t = task.objects.all()
	return HttpResponse(t)


# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             # Redirect to a success page.
#         else:
#             # Return a 'disabled account' error message
#     else:
#         # Return an 'invalid login' error message.

def get_tasks(request):
	t=task.objects.all()
	return render(request,"task.html",{"tasks":t})

def get_public_tasks(request):
	t=task.objects.all()
	return render(request,"public.html",{"tasks":t})

def get_private_tasks(request):
	t=task.objects.all()
	return render(request,"private.html",{"tasks":t})

