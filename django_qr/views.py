from django.shortcuts import render
from .form import QRGenerator

def get_qr(request):
    form = QRGenerator()
    context = {
        "form":form,
    }
    return render(request, "get_qr.html", context)