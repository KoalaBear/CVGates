

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin', admin.site.urls),  # Django admin route
    # path('admin/', admin.site.urls),  # Django admin route
    path("", include("accounts.urls")),  # Auth routes - login / register
    path("", include("app.urls")),  # UI Kits Html files
    path("", include("platenumbers.urls"))  # Platenumbers CRUD
]
