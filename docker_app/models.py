from django.db import models

class Museum(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    website = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    description = models.TextField()
    

    def __str__(self):
        return self.name