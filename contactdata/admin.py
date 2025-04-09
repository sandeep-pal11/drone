from django.contrib import admin

# Register your models here.
from contactdata.models import ContactData  # Import the model

# Register the model so it shows up in the admin
admin.site.register(ContactData)