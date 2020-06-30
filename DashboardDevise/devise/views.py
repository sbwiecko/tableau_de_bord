from django.shortcuts import render, HttpResponse

# Create your views here.
def dashboard(request):
    #return HttpResponse("<h1>Bonjour tout le monde!</h1>")
    return render(request, "devise/index.html", context={'liste_nombres': list(range(10))})