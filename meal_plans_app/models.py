from django.db import models

# Create your models here.

class Day(models.Model):
    text = models.CharField(max_length = 10)
    date_added = models.DateTimeField(auto_now_add = True)
    def  __str__(self):
        return self.text
    
class Entry(models.Model):
    day = models.ForeignKey(Day, on_delete= models.CASCADE)
    text = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'entries'

    def __str__(self):
        return f'{self.text[:50]}...'