from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Profile,Student,Supervisor, Data , User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from music.forms import SignUpForm,SignSupForm


def index(request):
    all_students = Student.objects.all()
    context = {'all_students': all_students , }
    return render(request, 'music/index.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.Reg_no = form.cleaned_data.get('Reg_no')
            user.profile.specs = form.cleaned_data.get('specs')
            user.profile.mob = form.cleaned_data.get('mob')
            user.save()
            return redirect('music:index')
    else:
        form = SignUpForm()
    return render(request, 'music/signup.html',{'form': form})


def sv_signup_view(request):
    if request.method == 'POST':
        form = SignSupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.data.Uid = form.cleaned_data.get('Uid')
            user.data.spec = form.cleaned_data.get('spec')
            user.data.mobile = form.cleaned_data.get('mobile')
            user.save()
            return redirect('music:index')
    else:
        form = SignSupForm()
    return render(request, 'music/sv_signup.html',{'form': form})


def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('music:index')
    else:
        form = AuthenticationForm()
    return render(request, 'music/login.html', {'form':form})


def info(request):
    all_users = User.objects.all()
    context = {'all_users': all_users,}
    return render(request, 'music/allotment.html', context)


def update(request, user_id):
    loguser = request.user
    a = User.objects.get(id=loguser.id)
    b = User.objects.get(id=user_id)
    a.profile.sup_name = b.first_name + ' ' + b.last_name
    a.save()
    return render(request, 'music/dashboard.html')