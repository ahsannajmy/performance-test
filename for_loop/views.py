from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.

def loop_view(request):
    iterations = 1000000  # Adjust the number of iterations as needed

    count = 0
    for i in range(iterations):
        count += 1
    



