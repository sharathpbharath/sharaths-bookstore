from django.conf import settings # new
from django.conf.urls.static import static # new
from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    # Django admin
    path('anything-but-admin/', admin.site.urls), # new

    # User management
    path('accounts/', include('allauth.urls')), # new

    # Local apps
    
    path('', include('pages.urls')),
    path('books/', include('books.urls')), # new
    path('orders/', include('orders.urls')), # new
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # new


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns