from django.contrib import admin
from django.utils.html import format_html
from .models import Place, SortableImage
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin


class SortableImagesInline(SortableInlineAdminMixin, admin.TabularInline):
    model = SortableImage
    verbose_name_plural = "Фотографии"
    readonly_fields = ['show_preview']
    fields = ('image', 'show_preview', 'order')

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
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = (SortableImagesInline,)


@admin.register(SortableImage)
class ImageAdmin(admin.ModelAdmin):
    pass

