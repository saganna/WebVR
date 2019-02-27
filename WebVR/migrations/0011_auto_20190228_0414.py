# Generated by Django 2.1.7 on 2019-02-28 04:14

import colorful.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebVR', '0010_auto_20190228_0322'),
    ]

    operations = [
        migrations.CreateModel(
            name='a_cone',
            fields=[
                ('scale_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.scale')),
                ('position_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.position')),
                ('rotation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.rotation')),
                ('shadow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebVR.shadow')),
                ('name', models.CharField(max_length=50)),
                ('color', colorful.fields.RGBColorField(default=['#FF0000', '#00FF00', '#0000FF'])),
                ('src', models.TextField(default='')),
                ('visible', models.BooleanField(default=False)),
                ('radius_bottom', models.FloatField(default=1)),
                ('radius_top', models.FloatField(default=0.8)),
                ('theta_length', models.FloatField(default=360)),
                ('theta_start', models.FloatField(default=0)),
                ('width', models.FloatField(default=512)),
                ('height', models.FloatField(default=256)),
            ],
            options={
                'abstract': False,
            },
            bases=('WebVR.shadow', 'WebVR.rotation', 'WebVR.position', 'WebVR.scale'),
        ),
        migrations.CreateModel(
            name='a_cylinder',
            fields=[
                ('scale_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.scale')),
                ('position_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.position')),
                ('rotation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.rotation')),
                ('shadow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebVR.shadow')),
                ('name', models.CharField(max_length=50)),
                ('color', colorful.fields.RGBColorField(default=['#FF0000', '#00FF00', '#0000FF'])),
                ('src', models.TextField(default='')),
                ('visible', models.BooleanField(default=False)),
                ('radius_bottom', models.FloatField(default=1)),
                ('radius_top', models.FloatField(default=0.8)),
                ('theta_length', models.FloatField(default=360)),
                ('theta_start', models.FloatField(default=0)),
                ('width', models.FloatField(default=512)),
                ('height', models.FloatField(default=256)),
                ('open_ended', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('WebVR.shadow', 'WebVR.rotation', 'WebVR.position', 'WebVR.scale'),
        ),
        migrations.CreateModel(
            name='a_dodecahedron',
            fields=[
                ('scale_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.scale')),
                ('position_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.position')),
                ('rotation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='WebVR.rotation')),
                ('shadow_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WebVR.shadow')),
                ('name', models.CharField(max_length=50)),
                ('color', colorful.fields.RGBColorField(default=['#FF0000', '#00FF00', '#0000FF'])),
                ('src', models.TextField(default='')),
                ('visible', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('WebVR.shadow', 'WebVR.rotation', 'WebVR.position', 'WebVR.scale'),
        ),
        migrations.RenameModel(
            old_name='abox',
            new_name='a_box',
        ),
        migrations.RenameModel(
            old_name='acircle',
            new_name='a_circle',
        ),
    ]
