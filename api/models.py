from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style =models.CharField(max_length=50)
    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    RED = 'R' 
    ORANGE = 'O'
    YELLOW = 'Y'
    GREEN = 'G'
    BLUE = 'B'
    INDIGO = 'I'
    VIOLET = 'V'
    BLACK = 'Bl'
    WHITE = 'W'

    ROYGBIV_CHOICES = [
        ('R','Red'),
        ('O','Orange'),
        ('Y','Yellow'),
        ('G','Green'),
        ('B','Blue'),
        ('I','Indigo'),
        ('V','Violet'),
        ('Bl','Black'),
        ('W','White'),
    ]

    color_name = models.CharField(max_length=2, choices=ROYGBIV_CHOICES, default=BLACK)

    def __str__(self):
        return self.color_name

class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)


    def __str__(self):
        return self.brand_name
