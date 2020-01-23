from django.shortcuts import render

from django.http import HttpResponse
from features.models import Carcomponent

def index(request):
    return render(request,'index.html')

def health(request):
    return render(request,'health/health.html')

def HealthDetails(request,name):
    prod = Carcomponent.objects.filter(company=name)
    prod=list(prod)
    print(prod,"this is company name")
    params = {'allProds':prod}
    return render(request,'health/HealthDetails.html',params)

def FinalHealth(request,name,model):


    model = Carcomponent.objects.filter(model=model)
    params = {'allProds':model}
    return render(request,'health/FinalHealth.html',params)
    
def about(request):
    return render(request,'about.html')
