from django.contrib import admin

from .models import Equip, Grup, Partit

class PartitAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

admin.site.register(Equip)
admin.site.register(Grup)
admin.site.register(Partit, PartitAdmin)
