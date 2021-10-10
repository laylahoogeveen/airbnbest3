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
    # print (len(Accommodation.objects.all()))

    context = {
    "room_types": Accommodation.objects.order_by().values('room_type').distinct(),
    "num_of_acc": range(1, 17),
    "facilities": list(chain(art, shop)),
    "art": art,
    "shop": shop,
    }

    return render(request, "bnbs/index.html", context)

def results(request):  
    '''Show results of user's search query'''

    art = Art.objects.all()
    shop = ShoppingArea.objects.all()
    property_types = "None"

    if request.method == 'GET':
        
        entire_home = request.GET.get("Entire home/apt")
        private_room  = request.GET.get("Private room")
        hotel_room = request.GET.get("Hotel room")
        shared_room = request.GET.get("Shared room")
        fac_distance = int(request.GET.get("max_distance"))
        room_types = [entire_home, private_room, hotel_room, shared_room]
        # Select all room types if user hasn't selected preference 
        room_types = [i for i in room_types if i != None]
        if room_types == []:
            room_types = ["Entire home/apt", "Private room", "Hotel room", "Shared room"]

        pr = request.GET.get('price')
        acc = int(request.GET.get('accommodates'))
        facility = request.GET.get('facility')
        accs = Accommodation.objects.filter(room_type__in=room_types, price_eu__range=(1, pr), accommodates__gte=acc).order_by().values(
            'room_id', 'price_eu', 'name', 'accommodates', 'picture_url').distinct()
        facility_type = "None"

        # If facility is selected, find out which of the two kinds
        if facility != "None":
            if 'MUSEUM' in facility:
                facility = facility.strip(" MUSEUM")
                facility = Art.objects.get(pk=facility)
                facility_type = "MUSEUM"
            elif 'SHOP' in facility:
                facility = facility.strip(" SHOP")
                facility = ShoppingArea.objects.get(pk=facility)
                facility_type = "SHOP"
            
            bnbs = bnb_near_facility(facility, fac_distance)
            
            accs = Accommodation.objects.filter(room_type__in=room_types, price_eu__range=(1, pr), accommodates__gte=acc, pk__in=bnbs).order_by().values(
            'room_id', 'price_eu', 'name', 'accommodates', 'picture_url').distinct()
        else: 
            accs = Accommodation.objects.filter(room_type__in=room_types, price_eu__range=(1, pr), accommodates__gte=acc).order_by().values(
            'room_id', 'price_eu', 'name', 'accommodates', 'picture_url').distinct()

        context = {
            "results": accs,
            "num_results": len(accs),
            "facility_type": facility_type,
            "price": pr,
            "accommodates": acc,
            "room_types": room_types,
            "facility": facility,
            "fac_distance": fac_distance,
            "art": art,
            "shop": shop,
            "neighbourhoods": Accommodation.objects.values('neighbourhood').distinct(),
            "neighbourhood": "None",
            "property_types": "None",
            "all_property_types": Accommodation.objects.values('property').distinct(),
            }

    return render(request, "bnbs/results.html", context)

def more_filters(request):  
    '''Show results of user's search query'''

    art = Art.objects.all()
    shop = ShoppingArea.objects.all()

    if request.method == 'GET':
        
        entire_home = request.GET.get("Entire home/apt")
        private_room  = request.GET.get("Private room")
        hotel_room = request.GET.get("Hotel room")
        shared_room = request.GET.get("Shared room")
        fac_distance = int(request.GET.get("max_distance"))
        nbh = request.GET.get("neighbourhood")
        room_types = [entire_home, private_room, hotel_room, shared_room]
         

        # Select all room types if user hasn't selected preference 
        room_types = [i for i in room_types if i != None]
        if room_types == []:
            room_types = ["Entire home/apt", "Private room", "Hotel room", "Shared room"]

        pr = request.GET.get('price')
        acc = int(request.GET.get('accommodates'))
        facility = request.GET.get('facility')

        accs = Accommodation.objects.filter(room_type__in=room_types, price_eu__range=(1, pr), accommodates__gte=acc).order_by().values(
                'room_id', 'price_eu', 'name', 'accommodates', 'picture_url').distinct()

        if nbh != "None":
            accs = accs.filter(neighbourhood=nbh)

        facility_type = "None"

        # If facility is selected, find out which of the two kinds
        if facility != "None":
            if 'MUSEUM' in facility:
                facility = facility.strip(" MUSEUM")
                facility = Art.objects.get(pk=facility)
                facility_type = "MUSEUM"
            elif 'SHOP' in facility:
                facility = facility.strip(" SHOP")
                facility = ShoppingArea.objects.get(pk=facility)
                facility_type = "SHOP"
            
            bnbs = bnb_near_facility(facility, fac_distance)
            
            accs =  accs.filter(pk__in=bnbs)

        context = {
            "results": accs,
            "num_results": len(accs),
            "facility_type": facility_type,
            "price": pr,
            "accommodates": acc,
            "room_types": room_types,
            "facility": facility,
            "fac_distance": fac_distance,
            "art": art,
            "shop": shop,
            "neighbourhoods": Accommodation.objects.values('neighbourhood').distinct(),
            "neighbourhood": nbh,
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
     
    return hs(fac_coor, bnb_coor, unit='m')




def accommodation(request, room_id):
    '''Return accommodation accessed through dynamic url'''

    accommodation = Accommodation.objects.filter(room_id=room_id).first()

    context = {
            "bnb": accommodation,
        }

    return render(request, "bnbs/bnb.html", context)