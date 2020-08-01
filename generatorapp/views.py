from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .passwordgenerationlogic import generator

# Create your views here.

def home(request):
    return render(request, 'html/home.html') 

def password(request):
    print('yadayada',request.GET.get('includeSpecials'))
    passlength = request.GET.get('Characterlength')
    isSpcl = request.GET.get('includeSpecials')
    isCap = request.GET.get('includeuppercase')
    isNum = request.GET.get('includeNumeric')

    if(isSpcl == 'on'):
        isSpclFlag = True
    else:
        isSpclFlag = False

    if(isCap == 'on'):
        isCapFlag = True
    else:
        isCapFlag = False


    if(isNum == 'on'):
        isNumFlag = True
    else:
        isNumFlag = False
        

    randPass = generator(isSpclFlag,isCapFlag,isNumFlag,passlength)
    result = randPass.generatePassword()
    print(f'The Final password is {result}')

    return render(request, 'html/password.html', {'key': result})    