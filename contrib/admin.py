from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Autor


class AtutorInline(admin.StackedInline):
    model = Autor
    can_delete = False  

class CustomUserAdmin(UserAdmin):
    inlines = (AtutorInline,)


admin.site.unregister(User)  
admin.site.register(User, CustomUserAdmin)  
