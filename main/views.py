from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from main import models, forms
from django.contrib.auth.models import Group
from datetime import date
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth import logout, login, authenticate
# Create your views here.


def is_admin(user):
    return user.is_superuser


def is_boss(user):
    return user.groups.filter(name='BOSS').exists()


def is_upper(user):
    return user.groups.filter(name='BOSS').exists() or user.groups.filter(name='WORKER').exists()


def index(request):
    return render(request, 'main/index.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def boss_signup_view(request):
    form1 = forms.BossUserForm()
    form2 = forms.BossExtraForm()
    if request.method == 'POST':
        form1 = forms.BossUserForm(request.POST)
        form2 = forms.BossExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(request.POST.get('password'))
            user.save()
            f2 = form2.save(commit=False)
            f2.user = user
            user2 = f2.save()

            boss_group = Group.objects.get_or_create(name='BOSS')
            boss_group[0].user_set.add(user)
            return redirect('home')
        return HttpResponseRedirect('boss_login')

    return render(request, 'main/boss_SignUp.html', {'form1': form1, 'form2': form2})


@login_required(login_url='admin-login')
@user_passes_test(is_admin)
def admin_view_user_view(request):
    user = get_user_model()
    worker = user.objects.filter(groups__name='WORKER')
    boss = user.objects.filter(groups__name='BOSS')

    return render(request, 'main/admin_view_user.html', {'boss': boss, 'worker': worker})


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_boss_view(request, pk):
    boss = models.BossExtra.objects.get(id=pk)
    user = models.User.objects.get(id=boss.user_id)
    user.delete()
    boss.delete()
    return redirect('admin_view_user')
