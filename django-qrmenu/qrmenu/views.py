from django.shortcuts import render
from .forms import QRCodeForm


def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']
            
            
    else:
        form = QRCodeForm()
        context ={
            'form': form,
        }
        return render(request, 'generate_qr_code.html', context)