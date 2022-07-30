# Generated by Django 3.2.14 on 2022-07-30 00:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.FileField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]