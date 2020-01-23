from django import forms

class Showdata(forms.Form):
    price1 = forms.IntegerField()
    price2= forms.IntegerField()
    mcost = forms.CharField()
    Mileage = forms.CharField()
    engine= forms.CharField()
    seat_capacity = forms.IntegerField()

# class update_data(forms.Form):
#     mname = forms.CharField()
#     mnumber = forms.IntegerField()
#     mcost = forms.IntegerField()
#<div class="jumbotron text-center"> <h1>{{data}}</h1></div>