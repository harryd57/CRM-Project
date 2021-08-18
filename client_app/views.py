from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import ClientSignUpForm, ClientForm
from django.contrib import messages
from admin_app.models import AdminAccount

# Create your views here.


def client_signup(request):
    code = AdminAccount.objects.values('registration_code')
    for i in code:
        reg_code = i['registration_code']

    if request.method == "POST":
        user_form = ClientSignUpForm(request.POST)
        client_form = ClientForm(request.POST)
        reg = request.POST['reg_code']
        if user_form.is_valid() and client_form.is_valid():
            if reg == reg_code:
                myuser = user_form.save()
                client = client_form.save(commit=False)
                client.user = myuser

                client.save()

                email = user_form.cleaned_data.get('email')
                password = user_form.cleaned_data.get('password1')
                myuser = authenticate(email=email, password=password)
                login(request, myuser)
                return redirect('dashboard')
            else:
                messages.info(request, "Invalid Registration Code")
    else:
        user_form = ClientSignUpForm()
        client_form = ClientForm()

    context = {'user': user_form, 'client': client_form}
    return render(request, 'user_signup.html', context)


def client_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password1']

        myuser = authenticate(email=email, password=password)

        if myuser is not None:
            login(request, myuser)
            return redirect('dashboard')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('admin_login')
    else:
        return render(request, 'user_login.html')
