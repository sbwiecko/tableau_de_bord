from django.shortcuts import render, HttpResponse

import api

# Create your views here.
def dashboard(request, days_range=30, currencies="CHF"):
    #return HttpResponse("<h1>Bonjour tout le monde!</h1>")

    days, rates = api.get_ratings(currencies=currencies.split(','),
                                  days=days_range)

    #return render(request, "devise/index.html", context={'liste_nombres': list(range(10))})

    return render(request, "devise/index.html",
                  context={'rates': rates, # rates['EUR'], type(rates)=dic here
                           'days': days})