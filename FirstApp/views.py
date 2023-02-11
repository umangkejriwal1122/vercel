from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
import joblib
# Create your views here.

def homepage(request):
    # return HttpResponse("<h2>This is my Home Page</h2>")
    return render(request,'home/home.html')

def about(request):
    # return HttpResponse("This is About Page")
   # a1 = request.GET.get('a1')
   # a2 = request.GET.get('a2')
   # a3 = request.GET.get('a3')
    a1 = request.POST['a1']
    a2 = request.POST['a2']
    a3 = request.POST['a3']
    # data = {"first":"Mr.","last":"Bean"}
    data = {"name":a1, "email":a2 , "mobile":a3}
    return render(request,'about/about.html',data)

def form(request):
    return render(request,'form/form.html')

def insert(request):
    name = request.POST['a1']
    email = request.POST['a2']
    mob = request.POST['a3']
    conn = sql.connect(host="localhost",user="root",passwd="",database="django")
    cursor = conn.cursor()
    query = "insert into users(name,email,mobile)values('{}','{}','{}')".format(name,email,mob)
    cursor.execute(query)
    conn.commit()
    return render(request,'form/form.html')

def login(request):
    email = request.POST['a2']
    mob = request.POST['a3']
    conn = sql.connect(host="localhost",user="root",passwd="",database="django")
    cursor = conn.cursor()
    query = "select * from users where email = '{}' and mobile = {}".format(email,mob)
    cursor.execute(query)
    d = cursor.fetchall()
    data = {"mydata":d}
    conn.commit()
    return render(request,'about/about.html',data)

def salary(request):
    # return HttpResponse("This is About Page")
   # a1 = request.GET.get('a1')
   # a2 = request.GET.get('a2')
   # a3 = request.GET.get('a3')
    a1 = request.POST['a1']
    a2 = request.POST['a2']
    a3 = request.POST['a3']
    # data = {"first":"Mr.","last":"Bean"}
    reg = joblib.load("model/salary.pkl")
    y_pred = reg.predict([[3.5]])
    data = {"name":y_pred, "email":a2 , "mobile":a3}
    return render(request,'about/about.html',data)