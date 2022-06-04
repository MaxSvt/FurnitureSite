from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from furniture_app.utils import *
from landing.forms import FeedBackForm
from landing.models import *


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
    context = {}
    form = FeedBackForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            print("yes")
            data = request.POST
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            phone_number = data.get("phone_number")
            email = data.get("email")
            message = data.get("message")

            ContactForm.objects.create(first_name=first_name, last_name=last_name, phone_number=phone_number,
                                       email=email, message=message)

            send_message(form.cleaned_data['first_name'], form.cleaned_data['last_name'],
                         form.cleaned_data['phone_number'], form.cleaned_data['email'],
                         form.cleaned_data['message'])
            context = {'success': 1}
            # return HttpResponseRedirect(reverse('home'))
        else:
            print("no")
    else:
        form = FeedBackForm()
    context['form'] = form
    context['menu'] = menu
    context['title'] = "Контакты"

    return render(request, 'furniture_app/contact.html', context=context)


def send_message(first_name, last_name, phone_number, email, message):
    text = get_template('furniture_app/message.html')
    html = get_template('furniture_app/message.html')
    context = {'first_name': first_name, 'last_name': last_name, 'phone_number': phone_number, 'email': email,
               'message': message}
    subject = 'Сообщение от пользователя'
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['manager@example.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
