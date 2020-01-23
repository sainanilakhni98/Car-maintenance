from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from django.db import connection
from .forms import Showdata 
from cars.models import CompanyDetail
from .models import Carcomponent
import csv
# Create your views here.
def features(request):
    return render(request,'features/features.html')

def maintenance(request):

    # query = str(CompanyDetail.objects.all().query)
    # df = pd.read_sql_query(query, connection)
    # new_df = pd.DataFrame(df) 
    df= pd.read_csv("data.csv")
    df.drop(df.columns[0],axis=1,inplace=True)
    error = "Please select Range for price"
    data = "There is no car "
    if request.method == "POST":
        form = Showdata(request.POST)
        if form.is_valid():
            p1=form.cleaned_data['price1']
            p2=form.cleaned_data['price2']
            mcost=form.cleaned_data['mcost']
            mileage=form.cleaned_data['Mileage']
            engine=form.cleaned_data['engine']
            sc=form.cleaned_data['seat_capacity']
            print(p1)
            print(p2)
            # p1=list(map(int,p1))
            # p2=list(map(int,p2))
            sc=int(sc)
            #p=list(map(int,p.split('-')))
            m=list(map(int,mcost.split('-')))
            ml=list(map(int,mileage.split('-')))
            e=list(map(int,engine.split('-')))
            #sc=list(map(int,seat_capacity.split('-')))

            
            DataFrame=df[(df['price']>p1) & (df['price']<p2) & (df['Average_cost']>m[0]) & (df['Average_cost']<m[1]) & (df['Mileage']>ml[0]) & (df['Mileage']<ml[1])& (df['Engine']>e[0]) & (df['Engine']<e[1]) & (df['SC']==sc )]
            

            DataFrame.sort_values(by='ri',axis=0,inplace=True)
            if DataFrame.empty :
                return render(request,'features/table1.html',{'data':data})
            return render(request,'features/table2.html',{'DataFrame':DataFrame})
        else:
            return render(request,"features/features.html",{'error':error})
# def update(request):
#     if request.method == "POST":
#         form = Showdata(request.POST)
#         if form.is_valid():
#             mname=form.cleaned_data['mname']
#             mnumber=form.cleaned_data['mnumber']
#             mcost=form.cleaned_data['mcost']
#             new = CompanyDetail.objects.get(model="Maruti Suzuki Ertiga")
#             ne

#     return render(request,'features/update.html')

            


           

    # d={
    # 'price'  : form.cleaned_data['price'],
    # 'mcost' : form.cleaned_data['mcost'],
    # 'Engine' : form.cleaned_data['Engine'],
    # 'Mileage' : form.cleaned_data['Mileage'],
    # 'capacity' : form.cleaned_data['capacity']
    # }
    # query = str(CompanyDetail.objects.all().query)
    # df = pd.read_sql_query(query, connection)
    # new_df = pd.DataFrame(df)
    # new_df.loc[16,'mileage']=28
    # #print(new_df['model'])
    # #print(type(new_df))

    # return HttpResponse(new_df.to_html())

    #return render(request,'features/check.html',d)

# DataFrame=df[(df['price']>p1[0]) & (df['price']<p2[0]) & (df['Average_cost']>m[0]) & (df['Average_cost']<m[1]) & (df['Mileage']>ml[0]) & (df['Mileage']<ml[1]) & (df['Engine']>e[0]) & (df['Engine']<e[1]) & (df['SC']==sc[0] )]



def Carcomponents(request):
    with open('components.csv') as f:
        reader = csv.reader(f)
        print(reader)
        for row in reader:
            created = Carcomponent.objects.get_or_create(
            model = row[0],company = row[1],price = float(row[2]),
            airConditioning=int(row[3]),breakingSystem=int(row[4]),
            coolingSystem=int(row[5]),
            electrical=int(row[6]),
            engine=int(row[7]),
            fuelSystem=int(row[8]),
            gearBox =int(row[9]),
            steeringSystem=int(row[10]),
            transmission =int(row[11]),
            link=row[12]

            )
    return HttpResponse("success")



