from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework'),
    ),
    path(
        '', render, kwargs={'template_name': 'index.html'}, name='start_page',
    ),
    path('api/', include('foodcartapp.urls')),
    path('manager/', include('restaurateur.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT,
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
