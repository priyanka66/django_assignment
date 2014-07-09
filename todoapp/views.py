from django.http import HttpResponse
import datetime
from todoapp.models import task


def home(request):
    return HttpResponse("Home Page")
