from django.db import models
# Create your models here.


class Task(models.Model):
      title = models.CharField(max_length=200)
      body = models.CharField(max_length=400)
      completed = models.BooleanField(default=False, blank=True, null=True)
      
      def __str__(self):

          return self.title


def upload_path(instance,filname):
    return '/'.join(['covers', str(instance.title), filname])

class Products(models.Model):
    title = models.CharField(max_length=32, blank=False)
    desc=models.CharField(max_length=32,blank=False)
    image = models.ImageField(blank=True, null=True, upload_to=upload_path)
    available=models.BooleanField(default=False,blank=True,null=True);



                                      