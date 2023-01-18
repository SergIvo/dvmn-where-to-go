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
        return format_html(
            '<img style="max-height:200px" src="{url}"/>',
            url=obj.image.url
        )

    show_preview.short_description = 'Превью'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ('title',)

    inlines = (SortableImagesInline,)


@admin.register(SortableImage)
class ImageAdmin(admin.ModelAdmin):
    pass
