from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def success(request):
    djtext = request.GET.get('text', '')  
    removepunc = request.GET.get('removepunc', 'off')
    upper = request.GET.get('upper', 'off')
    removenewline = request.GET.get('removenewline', 'off')
    removeextraspace = request.GET.get('removeextraspace', 'off')
    countchar = request.GET.get('countchar', 'off')
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    analyzed = djtext  
    
    if removepunc == 'on':
        analyzed = ''.join([char for char in analyzed if char not in punctuation])

    if upper == 'on':
        analyzed = analyzed.upper()

    if removenewline == 'on':
        analyzed = analyzed.replace('\n', '').replace('\r', '')  

    if removeextraspace == 'on':
        analyzed = ' '.join(analyzed.split())

    if countchar == 'on':
        analyzed = f"Character count: {len(analyzed)}"

    
    context = {
        'analyzed': analyzed,
        'removepunc': removepunc,
        'upper': upper,
        'removenewline': removenewline,
        'removeextraspace' : removeextraspace,
        'countchar' : countchar
    }

    return render(request, 'success.html', context)


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')