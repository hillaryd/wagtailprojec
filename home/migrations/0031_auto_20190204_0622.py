# Generated by Django 2.0.10 on 2019-02-04 06:22

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20190204_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmenu',
            name='menu',
            field=wagtail.core.fields.StreamField((('items', wagtail.core.blocks.StructBlock((('page', wagtail.core.blocks.PageChooserBlock()), ('subitems', wagtail.core.blocks.StreamBlock((('subitem', wagtail.core.blocks.PageChooserBlock()),), blank=True, null=True))))),), blank=True),
        ),
    ]