# Generated by Django 3.0.3 on 2020-02-20 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cowsay', '0005_author_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='choice',
            field=models.CharField(choices=[('beavis', 'beavis'), ('cheese', 'cheese'), ('cow', 'cow'), ('daemon', 'daemon'), ('dragon', 'dragon'), ('ghostbusters', 'ghostbusters'), ('kitty', 'kitty'), ('meow', 'meow'), ('milk', 'milk'), ('stegosaurus', 'stegosaurus'), ('stimpy', 'stimpy'), ('turkey', 'turkey'), ('turtle', 'turtle'), ('tux', 'tux')], max_length=13),
        ),
    ]