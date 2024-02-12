
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('help_center_category', views.help_center_category, name='help_center_category'),
    path('help_center', views.help_center, name='help_center'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('video', views.video, name='video'),
    path('price', views.price, name='price'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    