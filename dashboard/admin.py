from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Building, Pump, Boiler
from .resources import BuildingResource, PumpResource, BoilerResource


def generate_all_fields(ModelClass):
    ''' returns complete list of fields names for list_display setting'''
    return [field.name for field in ModelClass._meta.get_fields()]


class BuildingAdmin(ImportExportModelAdmin):
    resource_class = BuildingResource
    list_display = ('bdbid', 'building_name', 'retrofit_type')


class PumpAdmin(ImportExportModelAdmin):
    resource_class = PumpResource
    list_display = generate_all_fields(Pump)


class BoilerAdmin(ImportExportModelAdmin):
    resource_class = BoilerResource
    list_display = generate_all_fields(Boiler)


admin.site.register(Boiler, BoilerAdmin)
admin.site.register(Pump, PumpAdmin)
admin.site.register(Building, BuildingAdmin)
