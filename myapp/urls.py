from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('search_ventilador/',views.ventilador_search),
    path('projects/', views.projects),
    path('task/', views.task),
    path('ver_repuestos/<str:nombre_ventilador>/', views.ver_repuestos, name='ver_repuestos'),
    path('ver_despiece/<str:nombre_ventilador>/', views.ver_despiece, name='ver_despiece'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)