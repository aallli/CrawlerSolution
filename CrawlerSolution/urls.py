
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from rest_framework import routers
from Crawler import views
from django.conf.urls.i18n import i18n_patterns

router = routers.DefaultRouter()
router.register(r'config', views.ConfigViewSet)

urlpatterns = [
    path('', lambda request: redirect('/fa/admin/', permanent=False)),
    path('api/', include(router.urls)),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)

