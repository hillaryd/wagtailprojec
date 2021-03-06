# Generated by Django 2.0 on 2019-01-26 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0018_auto_20190126_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_telephone', models.CharField(help_text='Telephone', max_length=255)),
                ('contact_email', models.EmailField(help_text='Email address', max_length=255)),
                ('contact_twitter', models.CharField(help_text='Twitter', max_length=255)),
                ('email_newsletter_teaser', models.CharField(help_text='Text that sits above the email newsletter', max_length=255)),
                ('oxford_address_title', models.CharField(help_text='Full address', max_length=255)),
                ('oxford_address', models.CharField(help_text='Full address', max_length=255)),
                ('oxford_address_link', models.URLField(help_text='Link to google maps', max_length=255)),
                ('oxford_address_svg', models.CharField(help_text='Paste SVG code here', max_length=9000)),
                ('bristol_address_title', models.CharField(help_text='Full address', max_length=255)),
                ('bristol_address', models.CharField(help_text='Full address', max_length=255)),
                ('bristol_address_link', models.URLField(help_text='Link to google maps', max_length=255)),
                ('bristol_address_svg', models.CharField(help_text='Paste SVG code here', max_length=9000)),
                ('phili_address_title', models.CharField(help_text='Full address', max_length=255)),
                ('phili_address', models.CharField(help_text='Full address', max_length=255)),
                ('phili_address_link', models.URLField(help_text='Link to google maps', max_length=255)),
                ('phili_address_svg', models.CharField(help_text='Paste SVG code here', max_length=9000)),
                ('contact_widget_intro', models.TextField()),
                ('contact_widget_call_to_action', models.TextField()),
                ('contact_widget_button_text', models.TextField()),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Global Settings',
            },
        ),
    ]
