from django.conf.urls import url,include
from .views import home
urlpatterns = [
    url(r'^$', home,name="home"),
    url(r'^account/register/$',register,name='register'),
    url(r'^account/login/$',logintoit,name='login'),
    url(r'^account/logout/$',logout1,name='logout'),
]
