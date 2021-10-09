# import openpyxl
import requests
# from pathlib import Path
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bnbs.models import Accommodation
# import os
# import sys
import re

def run():
    accs = Accommodation.objects.filter(pk__gt=404).all()
    # listje = []
    total = 0
    i = 0
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path=r'C:/Users/Layla/.wdm/drivers/chromedriver/win32/94.0.4606.61/chromedriver.exe', options=options)
    
    for a in accs:
        total = total + 1
        
        URL = a.listing_url
        if check_url(URL, driver) == True:
            i=i+1
            print (i, "van de", total)
            a.delete()
            # listje.append(a.pk)
        if i > 1000:
            break
        
    print ('\n')
    print ('\n')
    print ('\n')
    print ("Final")
    print ('\n')
    print (i, "van de", total, "verwijderd")
    driver.quit()
    
    # print (len(listje))
    # print (listje)

def check_url(url, driver):
    page = requests.get(url)
    driver.get(url)
    time.sleep(5)
    res=driver.page_source
    # driver.quit()
    soup = BeautifulSoup(res, "html.parser")

    soup = str(soup)
    # driver.close()
    if "Permission denied by Himeji" in soup:
        return True
    
    return False



# PROPERTY_TYPE_CHOICES = ['Barn', 'Boat', 'Bus', 'Camper/RV', 'Campsite',
#                         'Cave', 'Earth house', 'Entire bed and breakfast', 'Entire bungalow',
#                         'Entire cabin', 'Entire chalet', 'Entire condominium (condo)',
#                         'Entire cottage', 'Entire guest suite', 'Entire guesthouse',
#                         'Entire home/apt', 'Entire loft', 'Entire place', 'Entire rental unit',
#                         'Entire residential home', 'Entire serviced apartment', 'Entire townhouse',
#                         'Entire villa', 'Farm stay', 'Floor', 'Houseboat', 'Private room',
#                         'Private room in bed and breakfast', 'Private room in boat',
#                         'Private room in bungalow', 'Private room in cabin',
#                         'Private room in casa particular', 'Private room in condominium (condo)',
#                         'Private room in dome house', 'Private room in earth house',
#                         'Private room in farm stay', 'Private room in floor',
#                         'Private room in guest suite', 'Private room in guesthouse',
#                         'Private room in hostel', 'Private room in houseboat',
#                         'Private room in island', 'Private room in loft', 'Private room in minsu',
#                         'Private room in nature lodge', 'Private room in rental unit',
#                         'Private room in residential home', 'Private room in serviced apartment', 
#                         'Private room in tiny house', 'Private room in townhouse',
#                         'Private room in villa', 'Room in aparthotel', 'Room in bed and breakfast',
#                         'Room in boutique hotel', 'Room in casa particular', 'Room in hostel',
#                         'Room in hotel', 'Room in serviced apartment',
#                         'Shared room in bed and breakfast', 'Shared room in boat',
#                         'Shared room in hostel', 'Shared room in houseboat',
#                         'Shared room in loft', 'Shared room in rental unit',
#                         'Shared room in residential home', 'Tiny house', 'Tipi', 'Tower', 'Yurt']

# PROPERTY_CHOICES = ['Aparthotel', 'Barn', 'Bed and breakfast', 'Boat', 
#                     'Boutique hotel', 'Bus', 'Bungalow', 'Cabin', 'Camper/RV', 'Campsite',
#                     'Casa particular', 'Cave', 'Earth house', 'Condo', 'Cottage',
#                     'Dome house', 'Farm', 'Floor', 'Guest suite', 'Guesthouse', 'Home/apt',
#                     'Hostel', 'Houseboat', 'Hotel', 'Island', 'Loft', 'Minsu', 'Nature lodge',
#                     'Rental unit', 'Residential home', 'Serviced apartment',
#                     'Tiny house', 'Tipi', 'Tower', 'Townhouse', 'Villa', 'Yurt']


# ROOM_TYPE_CHOICES = ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room']

# xlsx_file = Path('data\curated_data', 'shop_clean.xlsx')
# wb_obj = openpyxl.load_workbook(xlsx_file)
# sheet = wb_obj.active

# Shop
# def run():
#     for row in sheet.iter_rows():
        
#         nm = row[0].value
#         lat = row[1].value
#         long = row[2].value
        
#         add = ShoppingArea.objects.create(name = nm, latitude = lat, longitude = long)
#         add.save()
# Art
# def run():
#     i = 0
#     for row in sheet.iter_rows():
#         i = i + 1
#         # if i % 50 == 0:
#         print (i)
        
#         trc = row[0].value
#         lat = row[1].value
#         long = row[2].value
#         nm = row[3].value
#         descr = row[4].value
#         nm_en = row[5].value
#         descr_en = row[6].value
#         addr = row[7].value
#         link = row[8].value
#         if link != None:
#             link = link.partition(' -')[0]
#         md = row[9].value
#         if md != None:
#             md = md.partition(' -')[0]
#         thmb = row[10].value

        
#         add = Art.objects.create(trcid = trc, name = nm, name_en = nm_en,
#                                         latitude = lat, longitude = long,
#                                         description = descr,
#                                         description_en = descr_en, address = addr,
#                                         url = link, media = md, thumbnail = thmb)
#         add.save()


# Restaurants
# def run():
#     i = 0
#     for row in sheet.iter_rows():
#         i = i + 1
#         if i % 50 == 0:
#             print (i)
        
#         nm = row[0].value
#         lat = row[1].value
#         long = row[2].value
#         descr = row[3].value
#         nm_en = row[4].value
#         descr_en = row[5].value
#         addr = row[6].value
#         link = row[7].value
#         md = row[8].value
#         if md != None:
#             md = md.partition(',')[0]
#         thmb = row[9].value

#         add = Restaurant.objects.create(name = nm, latitude = lat, longitude = long,
#                                         description = descr, name_en = nm_en,
#                                         description_en = descr_en, address = addr,
#                                         url = link, media = md, thumbnail = thmb)
#         add.save()

# Accommodations
# def run():
#     i = 0
#     for row in sheet.iter_rows():
#         i = i + 1
#         if i % 1000 == 0:
#             print (i)
        
#         id = row[0].value
#         nm = row[1].value
#         rvw = row[2].value
#         dscr = row[3].value
#         nbh = row[4].value
#         lat = row[5].value
#         long = row[6].value
#         prop_type = row[7].value
#         prop = row[8].value
#         room = row[9].value
#         accs = row[10].value 
#         brooms = row[11].value
#         bds = row[12].value
#         baths = row[13].value
#         bthsh= row[14].value
#         am = row[15].value
#         pr_eu = row[16].value
#         pr_us = row[17].value
#         lsturl = row[18].value
#         pic = row[19].value

#         add = Accommodation.objects.create(room_id = id, name = nm, review = rvw,
#                                             description = dscr, neighbourhood = nbh,
#                                             latitude = lat, longitude = long,
#                                             property_long = prop_type, property = prop,
#                                             room_type = room, accommodates = accs,
#                                             bedrooms = brooms, beds = bds,
#                                             number_of_baths = baths, bathroom_shared = bthsh,
#                                             amenities = am, price_eu = pr_eu, price_us = pr_us,
#                                             listing_url = lsturl, picture_url = pic)
#         add.save()