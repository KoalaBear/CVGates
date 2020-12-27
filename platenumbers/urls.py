from django.urls import path

from platenumbers import views

urlpatterns = [

    # Plate Numbers
    path('plates/', views.plate),
    path('plates/edit/<int:id>', views.edit_plate),
    path('plates/update/<int:id>', views.update_plate),
    path('plates/delete/<int:id>', views.destroy_plate),
]
