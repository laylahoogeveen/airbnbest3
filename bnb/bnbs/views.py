from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
from .models import Accommodation

# Create your views here.from django.http import HttpResponse
def index(request):
    """Return index page"""

    context = {

    # Needed for webpage 
    "room_types": Accommodation.objects.order_by().values('room_type').distinct()
    }

    return render(request, "bnbs/index.html", context)

def results(request):  #price, accommodates, r_type+ facility, facility_range,
    if request.method == 'GET':
        r_type = request.GET.get('room_type')
        pr = request.GET.get('price')
        acc = int(request.GET.get('accommodates'))
        print (acc)

        accs = Accommodation.objects.filter(room_type=r_type, price_eu__lte=pr, accommodates__gte=acc).order_by().values(
            'room_id', 'price_eu', 'name', 'accommodates').distinct()

        context = {
            "results": accs,
            }

    return render(request, "bnbs/results.html", context)


def bnb(request, r_id):
    """Return accommodation accessed through dynamic url"""

    accommodation = Accommodation.objects.filter(room_id=r_id).first()


    context = {
            "bnb": accommodation,
        }

    return render(request, "bnbs/bnb.html", context)