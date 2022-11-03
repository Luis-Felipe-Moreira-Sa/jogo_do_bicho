from operator import index
from xml.dom.minidom import Element
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import NewUserForm
import random
from ifpi.models import Result, Bets
from datetime import datetime, timedelta

#constantes
DICT_BICHO = {
        'Avestruz' : [1,2,3,4],     ## Jogo do Bicho by: 7e15 vol.1
        'Aguia' : [5,6,7,8],
        'Burro' : [9,10,11,12],
        'Borboleta' : [13,14,15,16],
        'Cachorro' : [17,18,19,20],
        'Cabra' : [21,22,23,24],
        'Carneiro' : [25,26,27,28],
        'Camelo' : [29,30,31,32],
        'Cobra' : [33,34,35,36],
        'Coelho' : [37,38,39,40],
        'Cavalo' : [41,42,43,44],
        'Elefante' : [45,46,47,48],
        'Galo' : [49,50,51,52],
        'Gato' : [53,54,55,56],
        'Jacare' : [57,58,59,60],
        'Leao' : [61,62,63,64],
        'Macaco' : [65,66,67,68],
        'Porco' : [69,70,71,72],
        'Pavao' : [73,74,75,76],
        'Peru' : [77,78,79,80],
        'Touro' : [81,82,83,84],
        'Tigre' : [85,86,87,88],
        'Urso' : [89,90,91,92],
        'Veado' : [93,94,95,96],
        'Vaca' : [97,98,99,0],
        ' ': [] 
}


# Create your views here.
def page_login(request):
    context = {
        'resultado': resultado,
        'bichos': bichos
    }
    return render(request, 'ifpi/login.html', context)


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="ifpi/register.html", context={"register_form":form})


def login_views(request):
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    context = {
        'user': user
    }
    if user is not None:
        return render(request, 'ifpi/perfil.html', context)
    else:
        return render(request, 'ifpi/login.html',{'resultado': resultado})


def logout_view(request):
    logout(request)
    return render(request, 'ifpi/login.html', {})


def jogo_do_bicho(request):
    # restritions = bet_restritions()
    restritions = True
    print(restritions)
    context = {
        'lista': range(0, 100),
        'restritions': restritions,
    }
    return render(request, 'ifpi/jogo_do_bicho.html', context)


def loteria(request):
    return render(request, 'ifpi/loteria.html', {})


def bet(request):
    var = request.POST['aposta']
    print(var)

    context = {
        'resultado': resultado
    }
    return render(request, 'ifpi/login.html', context)


def current_date_time():
    dt = datetime.now()
    print("dt: ", dt)
    add_4 = dt + timedelta(hours=1)
    print(add_4, " current_date_time")
    return add_4

#somando 4 horas no horário atual
def current_date():
    add_4 = current_date_time()
    return add_4.date()


def bet_restritions():
    saldo = 100 #pegar no banco, model User
    isBalance = (saldo - 5 >=0)
    now = current_date_time()
    print(now.hour, " HOUR")
    isRush = (2 <= now.hour <= 22)
    print(isRush, ' isRush')
    return isRush and isBalance


def result_restritions():
    isValidUpdate = current_date() > str_date()
    print("isValidUpdate ", isValidUpdate)
    return isValidUpdate


def str_date():
    a = Result.objects.all()[0]
    str_date = a.last_date()
    print(str_date, " banco")
    date = datetime.strptime(str_date, '%Y-%m-%d').date()
    return date


def last_result():
    all_results = Result.objects.all()
    print(all_results, len(all_results))
    list_numbers = random.sample(range(0,100), 5)
    result = ''
    datetoday = str(current_date())
    print(f'''{datetoday}''')
    for num in list_numbers:
        result += f'''{num} '''
    print(result)
    if len(all_results) != 0 and not result_restritions():
        for element in all_results:
            result = f'''{element}'''
            # resultado = element
    else:
        print("Entrou aki heim")
        Result.objects.all().delete()
        last_result = Result.objects.create(
            last_result = result,
            last_date_update = datetoday,
        )
        last_result.save()
    resultado = result.split(' ')
    del resultado[-1]
    print(resultado, "  Resultado ")
    return resultado


# login_views mais detalhada
def nome_bicho(dezena):
    keys_list = list(DICT_BICHO)
    for index in range(0, len(DICT_BICHO)):
        bicho = keys_list[index]
        if dezena in DICT_BICHO[bicho]:
            break
    return bicho


'''
def login_views(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'ifpi/perfil.html')
    else:
        return render(request, 'ifpi/login.html',{})
'''
resultado = last_result()
bichos = []
for dezena in resultado:
    bicho = nome_bicho(int(dezena))
    bichos.append(bicho)
print(bichos)
