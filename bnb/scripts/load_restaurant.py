'''Very ugly and lengthy code to complete and finish all models.
Command needed: python manage.py runscript load_data
Please don't read or use xx
Layla Hoogeveen, Information Organization, October 2021
'''


import openpyxl
from pathlib import Path
from bnbs.models import Restaurant


xlsx_file = Path('data\curated_data\clean', 'eten_clean.xlsx')
wb_obj = openpyxl.load_workbook(xlsx_file)
sheet = wb_obj.active

def run():
    '''Provide model Restaurant with data from Excel sheet'''

    i = 0
    for row in sheet.iter_rows():
        i = i + 1
        if i % 50 == 0:
            print (i)
        
        nm = row[0].value
        lat = row[1].value
        long = row[2].value
        descr = row[3].value
        nm_en = row[4].value
        descr_en = row[5].value
        addr = row[6].value
        link = row[7].value
        md = row[8].value
        if md != None:
            md = md.partition(',')[0]
        thmb = row[9].value

        add = Restaurant.objects.create(name = nm, latitude = lat, longitude = long,
                                        description = descr, name_en = nm_en,
                                        description_en = descr_en, address = addr,
                                        url = link, media = md, thumbnail = thmb)
        add.save()
