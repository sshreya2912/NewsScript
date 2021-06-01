from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
import requests
# Create your views here.

def index(request):
    # prod1=Product()
    # prod1.image='by.jpeg'
    # prod1.name="Shakira"
    # prod1.desc="Baby yoda but we selling it as Shakira cuz why not mate?"
    # prod1.price=300
    # prod1.offer=0
    appi=requests.get("https://newsapi.org/v2/everything?q=tech&apiKey=884ad8f9a17a4e76925ed409fe630b69")
    news=appi.json()
    prods=Product.objects.all()
    return render(request,'shop/index.html',{'prods':prods})
def about(request):
    return render(request,'shop/about.html')
def home(request):
    genre=["technology","sports","science","wealth","entertainment","buisness"]
    url="https://newsapi.org/v2/top-headlines?country=in&category="+genre[1]+"&apiKey=884ad8f9a17a4e76925ed409fe630b69"
    appi=requests.get(url)
    news=appi.json()
   
    return render(request,'shop/index.html',{'news':news})
def buisness(request):
    url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=884ad8f9a17a4e76925ed409fe630b69"
    appi=requests.get(url)
    news=appi.json()
   
    return render(request,'shop/buisness.html',{'g':news})
def technology(request):
    url="https://newsapi.org/v2/top-headlines?country=in&category="+"technology"+"&apiKey=884ad8f9a17a4e76925ed409fe630b69"
    appi=requests.get(url)
    news=appi.json()
   
    return render(request,'shop/tech.html',{'g':news})
def sports(request):
    url="https://newsapi.org/v2/top-headlines?country=in&category="+"sports"+"&apiKey=884ad8f9a17a4e76925ed409fe630b69"
    appi=requests.get(url)
    news=appi.json()
   
    return render(request,'shop/sports.html',{'g':news})
def science(request):
    url="https://newsapi.org/v2/top-headlines?country=in&category="+"science"+"&apiKey=884ad8f9a17a4e76925ed409fe630b69"
    appi=requests.get(url)
    news=appi.json()
   
    return render(request,'shop/science.html',{'g':news})
def entertainment(request):
    url="https://newsapi.org/v2/top-headlines?country=in&category="+"entertainment"+"&apiKey=884ad8f9a17a4e76925ed409fe630b69"
    appi=requests.get(url)
    news=appi.json()
   
    return render(request,'shop/entertainment.html',{'g':news})
def health(request):
    url="https://newsapi.org/v2/top-headlines?country=in&category="+"health"+"&apiKey=884ad8f9a17a4e76925ed409fe630b69"
    appi=requests.get(url)
    news=appi.json()
   
    return render(request,'shop/health.html',{'g':news})



def contact(request):
    if request.method=="POST":
       name=request.POST.get('name','')
       email=request.POST.get('email','')
       place=request.POST.get('place','')
       subject=request.POST.get('subject','')
    #    print(place,subject,email,name)
       contact=Contact(name=name,email=email,place=place,subject=subject)
       contact.save()
    return render(request,'shop/contact.html')

    
def track(request):
    return HttpResponse("Track your product here")
