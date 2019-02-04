# Generated by Django 2.0 on 2019-01-26 11:54

from django.db import migrations, models
import django.db.models.deletion
import home.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0003_auto_20190126_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.TextField(blank=True)),
                ('intro', models.TextField(blank=True)),
                ('involvement_title', models.TextField(blank=True)),
                ('main_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.homeImage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ParticleSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('number', models.PositiveSmallIntegerField(default=50)),
                ('shape_type', models.PositiveSmallIntegerField(choices=[(1, 'circle'), (2, 'edge'), (3, 'triangle'), (4, 'polygon'), (5, 'star'), (6, 'image')], default=1)),
                ('polygon_sides', models.PositiveSmallIntegerField(default=5)),
                ('size', models.DecimalField(decimal_places=1, default=2.5, max_digits=4)),
                ('size_random', models.BooleanField(default=False)),
                ('colour', home.fields.ColorField(default='ffffff', help_text="Don't include # symbol.", max_length=6)),
                ('opacity', models.DecimalField(decimal_places=1, default=0.9, max_digits=2)),
                ('opacity_random', models.BooleanField(default=False)),
                ('move_speed', models.DecimalField(decimal_places=1, default=2.5, max_digits=2)),
                ('move_direction', models.PositiveSmallIntegerField(choices=[(1, 'none'), (2, 'top'), (3, 'top-right'), (4, 'right'), (5, 'bottom-right'), (6, 'bottom'), (7, 'bottom-left'), (8, 'left')], default=1)),
                ('line_linked', models.BooleanField(default=True)),
                ('css_background_colour', home.fields.ColorField(blank=True, help_text="Don't include # symbol. Will be overridden by linear gradient", max_length=6)),
                ('css_background_linear_gradient', models.CharField(blank=True, help_text="Enter in the format 'to right, #2b2b2b 0%, #243e3f 28%, #2b2b2b 100%'", max_length=255)),
                ('css_background_url', models.URLField(blank=True, max_length=255)),
            ],
        ),
    ]