from django.shortcuts import render, redirect
from django.utils import translation
# from django.utils.translation import LANGUAGE_SESSION_KEY
from django.conf import settings

def index(request):
    return render(request, 'pages/index.html')


def set_language(request):
    lang = request.GET.get('lang', 'en')
    print(lang)
    if lang in dict(settings.LANGUAGES):
        translation.activate(lang)
        request.session['django_language'] = lang
        print(request.session['django_language'])
    return redirect(request.META.get('HTTP_REFERER', '/'))



def set_theme(request):
    theme = request.GET.get('theme', 'default')
    print(theme)
    request.session['theme'] = theme
    return redirect(request.META.get('HTTP_REFERER', '/'))