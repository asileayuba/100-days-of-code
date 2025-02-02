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

from django.http import JsonResponse

from django.http import JsonResponse

def datatable_api(request):
    data = [
        {"title": "How to Build a Website in 10 Minutes", "views": "1,245,678", "likes": "98,765", "comments": "12,345"},
        {"title": "Top 5 AI Tools for Developers", "views": "987,654", "likes": "85,432", "comments": "9,876"},
        {"title": "Python for Beginners - Full Course", "views": "876,543", "likes": "74,321", "comments": "8,765"},
        {"title": "10 Tips to Boost Your Coding Skills", "views": "765,432", "likes": "65,210", "comments": "7,654"},
        {"title": "The Future of Artificial Intelligence", "views": "654,321", "likes": "54,109", "comments": "6,543"},
        {"title": "Understanding Neural Networks", "views": "543,210", "likes": "43,987", "comments": "5,432"},
        {"title": "How to Get Your First Tech Job", "views": "432,109", "likes": "32,876", "comments": "4,321"},
        {"title": "React vs Vue vs Angular - Which One to Learn?", "views": "321,098", "likes": "21,765", "comments": "3,210"},
        {"title": "Building a Portfolio Website from Scratch", "views": "210,987", "likes": "10,654", "comments": "2,109"},
        {"title": "How to Make Money as a Developer", "views": "109,876", "likes": "5,432", "comments": "1,098"}
    ]
    
    return JsonResponse(data, safe=False)



    # return JsonResponse({
    #     "labels": ["Aug", "Sept", "Oct", "Nov", "Dec", "Jan"],
    #     "data": [randint(1000*i, 1000*(i+10)) for i in range(6)],
    # })