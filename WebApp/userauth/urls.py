from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',views.userlogin),
    path('sign-up',views.usersignup,name='sign-up'),
    path('logout',views.deletesession,name='logout'),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('dash_bord',views.deshbord,name='dash_bord'),
    path('create_project/<int:id>/',views.createproject),
    path('cardfilter',views.cardfilter),
    path('autocad',views.autocadexprt),
    path('toolbar',TemplateView.as_view(template_name='toolbar.html'), name='toolbar'),
    #path('download', views.download, name='download'),
    path('layout_download', views.layout_download, name='layout_download'),
    
    
    #reset password urls.......................
    #path('password_reset/',auth_views.PasswordResetView.as_view(), name = 'password_reset'),
    #path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    #path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
    #path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
    #path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]