from django.shortcuts import *
from django.views import View
from .models import *
from django.contrib import messages


# Create your views here.

class index(View):
    def get(self, request):
        return render(request, 'index.html')


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = Customer.objects.filter(email=email, password=password)
        if len(user) == 0:
            messages.warning(request, 'Invalid Email and Password')
            return redirect('login')
        else:
            request.session['customer'] = {
                'email': email,
                'name': user[0].name,
                'mobile': user[0].mobile
            }
            return redirect('index')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        age = request.POST['age']
        mobile = request.POST['mobile']
        user = Customer(email=email, name=name, password=password, age=age, mobile=mobile)
        user.save()
        messages.success(request, 'Registeration Successfull, Pleasse Login Now')
        return redirect('register')


def logout(request):
    request.session['customer'] = ''
    del request.session['customer']
    return redirect('login')