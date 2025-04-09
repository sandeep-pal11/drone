from django.db import models

# Create your models here.

class ContactData(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.email
    

                                               

