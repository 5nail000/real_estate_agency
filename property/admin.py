from django.contrib import admin
from .models import Flat


# admin.site.register(Flat)

class FlatAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    # list_filter = ['town']
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ("created_at",)


admin.site.register(Flat, FlatAdmin)

# '''
