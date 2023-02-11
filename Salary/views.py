from django.shortcuts import render
from django.http import HttpResponse
import joblib
# Create your views here.

def homepage(request):
    return render(request,'form/form.html')

def salary(request):
    a1 = request.POST['a1']
    reg = joblib.load("model/salary.pkl")
    y_pred = reg.predict([[a1]])
    data = {"salary":y_pred}
    return render(request,'about/about.html',data)