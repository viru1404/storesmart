from django.conf.urls import url,include
from .views import *
urlpatterns = [
    url(r'^$', home,name="home"),
    url(r'^edit_warehouse/(?P<id>[\w\-]+)/$',edit_warehouse,name='edit'),
    url(r'^account/register/$',register,name='register'),
    url(r'^account/login/$',logintoit,name='login'),
    url(r'^account/logout/$',logout1,name='logout'),
    url(r'^index/$',index,name='index'),
    url(r'^add_warehouse/$',add_warehouse,name='add_warehouse'),
    url(r'^order/$', orders,name="order"),
]
