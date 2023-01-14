from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


class ImagesInline(admin.TabularInline):
    model = Image
    verbose_name_plural = "Фотографии"
    readonly_fields = ['show_preview']
    fields = ('image', 'show_preview', 'number')

    def show_preview(self, obj):
        max_width = 250
        image_ratio = obj.image.width / obj.image.height
        return format_html(
            '<img src="{url}" width="{width}" height={height} />',
            url=obj.image.url,
            width=max_width,
            height=max_width / image_ratio
        )
    show_preview.short_description = 'Превью'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = (ImagesInline,)


admin.site.register(Image)
