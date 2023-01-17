from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = HTMLField(verbose_name='Развернутое описание')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class SortableImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='images'
    )
    image = models.ImageField(verbose_name='Изображение')
    order = models.PositiveIntegerField(
        verbose_name='Порядковый номер изображения',
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order} {self.place.title}'
