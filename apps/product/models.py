from django.db import models

# Create your models here.
SHAPE_CHOICES = (
        ('oval','oval'),
        ('egg','egg'),
        ('star','star')
    )

class Eyeglass(models.Model):
    title = models.CharField(max_length=50)
    tint = models.BooleanField(default=False)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

class Sunglass(models.Model):
    title = models.CharField(max_length=50)
    shape = models.CharField(max_length=50, choices=SHAPE_CHOICES)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.title


