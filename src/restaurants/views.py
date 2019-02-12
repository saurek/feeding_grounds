from django.http import HttpResponse
from django.shortcuts import render
import random


# Create your views here.
# function based view
def home(request):
    html_var = str(random.randint(0, 1000)) + ' tanks '
    return render(request, "base.html", {"html_var": html_var})  # response
