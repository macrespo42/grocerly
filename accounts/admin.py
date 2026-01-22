from django.contrib import admin

from .models import Family, User

# Register your models here.
admin.site.register(User)
admin.site.register(Family)
