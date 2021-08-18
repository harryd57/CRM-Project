from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from . forms import AdminForm, AdminSignUpForm
from django.contrib import messages
from .models import AdminAccount

# Create your views here.


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    if request.user.is_authenticated:
        company = request.user.company_name
    else:
        company = "Not logged in"

    context = {"company": company}
    return render(request, "dashboard.html", context)


def admin_signup(request):
    user = AdminAccount.objects.values('is_admin_account')
    val = ''
    for item in user:
        val = item['is_admin_account']
    if val == True:
        return redirect('admin_login')
    else:
        if request.method == "POST":
            user_form = AdminSignUpForm(request.POST)
            admin_form = AdminForm(request.POST)

            if user_form.is_valid() and admin_form.is_valid():
                myuser = user_form.save()
                admin = admin_form.save(commit=False)
                admin.user = myuser

                admin.save()

                email = user_form.cleaned_data.get('email')
                password = user_form.cleaned_data.get('password1')
                myuser = authenticate(email=email, password=password)
                login(request, myuser)
                return redirect('dashboard')

        else:
            user_form = AdminSignUpForm()
            admin_form = AdminForm()

        context = {'user': user_form, 'admin': admin_form}

        return render(request, "signup.html", context)


def admin_login(request):
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
        return render(request, 'login.html')
