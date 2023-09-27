from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.products.urls")),
    path('auth/', include("apps.authsales.urls")),
    path('accounts/', include('django.contrib.auth.urls'))
]
