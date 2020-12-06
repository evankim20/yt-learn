from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm
# Create your views here.

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            print(f'Made user {email}')
            return redirect('/')
            #return render(request, 'accounts/info.html', context)
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'users/register.html', context)



def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        print('User authenticated')
        return redirect('/')

    # If user tries to login
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request,user)
                return redirect('/')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')