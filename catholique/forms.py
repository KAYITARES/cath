from django import forms
from . models import Personel

class PersonelForm(forms.ModelForm):
    class Meta:
        model=Personel
        fields=['first_name','last_name','date_of_birth','father_date_birth','mother_date_birth',
         'id_number','photocopy_id_image','address_place','phone','email','phone_number_family','first_profession_place',
         'first_profession_date','perpetual_profession_place','perpetual_profession_date','deaconate_place',
         'deaconate_date','presbyterate_place','presbyterate_date','studies','attached_photocopy',
         'work_and_functions_place_date','work_out_society','date_patronal_feast','name_lunge']
        exclude=['none']



   
   
   
 
 