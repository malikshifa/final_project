from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.logins, name='logins'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('map/', views.tempt, name='map'),
    path('mapdata/', views.tempt, name='mapdata'),
    path('getmapdata/', views.getmapdata, name='getmapdata'),
    # path('singleshape/', views.single_shape, name='singleshape'),
    # path('getcoordlen/', views.get_coord_len, name='get_coord_len'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),
         name='password_reset_complete'),
]
