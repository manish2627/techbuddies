from django.db import models

# Create your models here.
class Contact(models.Model):
    srno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=12)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self) :
        return  'A Message from  : ' + self.name + '-' +self.email