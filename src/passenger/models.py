from django.db import models
from django import forms
from django.core.validators import MinLengthValidator
from django.urls import reverse

class Passenger(models.Model):
	username = models.CharField(max_length=80)
	password = models.CharField(max_length=15,validators=[MinLengthValidator(8)])
	email    = models.EmailField()
	phone_no = models.CharField(max_length=10) 

