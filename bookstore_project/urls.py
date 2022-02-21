from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')), # new

    # Local apps
    path('accounts/', include('users.urls')), # new
    path('', include('pages.urls')),
]