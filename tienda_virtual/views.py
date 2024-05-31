from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from users.models import User
from products.models import Product
from django.http import HttpResponseRedirect

def index(request):

    products = Product.objects.all().order_by('-id')

    return render(request, 'index.html', {
        'message': '¡Bienvenido a la Store!',
        'products': products
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')

        user = authenticate(username=usuario, password=contraseña)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}!'.format(user.username))

            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])

            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña inválidos')
    return render(request, "users/login.html", {})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente!')
    return redirect('login')

def registro(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Te has registrado con exito!')
            return redirect('index')
    return render(request, 'users/registro.html', {'form': form})