from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def gallery(request):
    return render(request, "gallery.html")

def gallerysingle(request):
    return render(request, "gallery-single.html")

def samplepage(request):
    return render(request, "sample-inner-page.html")

def services(request):
    return render(request, "services.html")