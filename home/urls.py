from django.conf.urls import url, include
from home import views


app_name = 'home'

urlpatterns = [
                    url(r'^$',views.index,name='index'),
                    url(r'^user$',views.dashboard,name='dashboard')
              ]
