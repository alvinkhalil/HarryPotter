# Generated by Django 3.2.5 on 2021-07-19 13:54

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[700, 450], upload_to='', verbose_name='Şəkil əlavə et'),
        ),
    ]