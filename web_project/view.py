from django.http import HttpResponse
from django.shortcuts import render
def home(request):

    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('UPPERCASE','off')
    newlineremover = request.POST.get('Newlineremover','off')
    extraspaceremover = request.POST.get('Spaceremover','off')
    charcount = request.POST.get('Charcount','off')

    purpose = ""
    ana = djtext 

    if removepunc == "on":
        an = ""
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for i in djtext:
            if i not in punctuation:
                an += i
        ana = an
        purpose += "Remove punctuation "

    if uppercase == "on":
        ana = ana.upper()
        purpose +=  "| UPPERCASE "
    
    if newlineremover == "on":
        an = ""
        for i in ana:
            if i != '\n' and i != '\r' :
                an += i
        purpose += "| New Line Remover "
        ana  = an
    
    if extraspaceremover == "on":
        an = ""
        for i,char in enumerate(ana):
            if not( ana[i] == ' ' and ana[i+1] == ' '):
                an += char
        ana = an
        purpose += "| Extra Space Remover "
    
    if charcount == "on":
        count = 0
        for i in djtext:
            if i.isalpha():
                count += 1
        ana += str('\n Total character count is : ') + str(count) 
        purpose  += "| Character Count " 
    para = {'purpose':purpose,'analyzed_text' : ana}
    if removepunc == "on" or uppercase == "on" or newlineremover == "on" or extraspaceremover == "on" or charcount == "on" :
        return render(request,'analyze.html',para)
    else:
        return HttpResponse("Error choose correct option")
