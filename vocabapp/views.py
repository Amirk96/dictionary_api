from django.shortcuts import render
import requests
import json

def split_api(msg):
    pass

word = ''
phonetics = []
meanings = []
def vocab(request):
    word = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en_US/information')
    data = json.loads(word.text)
    content = {
        'word' : data[0]['word'],
        'phonetics' : data[0]['phonetics'],
        'meanings' : data[0]['meanings'],
    }
    return render(request, 'vocab.html', content)
    #print(json.loads(word.text))
    #print(type(json.loads(word.text)))
    #print(data[0]['word'])
    ''' print(data[0]['phonetics'])
    print(data[0]['meanings'])
    for v in data[0]['meanings']:
        print(v)
        meanings.append(v)
    
    
    print(meanings[0]['definitions'][0]['definition'])
        
    content = {
        'word': data[0]['word'],
        'phonetics': data[0]['phonetics'],
        'meanings': data[0]['meanings'],
    } '''
    ''' for entry in data:
        print(entry)
        print(type(entry)) '''
        
    #print(word.json())
    #print('')
    ''' for l in word.json():        
        for k,v in l.items():
            print(k,v)
            print('')
            if k == 'word':
                word = v
            elif k == 'phonetics':
                phonetics = v
            elif k == 'meanings':
                meanings = v
    print(word)
    print(phonetics)
    print(meanings) '''
    