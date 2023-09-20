from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Country)  # Admin page show Country model
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(Book)

