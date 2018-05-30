from rest_framework.views import APIView
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics
from django.contrib.auth.models import User

from .serializers import UserSerializer, BuildingSerializer, BoilerSerializer, PumpSerializer
from .filters import BuildingFilter, BoilerFilter, PumpFilter
from .models import Building, Boiler, Pump


class ApiRootView(APIView):
    """ returns a hyperlinked directory of API
    """

    def get(self, request, format=None):
        routes = {
            'obtain-auth-token': reverse('dashboard:obtain-auth-token', request=request, format=format),
            'users': reverse('dashboard:user-list', request=request, format=format),
            'buildings': reverse('dashboard:building-list', request=request, format=format),
            'boilers': reverse('dashboard:boiler-list', request=request, format=format),
            'pumps': reverse('dashboard:pump-list', request=request, format=format)
        }

        return Response(routes)



# ----- User Api views restricted to Admin app user only

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, )


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, )



# ---------- Pure Database Model  REST views
# These are basic CRUD Views for each model in the table

class BuildingListView(generics.ListCreateAPIView):
    ''' List all buildings or create a new building
    '''
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_class = BuildingFilter


class BuildingDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''retrieve update or delete a building instance
    '''
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = (permissions.IsAuthenticated,)



class PumpListView(generics.ListCreateAPIView):

    queryset = Pump.objects.all()
    serializer_class = PumpSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_class = PumpFilter


class PumpDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Pump.objects.all()
    serializer_class = PumpSerializer
    permission_classes = (permissions.IsAuthenticated,)



class BoilerListView(generics.ListCreateAPIView):

    queryset = Boiler.objects.all()
    serializer_class = BoilerSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_class = BoilerFilter


class BoilerDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Boiler.objects.all()
    serializer_class = BoilerSerializer
    permission_classes = (permissions.IsAuthenticated, )
