# Generated by Django 2.0.10 on 2019-02-03 08:50

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20190203_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmenu',
            name='menu',
            field=wagtail.core.fields.StreamField((('items', wagtail.core.blocks.StructBlock((('page', wagtail.core.blocks.PageChooserBlock(null=True)), ('subitems', wagtail.core.blocks.StreamBlock((('subitem', wagtail.core.blocks.PageChooserBlock(null=True)),), editable=False, null=True))), null=True)),), blank=True),
        ),
    ]