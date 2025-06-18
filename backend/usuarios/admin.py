from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MilitarUser

class MilitarUserAdmin(UserAdmin):
    list_display = ('matricula', 'nome_completo', 'tipo', 'is_active')
    fieldsets = (
        (None, {'fields': ('matricula', 'password')}),
        ('Personal Info', {'fields': ('nome_completo',)}),
        ('Permissions', {'fields': ('tipo', 'is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('matricula', 'nome_completo', 'tipo', 'password1', 'password2'),
        }),
    )
    ordering = ('matricula',)

admin.site.register(MilitarUser, MilitarUserAdmin)