from django.contrib import admin
from apps.user.models import User, Address, Area, VerifyCode

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Area)
admin.site.register(VerifyCode)