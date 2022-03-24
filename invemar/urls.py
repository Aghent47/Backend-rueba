from django.urls import path
from invemar import views as view

urlpatterns = [
    path('specie_create/', view.SpecieCreate.as_view()),
    path('specie_list/', view.SpecieList.as_view()),
    path('specie_update/<int:pk>/', view.SpecieUpdate.as_view()),
    path('specie_delete/<int:pk>/', view.SpecieDelete.as_view()),

    path('place_create/', view.PlaceCreate.as_view()),
    path('place_list/', view.PlaceList.as_view()),
    path('place_update/<int:pk>/', view.PlaceUpdate.as_view()),
    path('place_delete/<int:pk>/', view.PlaceDelete.as_view()),
   
    path('sighting_create/', view.SightingCreate.as_view()),
    path('sighting_list/', view.SightingList.as_view()),
    path('sighting_update/<int:pk>/', view.SightingUpdate.as_view()),
    path('sighting_delete/<int:pk>/', view.SightingDelete.as_view()),
    
]