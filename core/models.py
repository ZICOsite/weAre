from django.db import models
class ContactUs(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=13)
    text_message=models.CharField(max_length=500)