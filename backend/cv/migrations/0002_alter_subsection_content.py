# Generated by Django 3.2.9 on 2021-11-27 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsection',
            name='content',
            field=models.ManyToManyField(blank=True, to='cv.Content'),
        ),
    ]
