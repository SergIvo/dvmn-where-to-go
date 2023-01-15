# Generated by Django 3.0 on 2023-01-15 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_sortableimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sortableimage',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядковый номер изображения'),
        ),
        migrations.AlterField(
            model_name='sortableimage',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.Place', verbose_name='Место'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
