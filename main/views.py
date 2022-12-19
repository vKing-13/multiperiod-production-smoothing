from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from main import models,forms
from django.contrib.auth.models import Group
from datetime import date
from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

# Create your views here.


def is_admin(user):
    return user.is_superuser
def is_boss(user):
    return user.groups.filter(name='BOSS').exists()
def is_worker(user):
    return user.groups.filter(name='WORKER').exists()


def index(request):
  # if request.user.is_authenticated:
  #       if request.user.is_superuser:
  #           # return redirect('admin_view_user')
  #           return render(request, 'main/index.html')
  #       elif is_boss(request.user) :
  #           return redirect('Calculate Final Cost')
  #       else:
  #         return redirect('Calculate Final Cost')
  # return render(request, 'main/index.html')
  qsIHC = models.IHCDatabase.objects.all().values()
  qsFHC = models.FHCDatabase.objects.all().values()
  qsFC = models.FCDatabase.objects.all().values()
  qsRD = models.RDDatabase.objects.all().values()
  return render(request,"main/index.html",  {'IHC':qsIHC,
                                            'FHC':qsFHC,
                                            'FC':qsFC,
                                            'RD':qsRD})


def worker_signup_view(request): 
  form1=forms.WorkerUserForm()
  form2=forms.WorkerExtraForm()
  if request.method == 'POST':
    form1=forms.WorkerUserForm(request.POST)
    form2=forms.WorkerExtraForm(request.POST)
    if form1.is_valid() and form2.is_valid():
      user=form1.save()
      user.set_password(request.POST.get('password'))
      user.save()
      f2=form2.save(commit=False)
      f2.user=user
      user2=f2.save()

      worker_group=Group.objects.get_or_create(name='WORKER')
      worker_group[0].user_set.add(user)
      # return redirect('main/index.html')
      return render(request,'main/index.html')

    else:
      return HttpResponseRedirect('worker_login')

  return render(request,'main/worker_SignUp.html',{'form1':form1,'form2':form2})

def boss_signup_view(request): 
  form1=forms.BossUserForm()
  form2=forms.BossExtraForm()
  dict={'form1':form1,'form2':form2}
  if request.method == 'POST':
    form1=forms.BossUserForm(request.POST)
    form2=forms.BossExtraForm(request.POST)
    if form1.is_valid() and form2.is_valid():
      user=form1.save()
      user.set_password(request.POST.get('password'))
      user.save()
      f2=form2.save(commit=False)
      f2.user=user
      user2=f2.save()

      boss_group=Group.objects.get_or_create(name='BOSS')
      boss_group[0].user_set.add(user)
      return redirect('main/index.html')
    return HttpResponseRedirect('boss_login')

  return render(request,'main/boss_SignUp.html',context=dict)


@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_view_user_view(request):
    worker=models.WorkerExtra.objects.all()
    # user = get_user_model()
    # worker=user.objects.all()
    return render(request,'main/admin_view_user.html',{'worker':worker})













def calculateInventoryHoldingCost(request):
  if request.method == "POST":
    form = forms.IHCForm(request.POST)
    if form.is_valid():
      inputMonth = int(request.POST.get('month'))
      inputHoldingCostPerUnit = float(request.POST.get('holdingCostPerUnit'))
      inputUnitsOfEndingInventory = float(request.POST.get('unitsOfEndingInventory'))
      qs = models.IHCDatabase.objects.filter(month=inputMonth).values()
      if qs.count() > 0:
        models.IHCDatabase.objects.filter(month=inputMonth).update(holdingCostPerUnit=inputHoldingCostPerUnit)
        models.IHCDatabase.objects.filter(month=inputMonth).update(unitsOfEndingInventory=inputUnitsOfEndingInventory)
      else:
        form.save()
      for x in qs:
          holdingCostPerUnit = x['holdingCostPerUnit']
          unitsOfEndingInventory = x['unitsOfEndingInventory']
      inventoryHoldingCostResult = holdingCostPerUnit * unitsOfEndingInventory
      models.IHCDatabase.objects.filter(month=inputMonth).update(inventoryHoldingCost=inventoryHoldingCostResult)
      return HttpResponseRedirect('/')
  else:
      current_month = date.today().month
      form = forms.IHCForm(initial={'month': current_month})
  return render(request, 'main/calculate_inventory_holding_cost.html', {'form': form})

def calculateFiringHiringCost(request):
  if request.method == "POST":
    form = forms.FHCForm(request.POST)
    if form.is_valid():
      inputMonth = int(request.POST.get('month'))
      inputTempWorkerHiringCost = float(request.POST.get('tempWorkerHiringCost'))
      inputTempWorkerFiringCost = float(request.POST.get('tempWorkerFiringCost'))
      inputTempWorkerHired = float(request.POST.get('tempWorkerHired'))
      inputTempWorkerFired = float(request.POST.get('tempWorkerFired'))
      qs = models.FHCDatabase.objects.filter(month=inputMonth).values()
      if qs.count() > 0:
        models.FHCDatabase.objects.filter(month=inputMonth).update(tempWorkerHiringCost=inputTempWorkerHiringCost)
        models.FHCDatabase.objects.filter(month=inputMonth).update(tempWorkerFiringCost=inputTempWorkerFiringCost)
        models.FHCDatabase.objects.filter(month=inputMonth).update(tempWorkerHired=inputTempWorkerHired)
        models.FHCDatabase.objects.filter(month=inputMonth).update(tempWorkerFired=inputTempWorkerFired)
      else:
        form.save()
      for x in qs:
          tempWorkerHiringCost = x['tempWorkerHiringCost']
          tempWorkerFiringCost = x['tempWorkerFiringCost']
          tempWorkerHired = x['tempWorkerHired']
          tempWorkerFired = x['tempWorkerFired']
      hiringCostResult = tempWorkerHiringCost * tempWorkerHired
      firingCostResult = tempWorkerFiringCost * tempWorkerFired
      models.FHCDatabase.objects.filter(month=inputMonth).update(hiringCost=hiringCostResult)
      models.FHCDatabase.objects.filter(month=inputMonth).update(firingCost=firingCostResult)
      return HttpResponseRedirect('/')
  else:
      form = forms.FHCForm()
  return render(request,"main/calculate_firing_hiring_cost.html",{'form':form})

def calculateFinalCost(request):
  # if request.method == "POST":
  #   form = forms.FCForm(request.POST)
  #   if form.is_valid():
  #     inputMonth = int(request.POST.get('addMonth'))
  #     qs = models.FCDatabase.objects.all().values()
  #     if qs.count() <= 0:
  #       form.save()
  #     for x in qs:
  #       finalCostGet = x['finalCost']
  #     qsIHC = models.IHCDatabase.objects.filter(month=inputMonth).values()
  #     for x in qsIHC:
  #       inventoryHoldingCost = x['inventoryHoldingCost']
  #     qsFHC = models.FHCDatabase.objects.filter(month=inputMonth).values()
  #     for x in qsFHC:
  #       hiringCost = x['hiringCost']
  #       firingCost = x['firingCost']
  #     finalCostResult = finalCostGet + inventoryHoldingCost + hiringCost + firingCost
  #     models.FCDatabase.objects.filter(finalCost=finalCostGet).update(finalCost=finalCostResult)
  #     return HttpResponseRedirect('/')
  # else:
  #     form = forms.FCForm()
  # return render(request,"main/calculate_final_cost.html",{'form':form})
  return HttpResponseRedirect('/')

def calculateInventoryConstraints(request):
  form = forms.ICForm(request.POST)
  return render(request,"main/calculate_inventory_constraints.html",{'form':form})

def calculateNumOfTempWorkers(request):
  form = forms.NTWForm(request.POST)
  return render(request,"main/calculate_num_of_temp_workers.html",{'form':form})

def calculateRemainingDemand(request):
  if request.method == "POST":
    form = forms.RDForm(request.POST)
    if form.is_valid():
      inputMonth = int(request.POST.get('month'))
      inputDemand = float(request.POST.get('demand'))
      inputProductionPermanentWorker = float(request.POST.get('productionPermanentWorker'))
      inputNumPermanentWorker = float(request.POST.get('numPermanentWorker'))
      qs = models.RDDatabase.objects.filter(month=inputMonth).values()
      if qs.count() > 0:
        models.RDDatabase.objects.filter(month=inputMonth).update(demand=inputDemand)
        models.RDDatabase.objects.filter(month=inputMonth).update(productionPermanentWorker=inputProductionPermanentWorker)
        models.RDDatabase.objects.filter(month=inputMonth).update(numPermanentWorker=inputNumPermanentWorker)
      else:
        form.save()
      for x in qs:
          demand = x['demand']
          productionPermanentWorker = x['productionPermanentWorker']
          numPermanentWorker = x['numPermanentWorker']
      remainingDemandResult = demand - (productionPermanentWorker * numPermanentWorker)
      if remainingDemandResult < 0:
        remainingDemandResult = 0
      models.RDDatabase.objects.filter(month=inputMonth).update(remainingDemand=remainingDemandResult)
      return HttpResponseRedirect('/')
  else:
      form = forms.RDForm()
  return render(request,"main/calculate_remaining_demand.html",{'form':form})

def resetFC(request):
  qs = models.FCDatabase.objects.all().values()
  for x in qs:
    finalCostGet = x['finalCost']
  models.FCDatabase.objects.filter(finalCost=finalCostGet).update(finalCost=0)
  return HttpResponseRedirect('/')