from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import reverse
from django.shortcuts import redirect, render

menu = ['About Page', 'Add Paper', 'Call', 'Sing In']


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request): #HttpRequest
    date = {'title': 'Main Page',
            'menu': menu,
            'float': 39.23,
            'lst': [1, 2, 'abc', True],
            'set': {1, 2, 3, 4, 5},
            'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
            'obj': MyClass(20, 30)
            }
    return render(request, 'girls/index.html', context=date)


def about(request):
    return render(request, 'girls/about.html', {'title': 'About Page'})


def categories(request, cat_id):
    return HttpResponse(f"<h1>The Categories page</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>The Categories page</h1><p>slug : {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('sport', ))
        return HttpResponsePermanentRedirect(uri)
    return HttpResponse(f"<h1>Archive by years</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found</h1>")






