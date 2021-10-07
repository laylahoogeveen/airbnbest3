from django.contrib import admin
from .models import Accommodation, Restaurant, Art

# Register your models here.
admin.site.register(Accommodation)
admin.site.register(Restaurant)
admin.site.register(Art)