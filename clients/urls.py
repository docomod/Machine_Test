
from django.conf.urls import url 
from django.urls import path, include
from . import views 
from rest_framework import routers


router = routers.DefaultRouter()
router.register('client', views.ClientView)
router.register('user', views.UserView)
router.register('project', views.ProjectView)


urlpatterns = [ 
    url('', include(router.urls)),

]
