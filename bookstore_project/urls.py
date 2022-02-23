from django.conf import settings # new
from django.conf.urls.static import static # new
from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')), # new

    # Local apps
    
    path('', include('pages.urls')),
    path('books/', include('books.urls')), # new
    path('orders/', include('orders.urls')), # new
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # new