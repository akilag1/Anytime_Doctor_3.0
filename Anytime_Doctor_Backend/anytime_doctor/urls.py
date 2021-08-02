from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",include("accounts.urls")),
    path("accounts/",include("accounts.urls")),
    path("doctors/",include("doctors.urls")),
    path("hospitals/",include("hospitals.urls")),
    path("appotests/",include("appotests.urls")),
    path('admin/', admin.site.urls)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)