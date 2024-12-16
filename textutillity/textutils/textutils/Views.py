from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

# --> Home Page 
def index(request):
    # params = {'name':'Aqeel','place':'Pakistan'}
    return  render(request,'index.html')
    #return  HttpResponse("Home")

# --> Analyze Page 
@csrf_protect
def Analyze(request):
   #Get the text
    djtext = request.POST.get('text', 'default') 
    removepunc = request.POST.get('removepunc','off')   
    fullcaps = request.POST.get('fullcaps','off')   
    newline = request.POST.get('newline','off') 
    charcount = request.POST.get('charcount','off') 
    params = {'purpose': '', 'analyzed_text': djtext}

# --> Remove Punctuations
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    # --> Count the Char     
    if(charcount == 'on'):
        analyzed = ""
        count  = 0
        for char in djtext:
            count += 1
            params = {'purpose': 'Char Count ', 'analyzed_text': count}
            djtext = analyzed
    
# --> Remove the New Line
    if(newline == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            params = {'purpose': 'New Line Remove', 'analyzed_text': analyzed}
            djtext = analyzed
        # return render(request,'analyze.html',params)

    # --> Convert into UpperCase
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper() + " "
            params = {'purpose': 'Convert into UpperCase', 'analyzed_text': analyzed}
            djtext = analyzed
        # return render(request,'analyze.html',params)

        if(removepunc != "on" and newline !="on" and charcount !="on" and fullcaps !="on"):
            return HttpResponse("please select any operation and try again")        
        # return render(request,'analyze.html',params)
    return render(request,'analyze.html',params)  


def Contact(request):
    return render(request,'contact.html')  

def About(request):
    return render(request,'about.html')

