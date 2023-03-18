from django.shortcuts import render, HttpResponseRedirect
from . forms import StudentRegistration
from .models import User

# Create your views here.

#This function will add New item and Show all item

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
          fm.save()
          fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()

    return render(request, 'enroll/Add&Show.html', {'form':fm, 'stu': stud})



#This function will Delete Item
def delete_data(request, id):
    if request.method == 'POST':
     pi = User.objects.get(pk=id)
     pi.delete()
     return HttpResponseRedirect('/')

