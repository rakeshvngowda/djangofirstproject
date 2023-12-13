from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .dbConnection.dbconnect import connect_to_mysql
import requests

dbConnectProperties = {
    "host": 'localhost',
    "user": "root",
    "password":"Rock*2677",
    "database": "sales"
}
# Create your views here.
def members(request):
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': connect_to_mysql(dbConnectProperties["host"],dbConnectProperties["database"],dbConnectProperties["user"],dbConnectProperties["password"],"SELECT * FROM members")
    }
    return HttpResponse(template.render(context,request))

def users(request):
    response = requests.get('https://reqres.in/api/users')
    data = response.json()
    print(data["data"])
    context = {
        'users': data['data']
    }
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render(context,request))


def details(request,id):
    mymember = connect_to_mysql(dbConnectProperties["host"],dbConnectProperties["database"],dbConnectProperties["user"],dbConnectProperties["password"],f"SELECT * FROM members WHERE id={id}")
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember[0]
    }
    return HttpResponse(template.render(context,request))

def userdetails(request,id):
    response = requests.get(f'https://reqres.in/api/users/{id}')
    data = response.json()
    template = loader.get_template('userdetail.html')
    context = {
        'user': data["data"]
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())