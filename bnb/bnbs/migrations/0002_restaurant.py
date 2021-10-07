# Generated by Django 3.2.7 on 2021-10-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnbs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('description', models.TextField(null=True)),
                ('name_en', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('url', models.URLField(null=True)),
                ('media', models.URLField(null=True)),
                ('thumbnail', models.URLField(null=True)),
            ],
        ),
    ]