from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterUser, InfoUser, FutsalForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Account, UserInfo, FutsalInfo
# Create your views here.


def register(request):
    context = {}
    if request.method == 'GET':
        userform = RegisterUser()
        infoform = InfoUser()
        context['form'] = userform
        context['info'] = infoform
        return render(request, "pages/register1.html", context)
    else:
        userform = RegisterUser(request.POST)
        infoform = InfoUser(request.POST)
        if userform.is_valid() and infoform.is_valid():
            username = userform.cleaned_data.get('username')
            email = userform.cleaned_data.get('email')
            password = userform.cleaned_data.get('password')
            acc_type = 'User'
            user = Account.objects.create_user(username=username, password=password, email=email, acc_type=acc_type)

            first_name = infoform.cleaned_data.get('first_name')
            last_name = infoform.cleaned_data.get('last_name')
            phone = infoform.cleaned_data.get('phone')

            info = UserInfo()
            info.account_id = user
            info.first_name = first_name
            info.last_name = last_name
            info.phone = phone

            info.save()
            user.save()
            return redirect('/')
        else:
            context['form'] = userform
            context['info'] = infoform
            return render(request, "pages/register1.html", context)


def returnLogin(request):
    context = {}
    if request.method == 'GET':
        form = LoginForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()

        context['form'] = form
        return render(request, "pages/Login.html", context)
    else:
        username = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect("account/login")


def logoutUser(request):
    auth.logout(request)
    return redirect("home")


def registerFutsal(request):
    context = {}
    if request.method == 'POST':
        userform = RegisterUser(request.POST or None)
        infoform = FutsalForm(request.POST or None, request.FILES or None)
        if userform.is_valid() and infoform.is_valid():
            username = userform.cleaned_data.get('username')
            email = userform.cleaned_data.get('email')
            password = userform.cleaned_data.get('password')
            acc_type = 'Futsal'
            user = Account.objects.create_user(username=username, password=password, email=email, acc_type=acc_type)

            info = FutsalInfo()

            info.futsal_name = infoform.cleaned_data.get('futsal_name')
            info.phone = infoform.cleaned_data.get('phone')
            info.location = infoform.cleaned_data.get('location')
            info.open_at = infoform.cleaned_data.get('open_at')
            info.close_at = infoform.cleaned_data.get('close_at')
            info.price = infoform.cleaned_data.get('price')
            info.account_id = user

            if request.FILES:
                info.img1 = infoform.cleaned_data['img1']
                info.img2 = infoform.cleaned_data['img2']
                info.img3 = infoform.cleaned_data['img3']
                info.img4 = infoform.cleaned_data['img4']

            user.save()
            info.save()
            return redirect('/')
        else:
           context['form'] = userform
           context['info'] = infoform
           return render(request, "pages/register2.html", context)
    else:
        userform = RegisterUser(request.POST or None)
        infoform = FutsalForm(request.POST or None, request.FILES or None)
        context['form'] = userform
        context['info'] = infoform
        return render(request, "pages/register2.html", context)