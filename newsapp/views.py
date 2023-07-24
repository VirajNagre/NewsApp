from django.shortcuts import render,redirect
from requests import *

# Create your views here.

def pnf(request,exception):
	return redirect("home")
	

def home(request):
	try:
		url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=40c4a4b85dd14ed8ad6e9982a2da5f78"
		res = get(url)
		data = res.json()
		info = data["articles"]
		msg = info
		return render(request,"home.html",{"msg":msg})

	except Exception as e:
		return render(request,"home.html",{"msg":str(e)})

def about(request):
	return render(request,"about.html")