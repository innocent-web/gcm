from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'nom', 'prenoms', 'utilisateur', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'nom', 'prenoms')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)

