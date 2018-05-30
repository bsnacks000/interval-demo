from import_export import resources, fields, widgets
from .models import Building, Pump, Boiler

class CustomModelResource(resources.ModelResource):

    # need to override in order to correctly exclude id from import
    def get_instance(self, instance_loader, row):
        try:
            params = {}
            for key in instance_loader.resource.get_import_id_fields():
                field = instance_loader.resource.fields[key]
                params[field.attribute] = field.clean(row)
            return self.get_queryset().get(**params)
        except Exception:
            return None

class BuildingResource(CustomModelResource):
    class Meta:
        model = Building
        exclude = ('id', )


class PumpResource(CustomModelResource):

    bdbid = fields.Field(column_name='bdbid', attribute='bdbid', widget=widgets.ForeignKeyWidget(Building, 'bdbid'))
    class Meta:
        model = Pump
        exclude = ('id', )


class BoilerResource(CustomModelResource):

    bdbid = fields.Field(column_name='bdbid', attribute='bdbid', widget=widgets.ForeignKeyWidget(Building, 'bdbid'))
    class Meta:
        model = Boiler
        exclude = ('id', )
