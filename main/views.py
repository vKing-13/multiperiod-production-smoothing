from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from main import models,forms
from django.contrib.auth.models import Group
from datetime import date
from django.contrib.auth.decorators import login_required,user_passes_test
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth import logout,login,authenticate
# Create your views here.


def is_admin(user):
    return user.is_superuser
def is_boss(user):
    return user.groups.filter(name='BOSS').exists()
def is_worker(user):
    return user.groups.filter(name='WORKER').exists()
def is_upper(user):
  return user.groups.filter(name='BOSS').exists() or user.groups.filter(name='WORKER').exists()


def index(request):
  if request.user.is_authenticated:
    currUser=request.user
    if request.user.is_superuser:
        return redirect('admin_view_user')
    elif is_boss(request.user) :
      calculateFinalCost()
      calculateNumOfTempWorkers()
      recheckIC()
      IHCData = models.IHCDatabase.objects.all().values().order_by('month')
      FHCData = models.FHCDatabase.objects.all().values().order_by('month')
      FCData = models.FCDatabase.objects.all().values()
      RDData = models.RDDatabase.objects.all().values().order_by('month')
      NTWData = models.NTWDatabase.objects.all().values().order_by('month')
      ICData = models.ICDatabase.objects.all().values().order_by('month')
      return render(request,"main/index.html",  {'IHC':IHCData,
                                                'FHC':FHCData,
                                                'FC':FCData,
                                                'RD':RDData,
                                                'NTW':NTWData,
                                                'IC':ICData,
                                                'currUser':currUser})
    elif is_worker(request.user):
      calculateFinalCost()
      calculateNumOfTempWorkers()
      recheckIC()
      IHCData = models.IHCDatabase.objects.all().values().order_by('month')
      FHCData = models.FHCDatabase.objects.all().values().order_by('month')
      FCData = models.FCDatabase.objects.all().values()
      RDData = models.RDDatabase.objects.all().values().order_by('month')
      NTWData = models.NTWDatabase.objects.all().values().order_by('month')
      ICData = models.ICDatabase.objects.all().values().order_by('month')
      return render(request,"main/index.html",  {'IHC':IHCData,
                                                'FHC':FHCData,
                                                'FC':FCData,
                                                'RD':RDData,
                                                'NTW':NTWData,
                                                'IC':ICData})
  else:
    calculateFinalCost()
    calculateNumOfTempWorkers()
    recheckIC()
    IHCData = models.IHCDatabase.objects.all().values().order_by('month')
    FHCData = models.FHCDatabase.objects.all().values().order_by('month')
    FCData = models.FCDatabase.objects.all().values()
    RDData = models.RDDatabase.objects.all().values().order_by('month')
    NTWData = models.NTWDatabase.objects.all().values().order_by('month')
    ICData = models.ICDatabase.objects.all().values().order_by('month')
    return render(request,"main/index.html",  {'IHC':IHCData,
                                                'FHC':FHCData,
                                                'FC':FCData,
                                                'RD':RDData,
                                                'NTW':NTWData,
                                                'IC':ICData})


      
  


def logout_view(request):
  logout(request)
  return HttpResponseRedirect('/')



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
      return redirect('home')

    else:
      return HttpResponseRedirect('worker_login')

  return render(request,'main/worker_SignUp.html',{'form1':form1,'form2':form2})

def boss_signup_view(request): 
  form1=forms.BossUserForm()
  form2=forms.BossExtraForm()
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
      return redirect('home')
    return HttpResponseRedirect('boss_login')

  return render(request,'main/boss_SignUp.html',{'form1':form1,'form2':form2})


@login_required(login_url='admin-login')
@user_passes_test(is_admin)
def admin_view_user_view(request):
    user = get_user_model()
    worker=user.objects.filter(groups__name='WORKER') 
    boss=user.objects.filter(groups__name='BOSS') 
    
    return render(request,'main/admin_view_user.html',{'boss':boss,'worker':worker})

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_boss_view(request,pk):
    boss=models.BossExtra.objects.get(id=pk)
    user=models.User.objects.get(id=boss.user_id)
    user.delete()
    boss.delete()
    return redirect('admin_view_user')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def delete_worker_view(request,pk):
    worker=models.WorkerExtra.objects.get(id=pk)
    user=models.User.objects.get(id=worker.user_id)
    user.delete()
    worker.delete()
    return redirect('admin_view_user')










@login_required(login_url='/boss-login')
@user_passes_test(is_upper)
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

@login_required(login_url='/boss-login')
@user_passes_test(is_upper)
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
      current_month = date.today().month
      form = forms.FHCForm(initial={'month': current_month})
  return render(request,"main/calculate_firing_hiring_cost.html",{'form':form})

def calculateFinalCost():
  inputMonth = date.today().month
  qs = models.FCDatabase.objects.all().values()
  finalCostResult = 0
  if qs.count() <= 0:
    models.FCDatabase.objects.create(finalCost=0)
  for x in qs:
    finalCostGet = x['finalCost']
  for i in range(1, inputMonth+1):
    qsIHC = models.IHCDatabase.objects.filter(month=i).values()
    if qsIHC.exists():
      for x in qsIHC:
        inventoryHoldingCost = x['inventoryHoldingCost']
    else:
      inventoryHoldingCost = 0
    qsFHC = models.FHCDatabase.objects.filter(month=i).values()
    if qsFHC.exists():
      for x in qsFHC:
        hiringCost = x['hiringCost']
        firingCost = x['firingCost']
    else:
      hiringCost = 0
      firingCost = 0
    finalCostResult = finalCostResult + (inventoryHoldingCost + hiringCost + firingCost)
  models.FCDatabase.objects.filter(finalCost=finalCostGet).update(finalCost=finalCostResult)

@login_required(login_url='/boss-login')
@user_passes_test(is_upper)
def calculateInventoryConstraints(request):
  if request.method == "POST":
    form = forms.ICForm(request.POST)
    if form.is_valid():
      inputMonth = int(request.POST.get('month'))
      inputproductionTempWorker = float(request.POST.get('productionTempWorker'))
      qs = models.ICDatabase.objects.filter(month=inputMonth).values()
      if qs.count() > 0:
        models.ICDatabase.objects.filter(month=inputMonth).update(productionTempWorker=inputproductionTempWorker)
      else:
        form.save()
      for x in qs:
          productionTempWorker = x['productionTempWorker']
      qsIHC1 = models.IHCDatabase.objects.filter(month=inputMonth).values()
      if qsIHC1.exists():
        for x in qsIHC1:
          unitsOfEndingInventory = x['unitsOfEndingInventory']
      else:
        unitsOfEndingInventory = 0
      qsIHC2 = models.IHCDatabase.objects.filter(month=(inputMonth-1)).values()
      if qsIHC2.exists():
        for x in qsIHC2:
          unitsOfEndingInventoryLastMonth = x['unitsOfEndingInventory']
      else:
        unitsOfEndingInventoryLastMonth = 0
      qsNTW = models.NTWDatabase.objects.filter(month=inputMonth).values()
      if qsNTW.exists():
        for x in qsNTW:
          tempWorkerMonthly = x['tempWorkerMonthly']
      else:
        tempWorkerMonthly = 0
      qsRD = models.RDDatabase.objects.filter(month=inputMonth).values()
      if qsRD.exists():
        for x in qsRD:
          remainingDemand = x['remainingDemand']
      else:
        remainingDemand = 0
      monthlyInventoryConstraintsResult = remainingDemand + (unitsOfEndingInventory - unitsOfEndingInventoryLastMonth) - (productionTempWorker * tempWorkerMonthly)
      if monthlyInventoryConstraintsResult < 0:
        monthlyInventoryConstraintsResult = 0
      
      models.ICDatabase.objects.filter(month=inputMonth).update(monthlyInventoryConstraints=monthlyInventoryConstraintsResult)
      return HttpResponseRedirect('/')
  else:
      current_month = date.today().month
      form = forms.ICForm(initial={'month': current_month})
  return render(request,"main/calculate_inventory_constraints.html",{'form':form})

def calculateNumOfTempWorkers():
  inputMonth = date.today().month
  qs = models.NTWDatabase.objects.filter(month=inputMonth).values()
  tempWorkerMonthlyResult = 0
  tempWorkerMonthlyGet = 0
  if qs.count() <= 0:
    models.NTWDatabase.objects.create(month=inputMonth,tempWorkerMonthly = 0)
  for i in range(1, inputMonth+1):
    qsCheck = models.NTWDatabase.objects.filter(month=i).values()
    if qsCheck.exists() == False:
      models.NTWDatabase.objects.create(month=i,tempWorkerMonthly = 0)
    qsGet = models.NTWDatabase.objects.filter(month=i-1).values()
    if qsGet.exists():
      for x in qsGet:
        tempWorkerMonthlyGet = x['tempWorkerMonthly']
    else:
      tempWorkerMonthlyGet = 0
    qsFHC = models.FHCDatabase.objects.filter(month=i).values()
    if qsFHC.exists():
      for x in qsFHC:
        tempWorkerHired = x['tempWorkerHired']
        tempWorkerFired = x['tempWorkerFired']
    else:
      tempWorkerHired = 0
      tempWorkerFired = 0
    tempWorkerMonthlyResult = tempWorkerMonthlyGet + (tempWorkerHired - tempWorkerFired)
    models.NTWDatabase.objects.filter(month=i).update(tempWorkerMonthly=tempWorkerMonthlyResult)

@login_required(login_url='/boss-login')
@user_passes_test(is_upper)
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
      current_month = date.today().month
      form = forms.RDForm(initial={'month': current_month})
  return render(request,"main/calculate_remaining_demand.html",{'form':form})

def recheckIC():
  current_month = date.today().month
  for i in range(1, current_month+1):
    qs = models.ICDatabase.objects.filter(month=i).values()
    if qs.exists():
      for x in qs:
        productionTempWorkerGet = x['productionTempWorker']
    else:
      productionTempWorkerGet = 0
    qsIHC1 = models.IHCDatabase.objects.filter(month=i).values()
    if qsIHC1.exists():
      for x in qsIHC1:
        unitsOfEndingInventory = x['unitsOfEndingInventory']
    else:
      unitsOfEndingInventory = 0
    qsIHC2 = models.IHCDatabase.objects.filter(month=(i-1)).values()
    if qsIHC2.exists():
      for x in qsIHC2:
        unitsOfEndingInventoryLastMonth = x['unitsOfEndingInventory']
    else:
      unitsOfEndingInventoryLastMonth = 0
    qsNTW = models.NTWDatabase.objects.filter(month=i).values()
    if qsNTW.exists():
      for x in qsNTW:
        tempWorkerMonthly = x['tempWorkerMonthly']
    else:
      tempWorkerMonthly = 0
    qsRD = models.RDDatabase.objects.filter(month=i).values()
    if qsRD.exists():
      for x in qsRD:
        remainingDemand = x['remainingDemand']
    else:
      remainingDemand = 0
    monthlyInventoryConstraintsResult = remainingDemand + (unitsOfEndingInventory - unitsOfEndingInventoryLastMonth) - (productionTempWorkerGet * tempWorkerMonthly)
    if monthlyInventoryConstraintsResult < 0:
      monthlyInventoryConstraintsResult = 0
    if qs.exists():
      models.ICDatabase.objects.filter(month=i).update(monthlyInventoryConstraints=monthlyInventoryConstraintsResult)
    else:
      models.ICDatabase.objects.create(month=i,productionTempWorker=productionTempWorkerGet,monthlyInventoryConstraints=monthlyInventoryConstraintsResult)