from django.shortcuts import render
from .models import Feature
# Create your views here.

def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = "Fast"
    feature1.is_true = True
    feature1.details = "Our service is very quick!"

    feature2 = Feature()
    feature2.id = 1
    feature2.name = "Affordable"
    feature2.is_true = True
    feature2.details = "Our service is very affordable"

    feature3 = Feature()
    feature3.id = 2
    feature3.name = "Reliable"
    feature3.is_true = False
    feature3.details = "Our service is very reliable"

    feature4 = Feature()
    feature4.id = 3
    feature4.name = "Easy to use"
    feature4.is_true = True
    feature4.details = "Our service is easy to use"

    features = [feature1, feature2, feature3, feature4]
    return render(request, "index.html", {"features": features})

def form(request):
    return render(request, "form.html")    

def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    print(amount_of_words)
    return render(request, 'counter.html', {'count': amount_of_words})