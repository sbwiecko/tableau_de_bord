from django.shortcuts import render, HttpResponse

import api

# Create your views here.
def dashboard(request):
    #return HttpResponse("<h1>Bonjour tout le monde!</h1>")

    days, rates = api.get_ratings(currencies=["EUR"], days=300)

    #return render(request, "devise/index.html", context={'liste_nombres': list(range(10))})

    return render(request, "devise/index.html",
                  context={'rates': rates['EUR'],
                           'days': days})