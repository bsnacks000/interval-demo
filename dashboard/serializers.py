from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Building, Pump, Boiler


class UserSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.HyperlinkedRelatedField(view_name='dashboard:user-detail', read_only=True)
    class Meta:
        model = User
        fields = ('id','username', 'email', 'first_name', 'last_name')


class BuildingSerializer(serializers.HyperlinkedModelSerializer):

    bdbid = serializers.HyperlinkedRelatedField(view_name='dashboard:building-detail', read_only=True)
    class Meta:
        model = Building
        fields = ['bdbid', 'building_name', 'retrofit_type']


class PumpSerializer(serializers.HyperlinkedModelSerializer):

    bdbid = serializers.HyperlinkedRelatedField(view_name='dashboard:building-detail', read_only=True)
    class Meta:
        model = Pump
        fields = ['bdbid', 'pre_post', 'date_time', 'motor_on', 'motor_off', 'pump']



class BoilerSerializer(serializers.HyperlinkedModelSerializer):

    bdbid = serializers.HyperlinkedRelatedField(view_name='dashboard:building-detail', read_only=True)
    class Meta:
        model = Boiler
        fields = [
            'bdbid', 'pre_post', 'date_time', 'pre_post', 'date_time', 'second_on',
            'usage_ccf', 'temperature', 'hdd_60', 'hdd_62_5', 'hdd_65', 'hdd_67_5', 'hdd_70', 'boiler'
        ]
