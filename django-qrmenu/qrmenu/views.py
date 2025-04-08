from django.shortcuts import render
from .forms import QRCodeForm


def generate_qr_code(request):
    if request.method == 'POST':
        return
    else:
        form = QRCodeForm()
        context ={
            'form': form,
        }
        return render(request, 'generate_qr_code.html', context)