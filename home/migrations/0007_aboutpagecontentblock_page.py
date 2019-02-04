# Generated by Django 2.0 on 2019-01-26 11:57

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_aboutpagecontentblock_aboutpageoffice'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpagecontentblock',
            name='page',
            field=modelcluster.fields.ParentalKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='content_blocks', to='home.AboutPage'),
            preserve_default=False,
        ),
    ]
