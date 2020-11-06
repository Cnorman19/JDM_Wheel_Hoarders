from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Sell(models.Model):

    diameter_choices = [
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
    ]

    width_choices = [
        ('7', '7'),
        ('7.5', '7.5'),
        ('8', '8'),
        ('8.5', '8.5'),
        ('9', '9'),
        ('9.5', '9.5'),
        ('10', '10'),
        ('10.5', '10.5'),
        ('11', '11'),
        ('11.5', '11.5'),
        ('12', '12'),
        ('12.5', '12.5'),
        ('13', '13'),
        ('13.5', '13.5'),
        ('14', '14'),
        ('14.5', '14.5'),
        ('15', '15')
    ]

    offset_choices = [

    (i,i) for i in range(-100 , 100)
    ]

    bolt_pattern_choices = [
        ('4x100', '4x100'),
        ('4x114.3', '4x114.3'),
        ('5x100', '5x100'),
        ('5x114.3', '5x114.3'),



    ]



    name = models.CharField(max_length=100)
    diameter = models.CharField(max_length = 2, choices = diameter_choices, default=00)
    width = models.CharField(max_length = 3, choices = width_choices, default=00)
    offset = models.CharField(max_length = 4)
    bolt_pattern = models.CharField(max_length = 8, choices = bolt_pattern_choices, default=00)
    description = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('sell-detail', kwargs={'pk' : self.pk} )