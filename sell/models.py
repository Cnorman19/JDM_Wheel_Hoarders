from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Sell(models.Model):

	diameter_choices = [
    ('Ten', '10'),
    ('Eleven', '11'),
    ('Twelve', '12'),
    ('Thirteen', '13'),
    ('Fourteen', '14'),
    ('Fifteen', '15'),
    ('Sixteen', '16'),
    ('Seventeen', '17'),
    ('Eightteen', '18'),
    ('Nineteen', '19'),
    ('Twenty', '20'),
]

	width_choices = [
    ('Seven', '7'),
    ('Seven.5', '7.5'),
    ('Eight', '8'),
    ('Eight.5', '8.5'),
    ('Nine', '9'),
    ('Nine.5', '9.5'),
    ('Ten', '10'),
    ('Ten.5', '10.5'),
    ('Eleven', '11'),
    ('Eleven.5', '11.5'),
    ('Twelve', '12'),
    ('Twelve.5', '12.5'),
    ('Thirteen', '13'),
    ('Thirteen.5', '13.5'),
    ('Fourteen', '14'),
    ('Fourteen.5', '14.5'),
    ('Fifteen', '15')
]

	offset_choices = [

	(i,i) for i in range(-100 , 100)
]


	name = models.CharField(max_length=100)
	diameter = models.CharField(max_length = 2, choices = diameter_choices, default=00)
	width = models.CharField(max_length = 2, choices = width_choices, default=00)
	offset = models.CharField(max_length = 2, choices = offset_choices, default=00)
	description = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.name


	def get_absolute_url(self):
		return reverse('sell-detail', kwargs={'pk' : self.pk} )