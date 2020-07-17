from django.shortcuts import render, redirect #HttpResponse

import api

# Create your views here.
def redirect_index(request):
    return redirect('home', days_range=30, currencies='CHF')

def dashboard(request, days_range=30, currencies="CHF"):
    #return HttpResponse("<h1>Bonjour tout le monde!</h1>")
    #return render(request, "devise/index.html", context={'liste_nombres': list(range(10))})

    days, rates = api.get_ratings(currencies=currencies.split(','),
                                  days=days_range)

    page_label = {5: "semaine", 7: "semaine", 30: "mois", 31: "mois", 365: "année"}.get(
        days_range, "personnalisé"
    )

    return render(request, "devise/index.html",
                  context={'rates': rates, # rates['EUR'], type(rates)=dic here
                           'days': days,
                           'currencies': currencies,
                           'page_label': page_label})