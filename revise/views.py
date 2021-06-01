# I have made this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
     #return render(request,'index.html')
     return HttpResponse('''<h1>Personal navigator</h1> <br> <a href="https://www.google.com/"> Ask me anything</a> <br>  <a href="https://www.facebook.com/"> Chat with frends</a><br> <a href="https://s.aktu.ictacademyiitk.ac.in/"> Best university award goes to</a>''')
def about(request):
    return HttpResponse("About the website huehuehue")
def bold(request):
    return HttpResponse('''<h4>bold</h4><br><a href="/">Go back</a>''')
def capitalize(request):
    return HttpResponse('''<h4>Capitalize</h4><br><a href="/">Go back</a>''')