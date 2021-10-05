# from bs4 import BeautifulSoup
import openpyxl
from pathlib import Path
from bnbs.models import Accommodation
# import os
# import sys
# import re

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

xlsx_file = Path('data\curated_data', 'airBnB_data_clean.xlsx')
wb_obj = openpyxl.load_workbook(xlsx_file)
sheet = wb_obj.active
def run():
    for row in sheet.iter_rows():
        
        id = row[0].value
        nm = row[1].value
        rvw = row[2].value
        dscr = row[3].value
        nbh = row[4].value
        lat = row[5].value
        long = row[6].value
        prop_type = row[7].value
        prop = row[8].value
        room = row[9].value
        accs = row[10].value 
        brooms = row[11].value
        bds = row[12].value
        baths = row[13].value
        bthsh= row[14].value
        am = row[15].value
        pr_eu = row[16].value
        pr_us = row[17].value
        lsturl = row[18].value
        pic = row[19].value

        add = Accommodation.objects.create(room_id = id, name = nm, review = rvw,
                                            description = dscr, neighbourhood = nbh,
                                            latitude = lat, longitude = long,
                                            property_long = prop_type, property = prop,
                                            room_type = room, accommodates = accs,
                                            bedrooms = brooms, beds = bds,
                                            number_of_baths = baths, bathroom_shared = bthsh,
                                            amenities = am, price_eu = pr_eu, price_us = pr_us,
                                            listing_url = lsturl, picture_url = pic)
        add.save()