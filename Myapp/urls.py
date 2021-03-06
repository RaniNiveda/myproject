#from django.urls import include, path
#from django.conf.urls import patterns
from rest_framework.routers import DefaultRouter
from  .views import UserListView
from rest_framework.authtoken import views

router=DefaultRouter()
router.register('users',UserListView,base_name='users')
# urlpatterns = patterns('',
# 	url(r'^',include(router.urls,namespace=1.0)))
from django.urls import path, include

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='token')
]