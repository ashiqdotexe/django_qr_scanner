from django.shortcuts import render


def get_qr(request):
    return render(request, "get_qr.html")