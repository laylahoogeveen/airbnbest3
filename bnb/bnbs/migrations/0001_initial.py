# Generated by Django 3.2.7 on 2021-10-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField(default=0, null=True)),
                ('name', models.CharField(max_length=128, null=True)),
                ('review', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('neighbourhood', models.CharField(max_length=40, null=True)),
                ('description', models.TextField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('property_long', models.CharField(max_length=36, null=True)),
                ('property', models.CharField(max_length=20, null=True)),
                ('room_type', models.CharField(choices=[('ENT', 'ENT'), ('PRR', 'PRR'), ('HTR', 'HTR'), ('SHR', 'SHR')], max_length=36, null=True)),
                ('accommodates', models.IntegerField(null=True)),
                ('bedrooms', models.IntegerField(null=True)),
                ('beds', models.IntegerField(null=True)),
                ('number_of_baths', models.DecimalField(decimal_places=1, max_digits=5, null=True)),
                ('bathroom_shared', models.BooleanField(default=True)),
                ('amenities', models.TextField(null=True)),
                ('price_eu', models.IntegerField(default=0, null=True)),
                ('price_us', models.IntegerField(default=0, null=True)),
                ('listing_url', models.URLField(max_length=80, null=True)),
                ('picture_url', models.URLField(null=True)),
            ],
        ),
    ]
