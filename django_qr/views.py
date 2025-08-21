from django.shortcuts import render
from .form import QRGenerator
from django.conf import settings
import qrcode
import os

def get_qr(request):
    if request.method == "POST":
        form = QRGenerator(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data["retaurent_name"]
            url = form.cleaned_data["url"]
            file_name = res_name.replace(" ", "_").lower()+"_media.png"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr = qrcode.make(url)
            qr.save(file_path)

            qr_url = os.path.join(settings.MEDIA_URL, file_name)

        context = {
            "res_name": res_name,
            "qr_url":qr_url,
            "file_name":file_name
        }
        return render(request, "show_qr.html", context)
    else:
        form = QRGenerator()
        context = {
            "form":form,
        }
        return render(request, "get_qr.html", context)