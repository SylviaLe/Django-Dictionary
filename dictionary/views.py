from django.shortcuts import render
from PyDictionary import PyDictionary  #we use module this time instead of api

# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')  #get the input from the field with the attrs name=search
    dict = PyDictionary()
    msg = ''
    try: 
        meaning = dict.meaning(search)
        synonyms = dict.synonym(search)
        antonyms = dict.antonym(search)

        mean = {}

        if 'Noun' in meaning:
            mean['noun'] = meaning['Noun']

        if 'Verb' in meaning:
            mean['verb'] = meaning['Verb']

        if 'Adjective' in meaning:
            mean['adjective'] = meaning['Adjective']

        if 'Adverb' in meaning:
            mean['adverb'] = meaning['Adverb']

        

        context = { 
            'word': search,
            'mean': mean,
            'syn': synonyms, 
            'ant': antonyms,
            'msg': ''
        }
    except:
        msg = 'Word not exist!'
        context = { 
            'word': '',
            'mean': '',
            'syn': '', 
            'ant': '',
            'msg': msg
        }
    return render(request, 'word.html', context)