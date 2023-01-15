from .settings import MEDIA_URL, MEDIA_ROOT
from django.contrib import admin
from django.urls import include, path
from showplace_map import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.render_map),
    path('places/<int:id>', views.send_place_details, name='places'),
    path('tinymce/', include('tinymce.urls'))
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
