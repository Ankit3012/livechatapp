from django.contrib import admin
from .models import Userprofile,Messages,openticket,closeticket,ticketprofile,userlogin

# Register your models here.
admin.site.register(Userprofile)
admin.site.register(ticketprofile)
admin.site.register(Messages)
admin.site.register(openticket)
admin.site.register(closeticket)
admin.site.register(userlogin)