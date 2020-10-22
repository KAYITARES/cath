from django.db import models
from datetime import datetime, date

class Personel(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=20)
    date_of_birth=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    father_date_birth=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    mother_date_birth=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    id_number=models.CharField(max_length=16)
    photocopy_id_image= models.ImageField(upload_to = 'id/')
    address_place=models.CharField(max_length=10)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    phone_number_family=models.CharField(max_length=10)
    first_profession_place=models.CharField(max_length=30)
    first_profession_date=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    perpetual_profession_place=models.CharField(max_length=30)
    perpetual_profession_date=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    deaconate_place=models.CharField(max_length=30)
    deaconate_date=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    presbyterate_place=models.CharField(max_length=30)
    presbyterate_date=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    studies=models.CharField(max_length=40)
    attached_photocopy=models.ImageField(upload_to = 'id/')
    work_and_functions_place_date=models.TextField()
    work_out_society=models.TextField()
    date_patronal_feast=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    name_lunge=models.CharField(max_length=30)
    none=models.CharField(max_length=20)


   
    def __str__(self):
        return self.first_name

    def save_image(self):
        self.save()
    class Meta:
        ordering = ['first_name']
    @classmethod
    def get_all_names(cls):
        names= Personel.objects.all()
        return names