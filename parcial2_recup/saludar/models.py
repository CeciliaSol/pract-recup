from django.db import models

class Name(models.Model):
    first_name = models.CharField(max_length=30)

class Greet(models.Model):
    title = models.CharField(max_length=50)
    name_set = models.ForeignKey('Name', on_delete=models.SET_NULL, null=True)
    greet = models.CharField(max_length=30)
        
    def __str__(self):
        return self.title
