from django.contrib import admin
from .models import Place, Image


class ImagesInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = (ImagesInline,)


admin.site.register(Image)
