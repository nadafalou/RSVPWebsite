from django.contrib import admin
from invites.models import Invite, Event

# Register your models here.
admin.site.register(Invite)
admin.site.register(Event)