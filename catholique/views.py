from django.shortcuts import render, redirect
from .forms import PersonelForm
from .models import Personel
#................
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')



def formrender(request):
   if request.method == 'POST':
        form = PersonelForm(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            date_of_birth=form.cleaned_data['date_of_birth']
            father_date_birth=form.cleaned_data['father_date_birth']
            mother_date_birth=form.cleaned_data['mother_date_birth']
            id_number=form.cleaned_data['id_number']
            photocopy_id_image=form.cleaned_data['photocopy_id_image']
            address_place=form.cleaned_data['address_place']
            phone=form.cleaned_data['phone']
            email=form.cleaned_data['email']
            phone_number_family=form.cleaned_data['phone_number_family']
            first_profession_place=form.cleaned_data['first_profession_place']
            first_profession_date=form.cleaned_data['first_profession_date']
            perpetual_profession_place=form.cleaned_data['perpetual_profession_place']
            perpetual_profession_date=form.cleaned_data['perpetual_profession_date']
            deaconate_place=form.cleaned_data['deaconate_place']
            deaconate_date=form.cleaned_data['deaconate_date']
            presbyterate_place=form.cleaned_data['presbyterate_place']
            presbyterate_date=form.cleaned_data['presbyterate_date']
            studies=form.cleaned_data['studies']
            attached_photocopy=form.cleaned_data['attached_photocopy']
            work_and_functions_place_date=form.cleaned_data['work_and_functions_place_date']
            work_out_society=form.cleaned_data['work_out_society']
            date_patronal_feast=form.cleaned_data['date_patronal_feast']
            name_lunge=form.cleaned_data['name_lunge']
           
            per=Personel(first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            father_date_birth=father_date_birth,
            mother_date_birth=mother_date_birth,
            id_number=id_number,
            photocopy_id_image=photocopy_id_image,
            address_place=address_place,
            phone=phone,
            email=email,
            phone_number_family=phone_number_family,
            first_profession_place=first_profession_place,
            first_profession_date=first_profession_date,
            perpetual_profession_place=perpetual_profession_place,
            perpetual_profession_date=perpetual_profession_date,
            deaconate_place=deaconate_place,
            deaconate_date=deaconate_date,
            presbyterate_place=presbyterate_place,
            presbyterate_date=presbyterate_date,
            studies=studies,
            attached_photocopy=attached_photocopy,
            work_and_functions_place_date=work_and_functions_place_date,
            work_out_society=work_out_society,
            date_patronal_feast=date_patronal_feast,
            name_lunge=name_lunge)
           
            per.save()
        return redirect('all')

   else:
       form = PersonelForm()
   return render(request, 'formpage.html', {"personForm":form})

def all(request):
    names=Personel.objects.all() 
    return render(request, 'all.html',{"names":names})