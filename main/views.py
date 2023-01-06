from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from main import models, forms
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
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
        if request.user.is_authenticated:
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
            queryCheck = queryCheck = models.PlanDatabase.objects.filter(planName=inputPlanName).exists()
            while queryCheck == True:
                inputPlanName = inputPlanName+'_copy'
                queryCheck = models.PlanDatabase.objects.filter(planName=inputPlanName).exists()
            data = {'planName': inputPlanName,
                    'demand1': inputDemand1,
                    'demand2': inputDemand2,
                    'demand3': inputDemand3,
                    'demand4': inputDemand4,
                    'numPermanent': inputNumPermanent,
                    'prodPermanent': inputProdPermanent,
                    'prodTemporary': inputProdTemporary,
                    'costHiring': inputCostHiring,
                    'costFiring': inputCostFiring,
                    'costHoldingUnit': inputCostHoldingUnit,
                    'inventoryInitial': inputInventoryInitial,
                    'inventoryFinal': inputInventoryFinal
                    }
            form = forms.PlanningForm(data)
            form.save()
            model = LpProblem("Minimize Cost", LpMinimize)
            month = list(range(4))
            ihcDict = LpVariable.dicts(
                'IHC', month, lowBound=0, cat='Continuous')
            ihcDict[3] = inputInventoryFinal
            hcDict = LpVariable.dicts(
                'HC', month, lowBound=0, cat='Continuous')
            fcDict = LpVariable.dicts(
                'FC', month, lowBound=0, cat='Continuous')
            model += lpSum([inputCostHoldingUnit * ihcDict[i] for i in month]) + lpSum([inputCostHiring * hcDict[i]
                                                                                        for i in month]) + lpSum([inputCostFiring * fcDict[i] for i in month])
            model.addConstraint(inputInventoryInitial + inputProdTemporary *
                                hcDict[0] - inputProdTemporary*fcDict[0] - ihcDict[0] == inputDemand1 - (inputNumPermanent * inputProdPermanent))
            model.addConstraint(ihcDict[0] + inputProdTemporary*hcDict[0] - inputProdTemporary*fcDict[0] + inputProdTemporary *
                                hcDict[1] - inputProdTemporary*fcDict[1] - ihcDict[1] == inputDemand2 - (inputNumPermanent * inputProdPermanent))
            model.addConstraint(ihcDict[1] + inputProdTemporary*hcDict[0] - inputProdTemporary*fcDict[0] + inputProdTemporary*hcDict[1] - inputProdTemporary *
                                fcDict[1] + inputProdTemporary*hcDict[2] - inputProdTemporary*fcDict[2] - ihcDict[2] == inputDemand3 - (inputNumPermanent * inputProdPermanent))
            model.addConstraint(ihcDict[2] + inputProdTemporary*hcDict[0] - inputProdTemporary*fcDict[0] + inputProdTemporary*hcDict[1] - inputProdTemporary*fcDict[1] + inputProdTemporary *
                                hcDict[2] - inputProdTemporary*fcDict[2] + inputProdTemporary*hcDict[3] - inputProdTemporary*fcDict[3] - ihcDict[3] == inputDemand4 - (inputNumPermanent * inputProdPermanent))
            model.solve()
            models.PlanDatabase.objects.filter(planName=inputPlanName).update(inventoryMonth1=ihcDict[0].varValue, inventoryMonth2=ihcDict[1].varValue, inventoryMonth3=ihcDict[2].varValue, hiredTemporary1=hcDict[0].varValue, hiredTemporary2=hcDict[1].varValue, hiredTemporary3=hcDict[
                2].varValue, hiredTemporary4=hcDict[3].varValue, firedTemporary1=fcDict[0].varValue, firedTemporary2=fcDict[1].varValue, firedTemporary3=fcDict[2].varValue, firedTemporary4=fcDict[3].varValue, optimalCost=value(model.objective))
            newInput = models.PlanDatabase.objects.filter(planName=inputPlanName).values()
            for x in newInput:
                rd1 = x['demand1'] - (x['numPermanent'] * x['prodPermanent'])
                rd2 = x['demand2'] - (x['numPermanent'] * x['prodPermanent'])
                rd3 = x['demand3'] - (x['numPermanent'] * x['prodPermanent'])
                rd4 = x['demand4'] - (x['numPermanent'] * x['prodPermanent'])
                ntwH1 = x['hiredTemporary1']
                ntwH2 = x['hiredTemporary2']
                ntwH3 = x['hiredTemporary3']
                ntwH4 = x['hiredTemporary4']
                ntwF1 = x['firedTemporary1']
                ntwF2 = x['firedTemporary2']
                ntwF3 = x['firedTemporary3']
                ntwF4 = x['firedTemporary4']
                ntw1 = ntwH1 - ntwF1 
                ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
                ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
                ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
                hC1 = ntwH1 * x['costHiring']
                hC2 = ntwH2 * x['costHiring']
                hC3 = ntwH3 * x['costHiring']
                hC4 = ntwH4 * x['costHiring']
                fC1 = ntwF1 * x['costFiring']
                fC2 = ntwF2 * x['costFiring']
                fC3 = ntwF3 * x['costFiring']
                fC4 = ntwF4 * x['costFiring']
                ihc1 = x['costHoldingUnit'] * x['inventoryMonth1']
                ihc2 = x['costHoldingUnit'] * x['inventoryMonth2']
                ihc3 = x['costHoldingUnit'] * x['inventoryMonth3']
                ihc4 = x['costHoldingUnit'] * x['inventoryFinal']
                thC = hC1 + hC2 + hC3 + hC4
                tfC = fC1 + fC2 + fC3 + fC4
                tihC = ihc1 + ihc2 + ihc3 + ihc4
                ei1 = x['inventoryMonth1']
                ei2 = x['inventoryMonth2']
                ei3 = x['inventoryMonth3']
                ei4 = x['inventoryFinal']
            return render(request, "main/submitFormView.html",  {'newInput': newInput,
                                                                 'rd1': rd1,
                                                                 'rd2': rd2,
                                                                 'rd3': rd3,
                                                                 'rd4': rd4,
                                                                 'ntw1': ntw1,
                                                                 'ntw2': ntw2,
                                                                 'ntw3': ntw3,
                                                                 'ntw4': ntw4,
                                                                 'ihc1': ihc1,
                                                                 'ihc2': ihc2,
                                                                 'ihc3': ihc3,
                                                                 'ihc4': ihc4,
                                                                 'ntwH1':ntwH1,
                                                                 'ntwH2':ntwH2,
                                                                 'ntwH3':ntwH3,
                                                                 'ntwH4':ntwH4,
                                                                 'ntwF1':ntwF1,
                                                                 'ntwF2':ntwF2,
                                                                 'ntwF3':ntwF3,
                                                                 'ntwF4':ntwF4,
                                                                 'hC1': hC1,
                                                                 'hC2': hC2,
                                                                 'hC3': hC3,
                                                                 'hC4': hC4,
                                                                 'fC1': fC1,
                                                                 'fC2': fC2,
                                                                 'fC3': fC3,
                                                                 'fC4': fC4,
                                                                 'ei1': ei1,
                                                                 'ei2': ei2,
                                                                 'ei3': ei3,
                                                                 'ei4': ei4,
                                                                 'thC': thC,
                                                                 'tfC': tfC,
                                                                 'tihC': tihC
                                                                 })
        else:
            return redirect('boss-login')
    else:
        form = forms.PlanningForm()
    return render(request, 'main/index.html', {'form': form})


def history(request):
    historyList = models.PlanDatabase.objects.all().values
    return render(request, "main/history.html", {'historyList': historyList})


def viewDetail(request,plan_Name):
    detail = models.PlanDatabase.objects.filter(planName=plan_Name).values()
    for x in detail:
        rd1 = x['demand1'] - (x['numPermanent'] * x['prodPermanent'])
        rd2 = x['demand2'] - (x['numPermanent'] * x['prodPermanent'])
        rd3 = x['demand3'] - (x['numPermanent'] * x['prodPermanent'])
        rd4 = x['demand4'] - (x['numPermanent'] * x['prodPermanent'])
        ntwH1 = x['hiredTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF1 = x['firedTemporary1']
        ntwF2 = x['firedTemporary2']
        ntwF3 = x['firedTemporary3']
        ntwF4 = x['firedTemporary4']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        hC1 = ntwH1 * x['costHiring']
        hC2 = ntwH2 * x['costHiring']
        hC3 = ntwH3 * x['costHiring']
        hC4 = ntwH4 * x['costHiring']
        fC1 = ntwF1 * x['costFiring']
        fC2 = ntwF2 * x['costFiring']
        fC3 = ntwF3 * x['costFiring']
        fC4 = ntwF4 * x['costFiring']
        ihc1 = x['costHoldingUnit'] * x['inventoryMonth1']
        ihc2 = x['costHoldingUnit'] * x['inventoryMonth2']
        ihc3 = x['costHoldingUnit'] * x['inventoryMonth3']
        ihc4 = x['costHoldingUnit'] * x['inventoryFinal']
        thC = hC1 + hC2 + hC3 + hC4
        tfC = fC1 + fC2 + fC3 + fC4
        tihC = ihc1 + ihc2 + ihc3 + ihc4
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryFinal']
    return render(request, "main/viewDetail.html", {'detail': detail,
                                                    'rd1': rd1,
                                                    'rd2': rd2,
                                                    'rd3': rd3,
                                                    'rd4': rd4,
                                                    'ntw1': ntw1,
                                                    'ntw2': ntw2,
                                                    'ntw3': ntw3,
                                                    'ntw4': ntw4,
                                                    'ihc1': ihc1,
                                                    'ihc2': ihc2,
                                                    'ihc3': ihc3,
                                                    'ihc4': ihc4,
                                                    'ntwH1':ntwH1,
                                                    'ntwH2':ntwH2,
                                                    'ntwH3':ntwH3,
                                                    'ntwH4':ntwH4,
                                                    'ntwF1':ntwF1,
                                                    'ntwF2':ntwF2,
                                                    'ntwF3':ntwF3,
                                                    'ntwF4':ntwF4,
                                                    'hC1': hC1,
                                                    'hC2': hC2,
                                                    'hC3': hC3,
                                                    'hC4': hC4,
                                                    'fC1': fC1,
                                                    'fC2': fC2,
                                                    'fC3': fC3,
                                                    'fC4': fC4,
                                                    'ei1': ei1,
                                                    'ei2': ei2,
                                                    'ei3': ei3,
                                                    'ei4': ei4,
                                                    'thC': thC,
                                                    'tfC': tfC,
                                                    'tihC': tihC})

def deleteDetail(request,plan_Name):
    detail = models.PlanDatabase.objects.filter(planName=plan_Name)
    detail.delete()
    return redirect(history)
def formula(request):

    return render(request, "main/formula.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
