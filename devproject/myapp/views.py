from django.shortcuts import render
from django.shortcuts import render, redirect  
from myapp.forms import datasforms 
from myapp.models import datas  
# Create your views here.
def addnew(request):  
    if request.method == "POST":  
        form = datasforms(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = datasforms()  
    return render(request,'index.html',{'form':form})  
 
def index(request):  
    employees = datas.objects.all()  
    return render(request, "show.html", {'employees': employees}) 
 
def edit(request, id):  
    employee = datas.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
 
def update(request, id):  
    employee = datas.objects.get(id=id)  
    form = datasforms(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'employee': employee})  
     
def destroy(request, id):  
    employee = datas.objects.get(id=id)  
    employee.delete()  
    return redirect("/")

def about(request):  
    return render(request, "about.html") 