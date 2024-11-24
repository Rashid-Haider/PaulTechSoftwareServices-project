from django.shortcuts import render
from employee.models import Employee

def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')

def gallerypage(request):
    return render(request, 'gallery.html')

def menupage(request):
    return render(request, 'menu.html')

def orderpage(request):
    return render(request, 'order.html')

def reviewpage(request):
    return render(request, 'review.html')

def registrationpage(request):
    try:
        if request.method=="POST":
            mname=request.POST.get('empname')
            memail=request.POST.get('empmail')
            mgender=request.POST.get('empgender')
            mage=request.POST.get('empage')

            emp=Employee(
                name=mname,
                email=memail,
                gender=mgender,
                age=mage
            )
            emp.save()
            
    except:
        pass
    return render(request,'registration.html')