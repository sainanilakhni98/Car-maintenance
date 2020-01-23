from django.urls import path
from .import views

urlpatterns = [
    path('',views.cars),
    path('search/',views.search),
    path("<str:name>/",views.ViewDetails),
    path('<str:name>/<str:model>/',views.CarsDetails),
    path('filldata/',views.filldata)

    
]
