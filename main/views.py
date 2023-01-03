from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from main import models, forms
from django.contrib.auth.models import Group
from datetime import date
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth import logout, login, authenticate
from pulp import *
# Create your views here.


def is_admin(user):
    return user.is_superuser


def is_boss(user):
    return user.groups.filter(name='BOSS').exists()


def is_upper(user):
    return user.groups.filter(name='BOSS').exists() or user.groups.filter(name='WORKER').exists()


def index(request):
    if request.method == "POST":
        inputPlanName = str(request.POST.get('planName'))
        inputDemand1 = int(request.POST.get('demand1'))
        inputDemand2 = int(request.POST.get('demand2'))
        inputDemand3 = int(request.POST.get('demand3'))
        inputDemand4 = int(request.POST.get('demand4'))
        inputNumPermanent = int(request.POST.get('numPermanent'))
        inputProdPermanent = int(request.POST.get('prodPermanent'))
        inputProdTemporary = int(request.POST.get('prodTemporary'))
        inputCostHiring = float(request.POST.get('costHiring'))
        inputCostFiring = float(request.POST.get('costFiring'))
        inputCostHoldingUnit = float(request.POST.get('costHoldingUnit'))
        inputInventoryInitial = int(request.POST.get('inventoryInitial'))
        inputInventoryFinal = int(request.POST.get('inventoryFinal'))
        queryCheck = models.PlanDatabase.objects.filter(planName=inputPlanName).exists()
        if queryCheck == True:
            inputPlanName = inputPlanName+'_copy'
        data = {'planName':inputPlanName, 
                'demand1':inputDemand1, 
                'demand2':inputDemand2, 
                'demand3':inputDemand3, 
                'demand4':inputDemand4, 
                'numPermanent':inputNumPermanent,
                'prodPermanent':inputProdPermanent,
                'prodTemporary':inputProdTemporary,
                'costHiring':inputCostHiring,
                'costFiring':inputCostFiring,
                'costHoldingUnit':inputCostHoldingUnit,
                'inventoryInitial':inputInventoryInitial, 
                'inventoryFinal': inputInventoryFinal 
                }
        form = forms.PlanningForm(data)
        form.save()
        model = LpProblem("Minimize Cost",LpMinimize)
        month= list(range(4))
        ihcDict = LpVariable.dicts('IHC',month,lowBound=0, cat='Continuous')
        ihcDict[3] = inputInventoryFinal
        hcDict = LpVariable.dicts('HC',month,lowBound=0, cat='Continuous')
        fcDict = LpVariable.dicts('FC',month,lowBound=0, cat='Continuous')
        model += lpSum([inputCostHoldingUnit * ihcDict[i] for i in month]) + lpSum([inputCostHiring * hcDict[i] for i in month]) + lpSum([inputCostFiring * fcDict[i] for i in month])
        model.addConstraint(inputInventoryInitial + inputProdTemporary*hcDict[0] - inputProdTemporary*fcDict[0] - ihcDict[0] == inputDemand1 - (inputNumPermanent * inputProdPermanent))
        model.addConstraint(ihcDict[0] + inputProdTemporary*hcDict[0] - inputProdTemporary*fcDict[0] + inputProdTemporary*hcDict[1] - inputProdTemporary*fcDict[1] - ihcDict[1] == inputDemand2 - (inputNumPermanent * inputProdPermanent))
        model.addConstraint(ihcDict[1] + inputProdTemporary*hcDict[0] - inputProdTemporary*fcDict[0] + inputProdTemporary*hcDict[1] - inputProdTemporary*fcDict[1] + inputProdTemporary*hcDict[2] - inputProdTemporary*fcDict[2] - ihcDict[2] == inputDemand3 - (inputNumPermanent * inputProdPermanent))
        model.addConstraint(ihcDict[2] + inputProdTemporary*hcDict[0] - inputProdTemporary*fcDict[0] + inputProdTemporary*hcDict[1] - inputProdTemporary*fcDict[1] + inputProdTemporary*hcDict[2] - inputProdTemporary*fcDict[2] + inputProdTemporary*hcDict[3] - inputProdTemporary*fcDict[3] - ihcDict[3] == inputDemand4 - (inputNumPermanent * inputProdPermanent))
        model.solve()
        models.PlanDatabase.objects.filter(planName=inputPlanName).update(inventoryMonth1 = ihcDict[0].varValue, inventoryMonth2 = ihcDict[1].varValue, inventoryMonth3 = ihcDict[2].varValue, hiredTemporary1 = hcDict[0].varValue, hiredTemporary2 = hcDict[1].varValue, hiredTemporary3 = hcDict[2].varValue, hiredTemporary4 = hcDict[3].varValue, firedTemporary1 = fcDict[0].varValue, firedTemporary2 = fcDict[1].varValue, firedTemporary3 = fcDict[2].varValue, firedTemporary4 = fcDict[3].varValue, optimalCost = value(model.objective))
        newInput = models.PlanDatabase.objects.filter(planName=inputPlanName).values()
        return render(request,"main/displayRow.html",  {'newInput':newInput})
    else:
        form = forms.PlanningForm()
    return render(request, 'main/index.html', {'form': form})


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
