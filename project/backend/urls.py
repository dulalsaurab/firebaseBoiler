from django.conf.urls import include, url
from . import views

urlpatterns = [
#     url('', views.home_page, name='home_page'),
#     url(r'^login/', views.login_page, name='login_page'),
#     url(r'^post/', views.post_page, name='post_page'),
#     url(r'^author/', views.home_page, name='home_page'),
      url(r'^save/', views.articleHandler, name='save_article')
 ]
