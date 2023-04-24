from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class snippet(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='snippets')
    code = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)
    votes = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True) 
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code 
    

