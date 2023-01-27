from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Booking(models.Model):
    ID = models.AutoField(auto_created = True,primary_key=True)
    Name = models.CharField(max_length=255)
    No_Of_Guests = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(6)])
    BookingDate = models.DateTimeField()

class Menu(models.Model):
    ID = models.AutoField(auto_created = True,primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(decimal_places=2,max_digits=10)
    Inventory = models.IntegerField()