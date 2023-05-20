from django.contrib import admin
from .models import Flat, Сlaim, Like


class LikeInline(admin.TabularInline):
    # или admin.StackedInline для вертикального отображения

    model = Like
    extra = 0
    raw_id_fields = ('user',)


class FlatAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'address', 'price', 'new_building', 'construction_year', 'town'
        )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony', 'town')
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ("created_at",)
    raw_id_fields = ('liked_by',)
    inlines = [LikeInline]


class СlaimAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'text')
    raw_id_fields = ('user', 'flat')


class LikeAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Сlaim, СlaimAdmin)
admin.site.register(Like, LikeAdmin)

# '''
