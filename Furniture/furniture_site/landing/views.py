from furniture_app.utils import *
from landing.models import MainImage


def index(request):
    project_photo = MainImage.objects.all()
    context = {
        'menu': menu,
        'title': 'Главная',
        'project_photo': project_photo
    }

    return render(request, 'furniture_app/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О нас',
    }
    return render(request, 'furniture_app/about.html', context=context)


def contact(request):
    context = {
        'menu': menu,
        'title': 'Контакты',
    }
    return render(request, 'furniture_app/contact.html', context=context)
