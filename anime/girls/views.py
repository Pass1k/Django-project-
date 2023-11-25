from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import reverse
from django.shortcuts import redirect, render

menu = ['About Page', 'Add Paper', 'Call', 'Sing In']

data_db = [
    {'id': 1, 'title': 'Satoru Gojou', 'content': '28-летний преподаватель Токийского магического колледжа. Мечтает воспитать новое поколение магов, обладающих индивидуальным мышлением и толикой безумной самобытности. Очень умный и увереный в себе мужчина, один из сильнейших магов современности. Беззаботен и никогда не относится к чему-то всерьёз, а также не отличается особым уважением к другим магам, особенно к верхушке магического мира.', 'is_published': True},
    {'id': 2, 'title': 'Mei Mei', 'content': 'Женщина-маг первого класса. Любит деньги и обладает сомнительной моралью. Способна управлять воронами и видеть то, что видят они. Понимая, что её проклятая техника довольна слаба в бою, сосредоточилась на развитии физических способностей и боевых нав', 'is_published': True},
    {'id': 3, 'title': 'Sukuna Ryoumen', 'content': 'Высокоранговое Проклятье', 'is_published': False},
    {'id': 4, 'title': 'Touji Fushiguro', 'content': 'Отец Мэгуми Фусигуро. Маг, у которого нет проклятой энергии из-за небесного проклятия.', 'is_published': True},
]


def index(request): #HttpRequest
    date = {'title': 'Main Page',
            'menu': menu,
            'posts': data_db,
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






