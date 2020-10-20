from django import forms
from . models import Personel

class PersonelForm(forms.ModelForm):
    class Meta:
        model=Personel
        fields=['first_name','last_name','date_of_birth','father_date_birth','mother_date_birth','id_number','photocopy_id_image']
       