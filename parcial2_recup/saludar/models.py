from django.db import models

class Name(models.Model):
    first_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Greet(models.Model):
	
    title = models.CharField(max_length=50)
    name = models.ForeignKey('Name', on_delete=models.SET_NULL, null=True)
    greet = models.CharField(max_length=30)
        
    def __str__(self):
        return self.title

