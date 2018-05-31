from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views
from . import api

app_name='dashboard'
urlpatterns = [
    # app template/form views
    path('', views.index_view, name='index'),
    path('boilers', views.boiler_view, name='boilers'),
    path('pumps', views.pump_view, name='pumps'),

    # REST api links
    path('api/', api.ApiRootView.as_view(), name='api-root'),
    path('api/users/', api.UserListView.as_view(), name='user-list'),
    path('api/users/<int:pk>', api.UserDetailView.as_view(), name='user-detail'),
    path('api/obtain-auth-token/', obtain_auth_token, name='obtain-auth-token'),

    path('api/buildings/', api.BuildingListView.as_view(), name='building-list'),
    path('api/buildings/<int:pk>', api.BuildingDetailView.as_view(), name='building-detail'),

    path('api/boilers/', api.BoilerListView.as_view(), name='boiler-list'),
    path('api/boilers/<int:pk>', api.BoilerDetailView.as_view(), name='boiler-detail'),

    path('api/pumps/', api.PumpListView.as_view(), name='pump-list'),
    path('api/pumps/<int:pk>', api.PumpDetailView.as_view(), name='pump-detail')
]
