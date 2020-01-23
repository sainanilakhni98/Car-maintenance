from django.shortcuts import render
from django.http import HttpResponse
import csv
from .models import CompanyDetail
#from features.models import Carcomponent
def cars(request):
    return render(request,'cars/cars.html')


def filldata(request):
    with open('Cars-n.csv') as f:
        reader = csv.reader(f)
        print(reader)
        for row in reader:
            created = CompanyDetail.objects.get_or_create(
            model = row[0],company = row[1],price = float(row[2]),
            Engine = int(row[3]),seat_capacity = int(row[4]),mileage=float(row[5]),
            first_kms=int(row[6]),
            first_engine_oil=int(row[7]),
            first_oil_filter=float(row[8]),
            first_air_filter=int(row[9]),
            first_fuel_filter=int(row[10]),
            first_service_cost=float(row[11]),
            first_Brake_oil=int(row[12]),

            second_kms=int(row[13]),
            second_engine_oil=int(row[14]),
            second_oil_filter=float(row[15]),
            second_air_filter=int(row[16]),
            second_fuel_filter=int(row[17]),
            second_service_cost=float(row[18]),
            second_Brake_oil=int(row[19]),

            third_kms=int(row[20]),
            third_engine_oil=int(row[21]),
            third_oil_filter=float(row[22]),
            third_air_filter=int(row[23]),
            third_fuel_filter=int(row[24]),
            third_service_cost=float(row[25]),
            third_Brake_oil=int(row[26]),

            four_kms=int(row[27]),
            four_engine_oil=int(row[28]),
            four_oil_filter=float(row[29]),
            four_air_filter=int(row[30]),
            four_fuel_filter=int(row[31]),
            four_service_cost=float(row[32]),
            four_Brake_oil=float(row[33]),


            five_kms=int(row[34]),
            five_engine_oil=int(row[35]),
            five_oil_filter=float(row[36]),
            five_air_filter=int(row[37]),
            five_fuel_filter=int(row[38]),
            five_service_cost=float(row[39]),
            five_Brake_oil=int(row[40]),

            six_kms=int(row[41]),
            six_engine_oil=int(row[42]),
            six_oil_filter=float(row[43]),
            six_air_filter=float(row[44]),
            six_fuel_filter=float(row[45]),
            six_service_cost=float(row[46]),
            six_Brake_oil=float(row[47]),
            first_maintenance_cost =float(row[48]),second_maintenance_cost =float(row[49]),
            third_maintenance_cost =float(row[50]),four_maintenance_cost =float(row[51]),
            five_maintenance_cost =float(row[52]),six_maintenance_cost =float(row[53]),
            Average_maintenance_cost=int(row[54]),
            reliability_index=int(row[55]),
            link =row[56]
            )
    return HttpResponse("success")
def ViewDetails(request,name):
    prod = CompanyDetail.objects.filter(company=name)
    prod=list(prod)
    print(prod,"this is company name")
    params = {'allProds':prod}
    return render(request,'cars/ViewDetails.html',params)

def CarsDetails(request,name,model):

    #prod = CompanyDetail.objects.filter(company=name)
    model = CompanyDetail.objects.filter(model=model)
    #prob = Carcomponent.objects.filter(model=model)
    # prob = CompanyDetail.objects.filter(Carcomponents__model__in=CompanyDetail.Carcomponent.all())
    
    print(list(model),"This is model detail")
    #print(list(prob))
    # prod=list(prod)
    #print(prod,"this is company details")
    params = {'allProds':model}
    return render(request,'cars/CarDetails.html',params)
    
 
def search(request):
    query = request.GET['query']
     
    # if len(query)>78:
    #     allProds = CompanyDetail.objects.none()

    # allPostsCompany=CompanyDetail.objects.filter(company__icontains=query)
    # allPostsModel=CompanyDetail.objects.filter(model__icontains=query)
    # allProds= allPostsCompany.union(allPostsModel)

    allProdsCompany = CompanyDetail.objects.filter(company__icontains=query)
    allProdsModel = CompanyDetail.objects.filter(model__icontains=query)
    allProds = allProdsCompany.union(allProdsModel)
    # if allProds.count() == 0:
    #     messages.warning(request,"No search results found.Please refine your query")
    params = {'allProds':allProds,'query':query}
    #params = {'allProds':allProds}
    return render(request,'cars/search.html',params)
    
        
