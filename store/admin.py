from django.contrib import admin
from .models import Store

# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'updated')
    ordering = ('title',)
    search_fields = ('title',)

admin.site.register(Store, StoreAdmin)