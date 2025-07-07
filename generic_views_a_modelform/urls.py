from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # ⬅ přidáno pro přesměrování

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jackets/', include('jackets.urls')),
    path('', lambda request: redirect('jackets/', permanent=False)),  # ⬅ přesměrování z /
]
