from django.db import models

# Create your models here.
class Cities(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    mobile = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)

    def __str__(self):
          return f'{self.firstname} has helpline number - {self.mobile} and dob is {self.birth_date}'