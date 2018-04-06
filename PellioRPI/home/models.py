from django.db import models
from django.db import models
from django import forms

HAPPINESS = (
	('1', 'Not at all'),
	('2', 'A Little'),
	('3', 'Moderately'),
	('4', 'Quite a Bit'),
	('5', 'Strongly'),
)


class gad7(models.Model):
	first = models.CharField(choices=HAPPINESS, max_length=1)
	second = models.CharField(choices=HAPPINESS, max_length=1)
	third = models.CharField(choices=HAPPINESS, max_length=1)
	fourth = models.CharField(choices=HAPPINESS, max_length=1)
	fifth = models.CharField(choices=HAPPINESS, max_length=1)
	sixth = models.CharField(choices=HAPPINESS, max_length=1)
	seventh = models.CharField(choices=HAPPINESS, max_length=1)
    	
	