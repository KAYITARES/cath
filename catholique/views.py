from django.shortcuts import render, redirect
from .forms import PersonelForm
#................
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
def formrender(request):
    current_user = request.user
    if request.method=='Post':
        form=PersonelForm(request.Post,request.Files)
        if form.is_valid():
            personel=form.save(commit=False)
            personel.user=current_user
            personel.save()
        return redirect("welcome")
    else:
        form=PersonelForm()
    return render(request,'formpage.html',{'form':form})