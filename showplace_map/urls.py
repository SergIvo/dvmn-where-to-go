from .settings import MEDIA_URL, MEDIA_ROOT
from django.contrib import admin
from django.urls import path
from showplace_map import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.render_map)
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
