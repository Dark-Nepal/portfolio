from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100,verbose_name='Name')
    email = models.EmailField()
    subject = models.CharField(max_length=100, verbose_name='Subject')
    message = models.TextField()


    def __str__(self):
        return self.name

    
