from django.shortcuts import render
from django.http import JsonResponse
from random import randint


def total_views(request):
    return JsonResponse({
        "labels": ["Aug", "Sept", "Oct", "Nov", "Dec", "Jan"],
        "data": [randint(1000*i, 1000*(i+10)) for i in range(6)],
    })