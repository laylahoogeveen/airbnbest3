# from bs4 import BeautifulSoup
import openpyxl
from pathlib import Path
from bnbs.models import Accomodation
import os
import sys
import re

PROPERTY_TYPE_CHOICES = ['Barn', 'Boat', 'Bus', 'Camper/RV', 'Campsite',
                        'Cave', 'Earth house', 'Entire bed and breakfast', 'Entire bungalow',
                        'Entire cabin', 'Entire chalet', 'Entire condominium (condo)',
                        'Entire cottage', 'Entire guest suite', 'Entire guesthouse',
                        'Entire home/apt', 'Entire loft', 'Entire place', 'Entire rental unit',
                        'Entire residential home', 'Entire serviced apartment', 'Entire townhouse',
                        'Entire villa', 'Farm stay', 'Floor', 'Houseboat', 'Private room',
                        'Private room in bed and breakfast', 'Private room in boat',
                        'Private room in bungalow', 'Private room in cabin',
                        'Private room in casa particular', 'Private room in condominium (condo)',
                        'Private room in dome house', 'Private room in earth house',
                        'Private room in farm stay', 'Private room in floor',
                        'Private room in guest suite', 'Private room in guesthouse',
                        'Private room in hostel', 'Private room in houseboat',
                        'Private room in island', 'Private room in loft', 'Private room in minsu',
                        'Private room in nature lodge', 'Private room in rental unit',
                        'Private room in residential home', 'Private room in serviced apartment', 
                        'Private room in tiny house', 'Private room in townhouse',
                        'Private room in villa', 'Room in aparthotel', 'Room in bed and breakfast',
                        'Room in boutique hotel', 'Room in casa particular', 'Room in hostel',
                        'Room in hotel', 'Room in serviced apartment',
                        'Shared room in bed and breakfast', 'Shared room in boat',
                        'Shared room in hostel', 'Shared room in houseboat',
                        'Shared room in loft', 'Shared room in rental unit',
                        'Shared room in residential home', 'Tiny house', 'Tipi', 'Tower', 'Yurt']

PROPERTY_CHOICES = ['Aparthotel', 'Barn', 'Bed and breakfast', 'Boat', 
                    'Boutique hotel', 'Bus', 'Bungalow', 'Cabin', 'Camper/RV', 'Campsite',
                    'Casa particular', 'Cave', 'Earth house', 'Condo', 'Cottage',
                    'Dome house', 'Farm', 'Floor', 'Guest suite', 'Guesthouse', 'Home/apt',
                    'Hostel', 'Houseboat', 'Hotel', 'Island', 'Loft', 'Minsu', 'Nature lodge',
                    'Rental unit', 'Residential home', 'Serviced apartment',
                    'Tiny house', 'Tipi', 'Tower', 'Townhouse', 'Villa', 'Yurt']

ROOM_TYPE_CHOICES = ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room']

def run():

                                add = Text.objects.create(author="Suetonius", text="De vita Iulii", line=chap, word=word)
                                add.save()



    with open(os.path.join(sys.path[0], 'pharsalia_lat.xml')) as text:
        add = Text.objects.create(author="Lucanus", text="Bellum Civile", book_num=boek, line=line_num, word=word)



    # with open(os.path.join(sys.path[0], 'suet.caes_lat.xml')) as text:
    #     soup = BeautifulSoup(text, "xml")

    # for book in soup.find_all('div1', attrs={'type': 'life', 'n': 'nero'}):
    #     texts = book.descendants
    #     for chapter in texts:
    #         if chapter.name == 'div2':
    #             chap = chapter['n']
    #             print(chap)
    #             print(chapter.text)
    #             chap_text = chapter.text

    #             line_num = 0
    #             chap_text = chap_text.replace('\n', ' ')
    #             split = chap_text.split(" ")
    #             for word in split:
    #                 if word != "":
    #                     add = Text.objects.create(author="Suetonius", text="De vita Neronis", line=chap, word=word)
    #                     print(chap, word)
    #                     add.save()