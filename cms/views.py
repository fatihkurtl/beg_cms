from django.shortcuts import render, redirect
from django.utils import translation
# from django.utils.translation import LANGUAGE_SESSION_KEY
from django.conf import settings
from .forms import ContactForm, ContactFormWithDropdown
from .models import Language, Theme, Contact

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # form.save()
            print(form.cleaned_data)
            return redirect('home')
    else:
        form = ContactForm()
        if request.session['theme'] == 'default':
            formWdropdown = ContactFormWithDropdown()
            return render(request, 'pages/index.html', {'form': formWdropdown})
    return render(request, 'pages/index.html', {'form': form})


def set_language(request):
    lang = request.GET.get('lang', 'en')
    print(lang)
    if lang in dict(settings.LANGUAGES):
        translation.activate(lang)
        request.session['django_language'] = lang
        save_lang, created = Language.objects.get_or_create(language=lang)
        if not created:
            print(f"Dil bilgisi güncellendi: {save_lang.language}")
        else:
            print(f"Yeni dil bilgisi kaydedildi: {save_lang.language}")
        
    return redirect(request.META.get('HTTP_REFERER', '/'))


def set_theme(request):
    theme = request.GET.get('theme', 'default')
    print(theme)
    request.session['theme'] = theme
    save_theme, created = Theme.objects.get_or_create(theme=theme)

    if not created:
        print(f"Temayı güncelliyoruz: {save_theme.theme}")
    else:
        print(f"Yeni tema kaydedildi: {save_theme.theme}")
    return redirect(request.META.get('HTTP_REFERER', '/'))