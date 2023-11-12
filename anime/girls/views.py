from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def index(request): #HttpRequest
    return HttpResponse("The page of girls")


def categories(request, cat_id):
    return HttpResponse(f"<h1>The Categories page</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>The Categories page</h1><p>slug : {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        raise Http404()
    return HttpResponse(f"<h1>Archive by years</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found</h1>")




