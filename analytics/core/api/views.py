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
        ["How to Build a Website in 10 Minutes", "1,245,678", "98,765", "12,345"],
        ["Top 5 AI Tools for Developers", "987,654", "85,432", "9,876"],
        ["Python for Beginners - Full Course", "876,543", "74,321", "8,765"],
        ["10 Tips to Boost Your Coding Skills", "765,4345", "65,210", "7,654"],
        ["The Future of Artificial Intelligence", "654,321", "54,109", "6,543"],
        ["Understanding Neural Networks", "543,210", "43,987", "5,432"],
        ["How to Get Your First Tech Job", "432,109", "32,876", "4,321"],
        ["React vs Vue vs Angular - Which One to Learn?", "321,098", "21,765", "3,210"],
        ["Building a Portfolio Website from Scratch", "210,987", "10,654", "2,109"],
        ["How to Make Money as a Developer", "109,876", "5,432", "1,098"],
    ]

    return JsonResponse(data, safe=False)

    # return JsonResponse({
    #     "labels": ["Aug", "Sept", "Oct", "Nov", "Dec", "Jan"],
    #     "data": [randint(1000*i, 1000*(i+10)) for i in range(6)],
    # })
