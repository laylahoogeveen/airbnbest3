'''Very ugly and lengthy code to complete and finish all models.
Command needed: python manage.py runscript load_data
Please don't read or use xx
Layla Hoogeveen, Information Organization, October 2021
'''

import openpyxl
from pathlib import Path
from bnbs.models import Accommodation

xlsx_file = Path('data\curated_data\clean', 'airbnb_data_final.xlsx')
wb_obj = openpyxl.load_workbook(xlsx_file)
sheet = wb_obj.active

def run():
    '''Provide model Accommdation with data from Excel sheet'''

    i = 0
    for row in sheet.iter_rows():
        i = i + 1
        if i % 1000 == 0:
            print (i)
        
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


        if nm is not None and len(nm) > 4:
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