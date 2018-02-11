from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^login/', views.login_page, name='login_page'),
    url(r'^register/', views.register_page, name='login_page'),
    url(r'^postSingin/', views.postSingin, name='welcome page'),
    url(r'^logout/', views.logout, name='welcome page'),
    url(r'^editProfile/', views.editProfile, name='edit_profile')

 ]
