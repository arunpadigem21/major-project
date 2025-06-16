from django.contrib import admin
from .models import IPAddress

@admin.register(IPAddress)
class IPAddressAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('ip_address',)
