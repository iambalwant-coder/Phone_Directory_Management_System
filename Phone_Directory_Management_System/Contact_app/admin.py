from django.contrib import admin
from.models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email')
    

admin.site.register(Contact, ContactAdmin)