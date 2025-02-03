from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from random import randint
from api.models import TotalViewsModel, MostWatchedVideos
from app.models import Movies, Ratings
import csv


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
    quaery = MostWatchedVideos.objects.all()
    return JsonResponse({ 
        "data": [
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
        })

    # return JsonResponse({
    #     "labels": ["Aug", "Sept", "Oct", "Nov", "Dec", "Jan"],
    #     "data": [randint(1000*i, 1000*(i+10)) for i in range(6)],
    # })


def movies(request):
    # Fetch the first 1000 movies
    movie_queryset = Movies.objects.all()[:1000]
    
    data = []
    for item in movie_queryset:
        # Construct the dictionary with key names as expected by the DataTable
        data.append({
            "id": item.id,  
            "title": item.title,
            "year": item.year,
        })
    
    return JsonResponse({
        "data": data 
    })
    
    
def movies_with_ratings(request):
    # Fetch ratings and related movie data
    queryset = Ratings.objects.all().values(
        "rating", "votes", "movie__id", "movie__title", "movie__year"
    ).filter(movie__year__gt=2000).order_by('-rating')[:1000]  # Limit the query to the first 1000 records
    
    data = []  
    
    for item in queryset:
        data.append({
            "id": item["movie__id"],  
            "title": item["movie__title"],
            "year": item["movie__year"],
            "rating": item["rating"],
            "votes": item["votes"]
        })
    
    return JsonResponse({
        "data": data 
    })
    
    
def export(request):
    # Set up the HTTP response with the correct content type and header for downloading CSV
    response = HttpResponse(
        content_type="text/csv",
        headers={'Content-Disposition': 'attachment; filename="movies_export.csv"'}
    )
    
    # Create a CSV writer object
    writer = csv.writer(response)
    
    # Write the header row (column names)
    writer.writerow(['ID', 'Title', 'Year', 'Rating', 'Votes'])
    
    # Fetch the first 1000 ratings and related movie data, filtered by year > 2000 and ordered by rating
    queryset = Ratings.objects.all().values(
        "rating", "votes", "movie__id", "movie__title", "movie__year"
    ).filter(movie__year__gt=2000).order_by('-rating')[:1000]
    
    # Write each row of the data
    for item in queryset:
        writer.writerow([
            item["movie__id"],  # Movie ID
            item["movie__title"],  # Movie Title
            item["movie__year"],  # Movie Year
            item["rating"],  # Movie Rating
            item["votes"],  # Movie Votes
        ])
        
    return response