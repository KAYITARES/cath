from django.shortcuts import render, redirect
from .forms import PersonelForm
from .models import Personel
#................
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
def formrender(request):
   if request.method == 'POST':
        form = PersonelForm(request.POST)
        if form.is_valid():
            firstName=form.cleaned_data['first_name']
            lastName=form.cleaned_data['last_name']
            dateOfBirth=form.cleaned_data['date_of_birth']
            fatherDateBirth=form.cleaned_data['father_date_birth']
            motherDateBirth=form.cleaned_data['mother_date_birth']
            idNumber=form.cleaned_data['id_number']
            photocopyIdImage=form.cleaned_data['photocopy_id_image']
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
            work_out_society=form.cleaned_data[' work_out_society']
            date_patronal_feast=form.cleaned_data['date_patronal_feast']
            name_lunge=form.cleaned_data['name_lunge']
            none=form.cleaned_data[' none']
            

            per=Personel(first_name=firstName,last_name=lastName,date_of_birth=dateOfBirth,father_date_birth=fatherDateBirth,mother_date_birth=motherDateBirth,id_number=idNumber,photocopy_id_image=photocopyIdImage,address_place=address_place,
            phone=phone,email=email,phone_number_family=phone_number_family,first_profession_place=first_profession_place,
            first_profession_date=first_profession_date,perpetual_profession_place=perpetual_profession_place,perpetual_profession_date=perpetual_profession_date,
            deaconate_place=deaconate_place,deaconate_date=deaconate_date,presbyterate_place=presbyterate_place,presbyterate_date=presbyterate_date,
            studies=studies,attached_photocopy=attached_photocopy,work_and_functions_place_date=work_and_functions_place_date, work_out_society= work_out_society,
            date_patronal_feast=date_patronal_feast,name_lunge=name_lunge, none= none)

            per.save()
            return redirect('all')

   else:
       form = PersonelForm()
   return render(request, 'formpage.html', {"personForm":form})

def all(request):
    names=Personel.objects.all() 
    return render(request, 'all.html',{"names":names})