from django.db import models
from datetime import datetime, date

class Personel(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    date_of_birth=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    father_date_birth=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    mother_date_birth=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    id_number=models.CharField(max_length=16)
    photocopy_id_image= models.ImageField(upload_to = 'id/')
    def __str__(self):
        return self.first_name

    def save_image(self):
        self.save()
    class Meta:
        ordering = ['first_name']
   