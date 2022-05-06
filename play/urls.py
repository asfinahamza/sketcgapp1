
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.views.static import serve
default_router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('web.urls')),
    path('',include('movie.urls')),
    path('api/',include('api.urls')),
    path('',include('show.urls')),
    re_path(r'apiauth/', include('rest_framework.urls')),
    re_path(r'auth/', include('rest_framework_social_oauth2.urls')),
]

urlpatterns+= default_router.urls

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]
