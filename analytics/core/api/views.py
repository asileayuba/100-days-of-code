from django.shortcuts import render
from django.http import JsonResponse
from random import randint
from api.models import TotalViewsModel

def total_views(request):
    queryset = TotalViewsModel.objects.all()
    dct = {
        "labels": [],
        "data": [],
    }
    
    for item in queryset:
        dct["labels"].append(item.label)  
        dct["data"].append(item.views)  
    
    # Return the data as a JSON response
    return JsonResponse(dct)


    # return JsonResponse({
    #     "labels": ["Aug", "Sept", "Oct", "Nov", "Dec", "Jan"],
    #     "data": [randint(1000*i, 1000*(i+10)) for i in range(6)],
    # })