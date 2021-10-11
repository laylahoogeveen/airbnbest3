'''Very ugly and lengthy code to complete and finish all models.
Command needed: python manage.py runscript load_data
Please don't read or use xx
Layla Hoogeveen, Information Organization, October 2021
'''

import openpyxl
from pathlib import Path
from bnbs.models import ShoppingArea

xlsx_file = Path('data\curated_data\clean', 'shop_clean.xlsx')
wb_obj = openpyxl.load_workbook(xlsx_file)
sheet = wb_obj.active

def run():
    '''Provide model ShoppingArea with data from Excel sheet'''

    for row in sheet.iter_rows():
        
        nm = row[0].value
        lat = row[1].value
        long = row[2].value
        
        add = ShoppingArea.objects.create(name = nm, latitude = lat, longitude = long)
        add.save()