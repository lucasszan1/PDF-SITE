from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main_page(request):
    return render(request, 'pdfconversor/pages/main_page.html')