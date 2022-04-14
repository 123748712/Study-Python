from django.shortcuts import render
from django.http.response import JsonResponse

def omok(request):
    return render(request, 'omok19.html')


