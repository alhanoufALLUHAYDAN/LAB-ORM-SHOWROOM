from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('cars/', include('cars.urls')),
    path('brands/', include('brands.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


