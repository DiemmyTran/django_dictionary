from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from pyparsing import Word
import pyttsx3
from PyDictionary import PyDictionary


# Create your views here.

def home(request):
    return render(request, 'home.html')


def search_word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()

    meaning = dictionary.meaning(search)
    synonym = dictionary.synonym(search)
    antonym = dictionary.antonym(search)

    context = {
        'search': search,
        'meaning': meaning,
        'synonym': synonym,
        'antonym': antonym,
    }
    return render(request, 'word.html', context)


def audio(request):
    search = request.GET.get('search')
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)  # for female voice
    engine.setProperty('rate', 150)
    engine.say(search)
    engine.runAndWait()
    return HttpResponse(engine.say(search))
