from django.urls import path
from  . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    path('base', views.base, name='base'),
    path('baseproducto', views.baseproducto, name='baseproducto'),
    path('baseingreso', views.baseingreso, name='baseingreso'),
    path('', views.index, name='index'),
    path('artistas', views.artistas, name='artistas'),
    path('obras', views.obras, name='obras'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
