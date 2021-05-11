from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.logins, name='logins'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('map/', views.map, name='map'),
    path('mapdata/', views.mapdata, name='mapdata'),
    path('getmapdata/', views.getmapdata, name='getmapdata'),

]

#url(r'^data/$', GeoJSONLayerView.as_view(model=PFT), name='data'),