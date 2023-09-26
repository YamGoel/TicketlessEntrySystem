from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password , check_password
from .models import Users,Unique
# Create your views here.

# def index(request):
#     return HttpResponse("Hello")
uname=''
email=''
ids=[]
def index(request):
    return render(request,'ticket\index.html')


def loginpage(request):
    if request.method == 'POST':
        uemail = request.POST.get('email')
        password = request.POST.get('password')
        if Users.objects.filter(email=uemail).exists():
            obj = Users.objects.get(email=uemail)
            flag = check_password(password,obj.password)
            if flag:
                global uname
                uname = obj.name
                global email
                email = obj.email
                request.session['email'] = uemail
                request.session.set_expiry(0)
                return redirect("home")
            else:
                messages.info(request,'Wrong credentials')
                return redirect('loginpage')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('loginpage')
    else:
        return render(request,'ticket\login.html')

def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        uemail = request.POST.get('email')
        password = request.POST.get('password')
        confpassword = request.POST.get('confirm-password')
        if len(password)<8:
            messages.info(request,'Password must of minimum 8 Characters.')
            return redirect('signuppage')
        else:
            if password==confpassword:
                if Users.objects.filter(email=uemail).exists():
                    messages.info(request,'Email already in use.')
                    return redirect('signuppage')
                else:
                    password = make_password(password)
                    user = Users(name=uname,email=uemail,password=password,)
                    user.save();
                    return redirect('signuppage')
            else:
                messages.info(request,'Password and Confirm Password not Matching')
                return redirect('signuppage')
        return redirect('/')
    else:
        return render(request,'ticket\signup.html')

def home(request):
    if request.session.has_key('email'):
        if Users.objects.filter(email=email).exists():
            show = Users.objects.get(email=email)
            # n=show.name;
            d = {'name':uname}
            return render(request,"ticket\home.html",d)
    else:
        messages.info(request,'Login first/again')
        return redirect('loginpage')
    # return render(request,'ticket\home.html')

import random
import string

def generate_unique_id(length=6):
    characters = string.ascii_letters + string.digits  # includes all letters (uppercase and lowercase) and digits
    unique_id = ''.join(random.choice(characters) for _ in range(length))
    return unique_id
def visitor(request):
    d={}
    if request.method == 'POST':
        museum = request.POST.get('museum')
        date = request.POST.get('visit-date')
        phone= request.POST.get('phone')
        aadhar= request.POST.get('aadhar')
        nationality= request.POST.get('nationality')
        city= request.POST.get('city')
        state= request.POST.get('state')
        vis1= request.POST.get('num-adults-1')
        vis2= request.POST.get('num-adults-2')
        vis3= request.POST.get('num-adults-3')
        vis4= request.POST.get('num-adults-4')
        vis5= request.POST.get('num-adults-5')
        d = {'museum':museum,'date':date,'phone':phone,'aadhar':aadhar,'nationality':nationality,
            'city':city,'state':state,'vis1':vis1, 'vis2':vis2,'vis3':vis3,'vis4':vis4,'vis5':vis5}
        vis=[]
        for i in range(1,6):
            vis=generate_unique_id()
            name='vis'+str(i)+"id"
            d[name]=vis
            # ids.append(vis)
            idss = Unique(uid=vis)
            idss.save();

        # return render(request,"ticket\visit.html",d)
    # else:
    #     return redirect('home')
    try :
        return render(request,"ticket/visit.html",d)
    except OSError as error :
        print(error)
    # return render(request,"ticket\visit.html",d)
def verify(request):
    cnfrm={}
    if request.method=='POST':
        id = request.POST.get('uid')
        if Unique.objects.filter(uid=id).exists():
            cnfrm['status']= "Valid ID, Access Given!"
        else:
            cnfrm['status']= "InValid ID, Access Denied!"
    return render(request,'ticket/verify.html',cnfrm)