# Generated by Django 2.0 on 2019-01-26 12:47

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0009_jobindexpagejob_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleAdGrantApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', wagtail.core.fields.StreamField((('items', wagtail.core.blocks.StructBlock((('page', wagtail.core.blocks.PageChooserBlock()), ('subitems', wagtail.core.blocks.StreamBlock((('subitem', wagtail.core.blocks.PageChooserBlock()),)))))),), blank=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]