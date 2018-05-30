from django_filters import rest_framework as filters
from .models import Building, Boiler, Pump


# these are used to lookup int and str lists via url if needed: ?bdbids=1,2,3,4,
class ListFilter(filters.Filter):
    ''' custom list filter base class -- use subclasses override _parse_list to parse types of values for the url filter
    '''

    def _parse_list(self, value):
        return [v for v in value.split(',')]

    def filter(self,qs,value):
        self.lookup_type = 'in'
        try:
            if value not in (None,''):
                integers = self._parse_list(value)
                return qs.filter(**{'%s__%s'%(self.name, self.lookup_type):integers})
            return qs
        except (ValueError, TypeError) as err:
            return qs


class IntegerListFilter(ListFilter):

    def _parse_list(self, value):
        return [int(v) for v in value.split(',')]


class StrListFilter(ListFilter):

    def _parse_list(self, value):
        return [str(v) for v in value.split(',')]


class BuildingFilter(filters.FilterSet):

    bdbids = IntegerListFilter(name='bdbid')

    class Meta:
        model = Building
        fields = '__all__'


class PumpFilter(filters.FilterSet):

    start_date_time = filters.DateTimeFilter(name='date_time', lookup_expr='gte')
    end_date_time = filters.DateTimeFilter(name='date_time', lookup_expr='lte')

    class Meta:
        model = Pump
        fields = ['bdbid', 'pre_post', 'date_time', 'start_date_time', 'end_date_time', 'pump']


class BoilerFilter(filters.FilterSet):

    start_date_time = filters.DateTimeFilter(name='date_time', lookup_expr='gte')
    end_date_time = filters.DateTimeFilter(name='date_time', lookup_expr='lte')

    class Meta:
        model = Boiler
        fields = ['bdbid', 'pre_post', 'date_time',  'start_date_time', 'end_date_time']
