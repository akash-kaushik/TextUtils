# This file is created by me    ------  Akash

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # Index FIle
    return render(request, 'index.html')
    # return HttpResponse("<h1>HOME</h1>")

def analyze(request):
    # Analyze File
    # Get the text
    djtext = request.POST.get("text", "default")

    # Get the CheckBox
    removep = request.POST.get("removepunc", "off")
    fullca = request.POST.get("fullcapt", "off")

    print(djtext)
    print(removep)
    punctuation = """!()-[]{};:'"\,<>./?@#$%^&*_~"""    # List of punctuation's
    analyzed_text = ""      # Blank String
    purpose = ""        # Purpose of the analysing the text

    # Doing the analyzation
    if removep == "on" and fullca == "off":
        purpose = "Remove Punctuation"
        for char in djtext:
            if char not in punctuation:
                analyzed_text += char

    elif removep == "off" and fullca == "on":
        purpose = "Upper Case All"
        analyzed_text = djtext.upper()

    elif removep == "on" and fullca == "on":
        purpose = "Remove Punctuation and Upper Case All"
        for char in djtext:
            if char not in punctuation:
                analyzed_text += char
                analyzed_text = analyzed_text.upper()

    else:
        purpose = "Noting is selected"
        analyzed_text = djtext

    analyze_dict = {"purpose": purpose, "analyze_text": analyzed_text}
    return render(request, "analyze.html", analyze_dict)

def about(request):
    return render(request, "about.html")
