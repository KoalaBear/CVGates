from django.urls import path

from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('index.html', lambda x: views.redirect('/')),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages')

]
