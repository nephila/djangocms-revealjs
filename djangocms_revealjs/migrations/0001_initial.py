# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__latest__'),
        ('filer', '__latest__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FragmentModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('body', models.TextField(verbose_name='body')),
                ('effects', models.CharField(default=b'', max_length=20, blank=True, choices=[(b'fade-out', b'fade-out'), (b'current-visible', b'current-visible'), (b'highlight-red', b'highlight-red'), (b'roll-in', b'roll-in'), (b'highlight-blue', b'highlight-blue'), (b'highlight-current-blue', b'highlight-current-blue'), (b'grow', b'grow'), (b'shrink', b'shrink')])),
            ],
            options={
                'verbose_name': 'fragment',
                'verbose_name_plural': 'fragments',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SlideCode',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('code', models.TextField(default=b'', verbose_name='Code', blank=True)),
            ],
            options={
                'verbose_name': 'code',
                'verbose_name_plural': 'codes',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SlideModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('body', models.TextField(verbose_name='body')),
                ('title', models.CharField(default=b'', max_length=100, verbose_name='Title', blank=True)),
                ('sub_title', models.CharField(default=b'', max_length=100, verbose_name='Section title', blank=True)),
                ('transition', models.CharField(default=b'', max_length=20, verbose_name='Transition', blank=True, choices=[(b'none', b'None'), (b'cube', b'Cube'), (b'fade', b'Fade'), (b'default', b'Default'), (b'concave', b'Concave'), (b'page', b'Page'), (b'linea', b'Linear'), (b'zoom', b'Zoom')])),
                ('transition_speed', models.CharField(default=b'', max_length=20, verbose_name='Transition speed', blank=True, choices=[(b'default', b'Default'), (b'slow', b'Slow'), (b'fast', b'Fast')])),
                ('css_class', models.CharField(default=b'', max_length=100, verbose_name='Custom CSS class', blank=True)),
                ('background_css', models.CharField(default=b'', max_length=100, verbose_name='Background CSS class', blank=True)),
                ('background_transition_slide', models.BooleanField(default=False, verbose_name='Background transition')),
                ('background_image', filer.fields.image.FilerImageField(verbose_name='Background image', blank=True, to='filer.Image', null=True)),
            ],
            options={
                'verbose_name': 'slide',
                'verbose_name_plural': 'slides',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SlideNote',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('note', models.TextField(default=b'', verbose_name='Notes', blank=True)),
            ],
            options={
                'verbose_name': 'note',
                'verbose_name_plural': 'notes',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
