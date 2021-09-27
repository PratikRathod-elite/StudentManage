from django.contrib import admin

# Register your models here.
from .models import Contact , Students

admin.site.register(Contact)
admin.site.register(Students)