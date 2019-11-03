from django.conf.urls import url
from . import views


urlpatterns = [
        
   
    url(r'^signup/$',views.register ,name = 'register'),
    url(r'^login/$',views.signin,name='signin'),
    url(r'^special/$',views.special, name = 'special'),
    url(r'^logout/$',views.user_logout,name='user_logout')
    
]