from django.contrib import admin

# Register your models here.
from .models import FederalAgency, StateAgency, SubRecipient

admin.site.register(FederalAgency)
admin.site.register(StateAgency)
admin.site.register(SubRecipient)
