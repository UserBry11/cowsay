from django.db import models
from django.utils import timezone

class Author(models.Model):
    choices = [
        ('beavis.zen', 'beavis.zen'),
        ('blowfish', 'blowfish'),
        ('bong', 'bong'),
        ('bud-frogs', 'bud-frogs'),
        ('bunny', 'bunny'),
        ('cheese', 'cheese'),
        ('cower', 'cower'),
        ('daemon', 'daemon'),
        ('default', 'default'),
        ('dragon-and-cow', 'dragon-and-cow'),
        ('dragon', 'dragon'),
        ('elephant-in-snake', 'elephant-in-snake'),
        ('elephant', 'elephant'),
        ('eyes', 'eyes'),
        ('flaming-sheep', 'flaming-sheep'),
        ('ghostbusters', 'ghostbusters'),
        ('kitty', 'kitty'),
        ('meow', 'meow'),
        ('milk', 'milk'),
        ('moofasa', 'moofasa'),
        ('mutilated', 'mutilated'),
        ('satanic', 'satanic'),
        ('sodomized', 'sodomized'),
        ('surgery', 'surgery'),
        ('stegosaurus', 'stegosaurus'),
        ('stimpy', 'stimpy'),
        ('turkey', 'turkey'),
        ('turtle', 'turtle'),
        ('tux', 'tux'),
        ('www', 'www')
    ]

    text = models.CharField(max_length=50, blank=True)
    choice = models.CharField(max_length=17,
                              choices=choices)


class History(models.Model):
    text = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.text
