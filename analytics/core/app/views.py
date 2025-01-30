from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def area_chart(request):
    return render(request, 'area_chart.html')

def datatables(request):
    return render(request, 'datatables.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def reports(request):
    return render(request, 'reports.html')