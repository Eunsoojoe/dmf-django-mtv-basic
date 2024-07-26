from django.shortcuts import render
from faker import Faker
import random

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def lunch(request):
    menu = ['라면🍜','피자🍕','햄버거🍔','김밥🍙','초밥🍣']
    pick = random.choice(menu)
    context = {
        'pick':pick
    }
    return render(request,'lunch.html',context)

def lotto(request):
    number = random.sample(range(1,46),6)
    context = {
        'number':number
    }
    return render(request,'lotto.html',context)

def cube(request,number):
    result = int(number ** 3)
    context = {
        'result':result
    }
    return render(request,'cube.html',context)

def post(request):
    fake = Faker()
    fake_posts = []

    for post in range(100):
        fake_posts.append(fake.text())

    context={
        'fake_posts':fake_posts
    }

    return render(request,'post.html',context)