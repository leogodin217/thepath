from django.shortcuts import render

from journeys.models import Journey


def home(request):
    journeys = Journey.objects.all()
    context = {"journeys": journeys}
    return render(request, 'journeys/home.html', context)
