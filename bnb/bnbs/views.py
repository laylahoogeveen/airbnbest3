from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
# from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from itertools import chain
from haversine import haversine as hs
from django.db.models import Min
# from django.contrib.auth.decorators import login_required
from .models import Accommodation, Art, ShoppingArea

def index(request):
    """Return index page"""

    art = Art.objects.all()
    shop = ShoppingArea.objects.all()

    i = 0
    print("ACCommodations", len(Accommodation.objects.all()))
    for row in Accommodation.objects.all():
        if Accommodation.objects.filter(room_id=row.room_id).count() > 1:
            i = i + 1
            print (row)
            # row.delete()
    
    print("ACCommodations after deleting", len(Accommodation.objects.all()))

    context = {

    # Needed for webpage 
    "room_types": Accommodation.objects.order_by().values('room_type').distinct(),
    "num_of_acc": range(1, 17),
    "facilities": list(chain(art, shop)),
    "art": art,
    "shop": shop,
    }

    return render(request, "bnbs/index.html", context)

def results(request):  
    '''Show results of user's search query'''

    if request.method == 'GET':
        
        entire_home = request.GET.get("Entire home/apt")
        private_room  = request.GET.get("Private room")
        hotel_room = request.GET.get("Hotel room")
        shared_room = request.GET.get("Shared room")
        facility = request.GET.get("facility")
        fac_distance = request.GET.get("fac_distance")
        room_types = [entire_home, private_room, hotel_room, shared_room]
        fac_distance = 0.5

        # Select all room types if user hasn't selected preference 
        room_types = [i for i in room_types if i != None]
        if room_types == []:
            room_types = ["Entire home/apt", "Private room", "Hotel room", "Shared room"]

        pr = request.GET.get('price')
        acc = int(request.GET.get('accommodates'))
        facility = request.GET.get('facility')
        accs = Accommodation.objects.filter(room_type__in=room_types, price_eu__range=(1, pr), accommodates__gte=acc).order_by().values(
            'room_id', 'price_eu', 'name', 'accommodates', 'picture_url').distinct()
        
        # If facility is selected, find out which of the two kinds
        if facility is not None:
            if 'MUSEUM' in facility:
                facility = facility.strip(" MUSEUM")
                facility = Art.objects.get(pk=facility)
            else:
                facility = facility.strip(" SHOP")
                facility = ShoppingArea.objects.get(pk=facility)
            
            bnbs = bnb_near_facility(facility, fac_distance)
            

            accs = Accommodation.objects.filter(room_type__in=room_types, price_eu__range=(1, pr), accommodates__gte=acc, pk__in=bnbs).order_by().values(
            'room_id', 'price_eu', 'name', 'accommodates', 'picture_url').distinct()
            print (len(accs))
            print ('\n')
        else: 
            accs = Accommodation.objects.filter(room_type__in=room_types, price_eu__range=(1, pr), accommodates__gte=acc).order_by().values(
            'room_id', 'price_eu', 'name', 'accommodates', 'picture_url').distinct()

        context = {
            "results": accs,
            "price": pr,
            "accommodates": acc,
            "room_types": room_types,
            "facility": facility,
            }

    return render(request, "bnbs/results.html", context)

def bnb_near_facility(facility, max_distance):
    '''Find bnbs in near chosen facility within range max_distance'''

    bnbs = Accommodation.objects.all()
    results = []

    for bnb in bnbs:
        if bnb.latitude != None:
            if calculate_distance(bnb, facility) <= max_distance:
                results.append(bnb.pk)

    return results


def calculate_distance(bnb, facility):
    '''Calculate distance between two objects'''

    fac_coor = (facility.latitude, facility.longitude)
    bnb_coor = (bnb.latitude, bnb.longitude)
     
    return hs(fac_coor, bnb_coor)




def accommodation(request, r_id):
    '''Return accommodation accessed through dynamic url'''

    accommodation = Accommodation.objects.filter(room_id=r_id).first()


    context = {
            "bnb": accommodation,
        }

    return render(request, "bnbs/bnb.html", context)