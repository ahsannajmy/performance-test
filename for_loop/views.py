from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.

def loop_view(request):
    iterations = 1000  # Adjust the number of iterations as needed
    start_time = time.time()

    count = 0
    for i in range(iterations):
        count += 1
    
    end_time = time.time()
    duration = end_time - start_time

    return HttpResponse(f"Selesai selama {duration} s")



