from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from anonim.core import views



urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('gallery/', views.gallery, name='gallery'),
    path('upload/', views.upload, name='upload'),
    path('connect/', views.connect_wan, name='connect_wan'),
    path('media/{{image}}', views.media, name='media'),
    path('dash/', views.dash, name='dash'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)