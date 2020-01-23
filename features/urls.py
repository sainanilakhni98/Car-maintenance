from django.urls import path
from .import views
urlpatterns = [
    path('',views.features),
    path('maintenance/',views.maintenance),
    path('Carcomponents/',views.Carcomponents)
    #path('update/',views.update)
]
