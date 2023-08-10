from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.category import Category

def quiz (request):
    if request.method != 'POST':
        return render (request, 'quiz.html')

    postData = request.POST
    skin = postData.get('skin')
    concern = postData.get('concern')
    ss=postData.get('ss')

    if skin == "dry" or concern=="dryness":
        request.session['problem']='pdryness'
    elif skin=="oily"or concern=="acne":
        request.session['problem']='oilcontrol'
    else:
        request.session['problem'] = 'general'
    
    print('quiz inputs:   ',skin)
    return redirect ('result')
        

