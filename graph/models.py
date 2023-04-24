from django.db import models

# Create your models here.
class graph(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name