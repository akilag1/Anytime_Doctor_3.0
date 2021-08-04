# from django.urls import include, path
# from rest_framework import routers
# from . import views
# from .routers import router
# from rest_framework.authtoken.views import obtain_auth_token

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'usersEx', views.UserExViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     # path('regis',register_view,name="regis"),
#     path('login',obtain_auth_token,name="login"),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]