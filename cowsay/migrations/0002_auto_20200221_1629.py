# Generated by Django 3.0.3 on 2020-02-21 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowsay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='text',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
    ]