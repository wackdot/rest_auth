from django.urls import include, re_path
from rest_framework import routers
 
from . import views
 
router = routers.DefaultRouter()
router.register(r'accounts', views.UserView, 'list')
 
urlpatterns = [
    re_path(r'^api/', include(router.urls)),
]