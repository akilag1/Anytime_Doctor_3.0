from django.urls.resolvers import URLPattern
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'doctor_appo', views.AppoViewSet)
router.register(r'test_appo', views.TestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]