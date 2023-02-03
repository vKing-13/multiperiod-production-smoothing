from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from main import models, forms
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout, login, authenticate
from pulp import *
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
import xlwt
from io import StringIO,BytesIO
import csv
from django.conf import settings
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
            inputMonthRange = int(request.POST.get('monthRange'))
            if inputMonthRange == 4:
                queryCheck = models.FourMonthPlan.objects.filter(planName=inputPlanName).exists()
                while queryCheck == True:
                    inputPlanName = inputPlanName+'_copy'
                    queryCheck = models.FourMonthPlan.objects.filter(planName=inputPlanName).exists()
                models.FourMonthPlan.objects.create(planName=inputPlanName)
                return redirect('history')
            elif inputMonthRange == 5:
                queryCheck = models.FiveMonthPlan.objects.filter(planName=inputPlanName).exists()
                while queryCheck == True:
                    inputPlanName = inputPlanName+'_copy'
                    queryCheck = models.FiveMonthPlan.objects.filter(planName=inputPlanName).exists()
                models.FiveMonthPlan.objects.create(planName=inputPlanName)
                return redirect('history')
            elif inputMonthRange == 6:
                queryCheck = models.SixMonthPlan.objects.filter(planName=inputPlanName).exists()
                while queryCheck == True:
                    inputPlanName = inputPlanName+'_copy'
                    queryCheck = models.SixMonthPlan.objects.filter(planName=inputPlanName).exists()
                models.SixMonthPlan.objects.create(planName=inputPlanName)
                return redirect('history')
            elif inputMonthRange == 7:
                queryCheck = models.SevenMonthPlan.objects.filter(planName=inputPlanName).exists()
                while queryCheck == True:
                    inputPlanName = inputPlanName+'_copy'
                    queryCheck = models.SevenMonthPlan.objects.filter(planName=inputPlanName).exists()
                models.SevenMonthPlan.objects.create(planName=inputPlanName)
                return redirect('history')
            elif inputMonthRange == 8:
                queryCheck = models.EightMonthPlan.objects.filter(planName=inputPlanName).exists()
                while queryCheck == True:
                    inputPlanName = inputPlanName+'_copy'
                    queryCheck = models.EightMonthPlan.objects.filter(planName=inputPlanName).exists()
                models.EightMonthPlan.objects.create(planName=inputPlanName)
                return redirect('history')
            elif inputMonthRange == 9:
                queryCheck = models.NineMonthPlan.objects.filter(planName=inputPlanName).exists()
                while queryCheck == True:
                    inputPlanName = inputPlanName+'_copy'
                    queryCheck = models.NineMonthPlan.objects.filter(planName=inputPlanName).exists()
                models.NineMonthPlan.objects.create(planName=inputPlanName)
                return redirect('history')
            elif inputMonthRange == 10:
                queryCheck = models.TenMonthPlan.objects.filter(planName=inputPlanName).exists()
                while queryCheck == True:
                    inputPlanName = inputPlanName+'_copy'
                    queryCheck = models.TenMonthPlan.objects.filter(planName=inputPlanName).exists()
                models.TenMonthPlan.objects.create(planName=inputPlanName)
                return redirect('history')
            elif inputMonthRange == 11:
                queryCheck = models.ElevenMonthPlan.objects.filter(planName=inputPlanName).exists()
                while queryCheck == True:
                    inputPlanName = inputPlanName+'_copy'
                    queryCheck = models.ElevenMonthPlan.objects.filter(planName=inputPlanName).exists()
                models.ElevenMonthPlan.objects.create(planName=inputPlanName)
                return redirect('history')
            elif inputMonthRange == 12:
                queryCheck = models.TwelveMonthPlan.objects.filter(planName=inputPlanName).exists()
                while queryCheck == True:
                    inputPlanName = inputPlanName+'_copy'
                    queryCheck = models.TwelveMonthPlan.objects.filter(planName=inputPlanName).exists()
                models.TwelveMonthPlan.objects.create(planName=inputPlanName)
                return redirect('history')
        else:
            return redirect('login')
    return render(request, 'main/index.html')

@login_required(login_url='login/')
def history(request):
    historyListFour = models.FourMonthPlan.objects.all().values
    historyListFive = models.FiveMonthPlan.objects.all().values
    historyListSix = models.SixMonthPlan.objects.all().values
    historyListSeven = models.SevenMonthPlan.objects.all().values
    historyListEight = models.EightMonthPlan.objects.all().values
    historyListNine = models.NineMonthPlan.objects.all().values
    historyListTen = models.TenMonthPlan.objects.all().values
    historyListEleven = models.ElevenMonthPlan.objects.all().values
    historyListTwelve = models.TwelveMonthPlan.objects.all().values
    return render(request, "main/history.html", {'historyListFour': historyListFour, 'historyListFive': historyListFive, 'historyListSix': historyListSix, 'historyListSeven': historyListSeven, 'historyListEight': historyListEight, 'historyListNine': historyListNine, 'historyListTen': historyListTen, 'historyListEleven': historyListEleven, 'historyListTwelve': historyListTwelve})

@login_required(login_url='login/')
def formula(request):

    return render(request, "main/formula.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='login/')
def viewDetailFour(request,plan_Name):
    optimizeFour(plan_Name)
    detail = models.FourMonthPlan.objects.filter(planName=plan_Name).values()
    for x in detail:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        thC = hC1 + hC2 + hC3 + hC4
        tfC = fC1 + fC2 + fC3 + fC4
        tihC = ihc1 + ihc2 + ihc3 + ihc4
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryFinal']
    return render(request, "main/Four/viewDetailFour.html", {'detail': detail, 'rd1': rd1, 'rd2': rd2, 'rd3': rd3, 'rd4': rd4, 'ntw1': ntw1, 'ntw2': ntw2, 'ntw3': ntw3, 'ntw4': ntw4, 'ihc1': ihc1, 'ihc2': ihc2, 'ihc3': ihc3, 'ihc4': ihc4, 'ntwH1':ntwH1, 'ntwH2':ntwH2, 'ntwH3':ntwH3, 'ntwH4':ntwH4, 'ntwF1':ntwF1, 'ntwF2':ntwF2, 'ntwF3':ntwF3, 'ntwF4':ntwF4, 'hC1': hC1, 'hC2': hC2, 'hC3': hC3, 'hC4': hC4, 'fC1': fC1, 'fC2': fC2, 'fC3': fC3, 'fC4': fC4, 'ei1': ei1, 'ei2': ei2, 'ei3': ei3, 'ei4': ei4, 'thC': thC, 'tfC': tfC, 'tihC': tihC})

@login_required(login_url='login/')
def viewDetailFive(request,plan_Name):
    optimizeFive(plan_Name)
    detail = models.FiveMonthPlan.objects.filter(planName=plan_Name).values()
    for x in detail:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        ntwH5 = x['hiredTemporary5']
        ntwF5 = x['firedTemporary5']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryMonth4']
        rd5 = x['demand5'] - (x['numPermanent5'] * x['prodPermanent5'])
        if rd5 < 0:
            rd5 = 0
        hC5 = ntwH5 * x['costHiring5']
        fC5 = ntwF5 * x['costFiring5']
        ihc5 = x['costHoldingUnit5'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        ntw5 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5
        thC = hC1 + hC2 + hC3 + hC4 + hC5
        tfC = fC1 + fC2 + fC3 + fC4 + fC5
        tihC = ihc1 + ihc2 + ihc3 + ihc4 + ihc5
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryMonth4']
        ei5 = x['inventoryFinal']
    return render(request, "main/Five/viewDetailFive.html", {'detail': detail, 'rd1': rd1, 'rd2': rd2, 'rd3': rd3, 'rd4': rd4, 'rd5': rd5, 'ntw1': ntw1, 'ntw2': ntw2, 'ntw3': ntw3, 'ntw4': ntw4, 'ntw5': ntw5, 'ihc1': ihc1, 'ihc2': ihc2, 'ihc3': ihc3, 'ihc4': ihc4, 'ihc5': ihc5, 'ntwH1':ntwH1, 'ntwH2':ntwH2, 'ntwH3':ntwH3, 'ntwH4':ntwH4, 'ntwH5':ntwH5, 'ntwF1':ntwF1, 'ntwF2':ntwF2, 'ntwF3':ntwF3, 'ntwF4':ntwF4, 'ntwF5':ntwF5, 'hC1': hC1, 'hC2': hC2, 'hC3': hC3, 'hC4': hC4, 'hC5': hC5, 'fC1': fC1, 'fC2': fC2, 'fC3': fC3, 'fC4': fC4, 'fC5': fC5, 'ei1': ei1, 'ei2': ei2, 'ei3': ei3, 'ei4': ei4, 'ei5': ei5, 'thC': thC, 'tfC': tfC, 'tihC': tihC})

@login_required(login_url='login/')
def viewDetailSix(request,plan_Name):
    optimizeSix(plan_Name)
    detail = models.SixMonthPlan.objects.filter(planName=plan_Name).values()
    for x in detail:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        ntwH5 = x['hiredTemporary5']
        ntwF5 = x['firedTemporary5']
        ntwH6 = x['hiredTemporary6']
        ntwF6 = x['firedTemporary6']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryMonth4']
        rd5 = x['demand5'] - (x['numPermanent5'] * x['prodPermanent5'])
        if rd5 < 0:
            rd5 = 0
        hC5 = ntwH5 * x['costHiring5']
        fC5 = ntwF5 * x['costFiring5']
        ihc5 = x['costHoldingUnit5'] * x['inventoryMonth5']
        rd6 = x['demand6'] - (x['numPermanent6'] * x['prodPermanent6'])
        if rd6 < 0:
            rd6 = 0
        hC6 = ntwH6 * x['costHiring6']
        fC6 = ntwF6 * x['costFiring6']
        ihc6 = x['costHoldingUnit6'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        ntw5 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5
        ntw6 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6
        thC = hC1 + hC2 + hC3 + hC4 + hC5 + hC6
        tfC = fC1 + fC2 + fC3 + fC4 + fC5 + fC6
        tihC = ihc1 + ihc2 + ihc3 + ihc4 + ihc5 + ihc6
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryMonth4']
        ei5 = x['inventoryMonth5']
        ei6 = x['inventoryFinal']
    return render(request, "main/Six/viewDetailSix.html", {'detail': detail, 'rd1': rd1, 'rd2': rd2, 'rd3': rd3, 'rd4': rd4, 'rd5': rd5, 'rd6': rd6,'ntw1': ntw1, 'ntw2': ntw2, 'ntw3': ntw3, 'ntw4': ntw4, 'ntw5': ntw5, 'ntw6': ntw6,'ihc1': ihc1, 'ihc2': ihc2, 'ihc3': ihc3, 'ihc4': ihc4, 'ihc5': ihc5, 'ihc6': ihc6,'ntwH1':ntwH1, 'ntwH2':ntwH2, 'ntwH3':ntwH3, 'ntwH4':ntwH4, 'ntwH5':ntwH5, 'ntwH6':ntwH6,'ntwF1':ntwF1, 'ntwF2':ntwF2, 'ntwF3':ntwF3, 'ntwF4':ntwF4, 'ntwF5':ntwF5, 'ntwF6':ntwF6,'hC1': hC1, 'hC2': hC2, 'hC3': hC3, 'hC4': hC4, 'hC5': hC5, 'hC6': hC6,'fC1': fC1, 'fC2': fC2, 'fC3': fC3, 'fC4': fC4, 'fC5': fC5, 'fC6': fC6,'ei1': ei1, 'ei2': ei2, 'ei3': ei3, 'ei4': ei4, 'ei5': ei5, 'ei6': ei6,'thC': thC, 'tfC': tfC, 'tihC': tihC})

@login_required(login_url='login/')
def viewDetailSeven(request,plan_Name):
    optimizeSeven(plan_Name)
    detail = models.SevenMonthPlan.objects.filter(planName=plan_Name).values()
    for x in detail:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        ntwH5 = x['hiredTemporary5']
        ntwF5 = x['firedTemporary5']
        ntwH6 = x['hiredTemporary6']
        ntwF6 = x['firedTemporary6']
        ntwH7 = x['hiredTemporary7']
        ntwF7 = x['firedTemporary7']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryMonth4']
        rd5 = x['demand5'] - (x['numPermanent5'] * x['prodPermanent5'])
        if rd5 < 0:
            rd5 = 0
        hC5 = ntwH5 * x['costHiring5']
        fC5 = ntwF5 * x['costFiring5']
        ihc5 = x['costHoldingUnit5'] * x['inventoryMonth5']
        rd6 = x['demand6'] - (x['numPermanent6'] * x['prodPermanent6'])
        if rd6 < 0:
            rd6 = 0
        hC6 = ntwH6 * x['costHiring6']
        fC6 = ntwF6 * x['costFiring6']
        ihc6 = x['costHoldingUnit6'] * x['inventoryMonth6']
        rd7 = x['demand7'] - (x['numPermanent7'] * x['prodPermanent7'])
        if rd7 < 0:
            rd7 = 0
        hC7 = ntwH7 * x['costHiring7']
        fC7 = ntwF7 * x['costFiring7']
        ihc7 = x['costHoldingUnit7'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        ntw5 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5
        ntw6 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6
        ntw7 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7
        thC = hC1 + hC2 + hC3 + hC4 + hC5 + hC6 + hC7
        tfC = fC1 + fC2 + fC3 + fC4 + fC5 + fC6 + fC7
        tihC = ihc1 + ihc2 + ihc3 + ihc4 + ihc5 + ihc6 + ihc7
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryMonth4']
        ei5 = x['inventoryMonth5']
        ei6 = x['inventoryMonth6']
        ei7 = x['inventoryFinal']
    return render(request, "main/Seven/viewDetailSeven.html", {'detail': detail, 'rd1': rd1, 'rd2': rd2, 'rd3': rd3, 'rd4': rd4, 'rd5': rd5, 'rd6': rd6, 'rd7': rd7, 'ntw1': ntw1, 'ntw2': ntw2, 'ntw3': ntw3, 'ntw4': ntw4, 'ntw5': ntw5, 'ntw6': ntw6, 'ntw7': ntw7, 'ihc1': ihc1, 'ihc2': ihc2, 'ihc3': ihc3, 'ihc4': ihc4, 'ihc5': ihc5, 'ihc6': ihc6, 'ihc7': ihc7, 'ntwH1':ntwH1, 'ntwH2':ntwH2, 'ntwH3':ntwH3, 'ntwH4':ntwH4, 'ntwH5':ntwH5, 'ntwH6':ntwH6, 'ntwH7':ntwH7, 'ntwF1':ntwF1, 'ntwF2':ntwF2, 'ntwF3':ntwF3, 'ntwF4':ntwF4, 'ntwF5':ntwF5, 'ntwF6':ntwF6, 'ntwF7':ntwF7, 'hC1': hC1, 'hC2': hC2, 'hC3': hC3, 'hC4': hC4, 'hC5': hC5, 'hC6': hC6, 'hC7': hC7, 'fC1': fC1, 'fC2': fC2, 'fC3': fC3, 'fC4': fC4, 'fC5': fC5, 'fC6': fC6, 'fC7': fC7, 'ei1': ei1, 'ei2': ei2, 'ei3': ei3, 'ei4': ei4, 'ei5': ei5, 'ei6': ei6, 'ei7': ei7, 'thC': thC, 'tfC': tfC, 'tihC': tihC})

@login_required(login_url='login/')
def viewDetailEight(request,plan_Name):
    optimizeEight(plan_Name)
    detail = models.EightMonthPlan.objects.filter(planName=plan_Name).values()
    for x in detail:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        ntwH5 = x['hiredTemporary5']
        ntwF5 = x['firedTemporary5']
        ntwH6 = x['hiredTemporary6']
        ntwF6 = x['firedTemporary6']
        ntwH7 = x['hiredTemporary7']
        ntwF7 = x['firedTemporary7']
        ntwH8 = x['hiredTemporary8']
        ntwF8 = x['firedTemporary8']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryMonth4']
        rd5 = x['demand5'] - (x['numPermanent5'] * x['prodPermanent5'])
        if rd5 < 0:
            rd5 = 0
        hC5 = ntwH5 * x['costHiring5']
        fC5 = ntwF5 * x['costFiring5']
        ihc5 = x['costHoldingUnit5'] * x['inventoryMonth5']
        rd6 = x['demand6'] - (x['numPermanent6'] * x['prodPermanent6'])
        if rd6 < 0:
            rd6 = 0
        hC6 = ntwH6 * x['costHiring6']
        fC6 = ntwF6 * x['costFiring6']
        ihc6 = x['costHoldingUnit6'] * x['inventoryMonth6']
        rd7 = x['demand7'] - (x['numPermanent7'] * x['prodPermanent7'])
        if rd7 < 0:
            rd7 = 0
        hC7 = ntwH7 * x['costHiring7']
        fC7 = ntwF7 * x['costFiring7']
        ihc7 = x['costHoldingUnit7'] * x['inventoryMonth7']
        rd8 = x['demand8'] - (x['numPermanent8'] * x['prodPermanent8'])
        if rd8 < 0:
            rd8 = 0
        hC8 = ntwH8 * x['costHiring8']
        fC8 = ntwF8 * x['costFiring8']
        ihc8 = x['costHoldingUnit8'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        ntw5 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5
        ntw6 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6
        ntw7 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7
        ntw8 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8
        thC = hC1 + hC2 + hC3 + hC4 + hC5 + hC6 + hC7 + hC8
        tfC = fC1 + fC2 + fC3 + fC4 + fC5 + fC6 + fC7 + fC8
        tihC = ihc1 + ihc2 + ihc3 + ihc4 + ihc5 + ihc6 + ihc7 + ihc8
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryMonth4']
        ei5 = x['inventoryMonth5']
        ei6 = x['inventoryMonth6']
        ei7 = x['inventoryMonth7']
        ei8 = x['inventoryFinal']
    return render(request, "main/Eight/viewDetailEight.html", {'detail': detail, 'rd1': rd1, 'rd2': rd2, 'rd3': rd3, 'rd4': rd4, 'rd5': rd5, 'rd6': rd6, 'rd7': rd7, 'rd8': rd8, 'ntw1': ntw1, 'ntw2': ntw2, 'ntw3': ntw3, 'ntw4': ntw4, 'ntw5': ntw5, 'ntw6': ntw6, 'ntw7': ntw7, 'ntw8': ntw8, 'ihc1': ihc1, 'ihc2': ihc2, 'ihc3': ihc3, 'ihc4': ihc4, 'ihc5': ihc5, 'ihc6': ihc6, 'ihc7': ihc7, 'ihc8': ihc8, 'ntwH1':ntwH1, 'ntwH2':ntwH2, 'ntwH3':ntwH3, 'ntwH4':ntwH4, 'ntwH5':ntwH5, 'ntwH6':ntwH6, 'ntwH7':ntwH7, 'ntwH8':ntwH8, 'ntwF1':ntwF1, 'ntwF2':ntwF2, 'ntwF3':ntwF3, 'ntwF4':ntwF4, 'ntwF5':ntwF5, 'ntwF6':ntwF6, 'ntwF7':ntwF7, 'ntwF8':ntwF8, 'hC1': hC1, 'hC2': hC2, 'hC3': hC3, 'hC4': hC4, 'hC5': hC5, 'hC6': hC6, 'hC7': hC7, 'hC8': hC8, 'fC1': fC1, 'fC2': fC2, 'fC3': fC3, 'fC4': fC4, 'fC5': fC5, 'fC6': fC6, 'fC7': fC7, 'fC8': fC8, 'ei1': ei1, 'ei2': ei2, 'ei3': ei3, 'ei4': ei4, 'ei5': ei5, 'ei6': ei6, 'ei7': ei7, 'ei8': ei8, 'thC': thC, 'tfC': tfC, 'tihC': tihC})

@login_required(login_url='login/')
def viewDetailNine(request,plan_Name):
    optimizeNine(plan_Name)
    detail = models.NineMonthPlan.objects.filter(planName=plan_Name).values()
    for x in detail:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        ntwH5 = x['hiredTemporary5']
        ntwF5 = x['firedTemporary5']
        ntwH6 = x['hiredTemporary6']
        ntwF6 = x['firedTemporary6']
        ntwH7 = x['hiredTemporary7']
        ntwF7 = x['firedTemporary7']
        ntwH8 = x['hiredTemporary8']
        ntwF8 = x['firedTemporary8']
        ntwH9 = x['hiredTemporary9']
        ntwF9 = x['firedTemporary9']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryMonth4']
        rd5 = x['demand5'] - (x['numPermanent5'] * x['prodPermanent5'])
        if rd5 < 0:
            rd5 = 0
        hC5 = ntwH5 * x['costHiring5']
        fC5 = ntwF5 * x['costFiring5']
        ihc5 = x['costHoldingUnit5'] * x['inventoryMonth5']
        rd6 = x['demand6'] - (x['numPermanent6'] * x['prodPermanent6'])
        if rd6 < 0:
            rd6 = 0
        hC6 = ntwH6 * x['costHiring6']
        fC6 = ntwF6 * x['costFiring6']
        ihc6 = x['costHoldingUnit6'] * x['inventoryMonth6']
        rd7 = x['demand7'] - (x['numPermanent7'] * x['prodPermanent7'])
        if rd7 < 0:
            rd7 = 0
        hC7 = ntwH7 * x['costHiring7']
        fC7 = ntwF7 * x['costFiring7']
        ihc7 = x['costHoldingUnit7'] * x['inventoryMonth7']
        rd8 = x['demand8'] - (x['numPermanent8'] * x['prodPermanent8'])
        if rd8 < 0:
            rd8 = 0
        hC8 = ntwH8 * x['costHiring8']
        fC8 = ntwF8 * x['costFiring8']
        ihc8 = x['costHoldingUnit8'] * x['inventoryMonth8']
        rd9 = x['demand9'] - (x['numPermanent9'] * x['prodPermanent9'])
        if rd9 < 0:
            rd9 = 0
        hC9 = ntwH9 * x['costHiring9']
        fC9 = ntwF9 * x['costFiring9']
        ihc9 = x['costHoldingUnit9'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        ntw5 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5
        ntw6 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6
        ntw7 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7
        ntw8 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8
        ntw9 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9
        thC = hC1 + hC2 + hC3 + hC4 + hC5 + hC6 + hC7 + hC8 + hC9
        tfC = fC1 + fC2 + fC3 + fC4 + fC5 + fC6 + fC7 + fC8 + fC9
        tihC = ihc1 + ihc2 + ihc3 + ihc4 + ihc5 + ihc6 + ihc7 + ihc8 + ihc9
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryMonth4']
        ei5 = x['inventoryMonth5']
        ei6 = x['inventoryMonth6']
        ei7 = x['inventoryMonth7']
        ei8 = x['inventoryMonth8']
        ei9 = x['inventoryFinal']
    return render(request, "main/Nine/viewDetailNine.html", {'detail': detail, 'rd1': rd1, 'rd2': rd2, 'rd3': rd3, 'rd4': rd4, 'rd5': rd5, 'rd6': rd6, 'rd7': rd7, 'rd8': rd8, 'rd9': rd9,'ntw1': ntw1, 'ntw2': ntw2, 'ntw3': ntw3, 'ntw4': ntw4, 'ntw5': ntw5, 'ntw6': ntw6, 'ntw7': ntw7, 'ntw8': ntw8, 'ntw9': ntw9,'ihc1': ihc1, 'ihc2': ihc2, 'ihc3': ihc3, 'ihc4': ihc4, 'ihc5': ihc5, 'ihc6': ihc6, 'ihc7': ihc7, 'ihc8': ihc8, 'ihc9': ihc9,'ntwH1':ntwH1, 'ntwH2':ntwH2, 'ntwH3':ntwH3, 'ntwH4':ntwH4, 'ntwH5':ntwH5, 'ntwH6':ntwH6, 'ntwH7':ntwH7, 'ntwH8':ntwH8, 'ntwH9':ntwH9,'ntwF1':ntwF1, 'ntwF2':ntwF2, 'ntwF3':ntwF3, 'ntwF4':ntwF4, 'ntwF5':ntwF5, 'ntwF6':ntwF6, 'ntwF7':ntwF7, 'ntwF8':ntwF8, 'ntwF9':ntwF9,'hC1': hC1, 'hC2': hC2, 'hC3': hC3, 'hC4': hC4, 'hC5': hC5, 'hC6': hC6, 'hC7': hC7, 'hC8': hC8, 'hC9': hC9,'fC1': fC1, 'fC2': fC2, 'fC3': fC3, 'fC4': fC4, 'fC5': fC5, 'fC6': fC6, 'fC7': fC7, 'fC8': fC8, 'fC9': fC9,'ei1': ei1, 'ei2': ei2, 'ei3': ei3, 'ei4': ei4, 'ei5': ei5, 'ei6': ei6, 'ei7': ei7, 'ei8': ei8, 'ei9': ei9,'thC': thC, 'tfC': tfC, 'tihC': tihC})

@login_required(login_url='login/')
def viewDetailTen(request,plan_Name):
    optimizeTen(plan_Name)
    detail = models.TenMonthPlan.objects.filter(planName=plan_Name).values()
    for x in detail:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        ntwH5 = x['hiredTemporary5']
        ntwF5 = x['firedTemporary5']
        ntwH6 = x['hiredTemporary6']
        ntwF6 = x['firedTemporary6']
        ntwH7 = x['hiredTemporary7']
        ntwF7 = x['firedTemporary7']
        ntwH8 = x['hiredTemporary8']
        ntwF8 = x['firedTemporary8']
        ntwH9 = x['hiredTemporary9']
        ntwF9 = x['firedTemporary9']
        ntwH10 = x['hiredTemporary10']
        ntwF10 = x['firedTemporary10']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryMonth4']
        rd5 = x['demand5'] - (x['numPermanent5'] * x['prodPermanent5'])
        if rd5 < 0:
            rd5 = 0
        hC5 = ntwH5 * x['costHiring5']
        fC5 = ntwF5 * x['costFiring5']
        ihc5 = x['costHoldingUnit5'] * x['inventoryMonth5']
        rd6 = x['demand6'] - (x['numPermanent6'] * x['prodPermanent6'])
        if rd6 < 0:
            rd6 = 0
        hC6 = ntwH6 * x['costHiring6']
        fC6 = ntwF6 * x['costFiring6']
        ihc6 = x['costHoldingUnit6'] * x['inventoryMonth6']
        rd7 = x['demand7'] - (x['numPermanent7'] * x['prodPermanent7'])
        if rd7 < 0:
            rd7 = 0
        hC7 = ntwH7 * x['costHiring7']
        fC7 = ntwF7 * x['costFiring7']
        ihc7 = x['costHoldingUnit7'] * x['inventoryMonth7']
        rd8 = x['demand8'] - (x['numPermanent8'] * x['prodPermanent8'])
        if rd8 < 0:
            rd8 = 0
        hC8 = ntwH8 * x['costHiring8']
        fC8 = ntwF8 * x['costFiring8']
        ihc8 = x['costHoldingUnit8'] * x['inventoryMonth8']
        rd9 = x['demand9'] - (x['numPermanent9'] * x['prodPermanent9'])
        if rd9 < 0:
            rd9 = 0
        hC9 = ntwH9 * x['costHiring9']
        fC9 = ntwF9 * x['costFiring9']
        ihc9 = x['costHoldingUnit9'] * x['inventoryMonth9']
        rd10 = x['demand10'] - (x['numPermanent10'] * x['prodPermanent10'])
        if rd10 < 0:
            rd10 = 0
        hC10 = ntwH10 * x['costHiring10']
        fC10 = ntwF10 * x['costFiring10']
        ihc10 = x['costHoldingUnit10'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        ntw5 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5
        ntw6 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6
        ntw7 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7
        ntw8 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8
        ntw9 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9
        ntw10 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9 + ntwH10 - ntwF10
        thC = hC1 + hC2 + hC3 + hC4 + hC5 + hC6 + hC7 + hC8 + hC9 + hC10
        tfC = fC1 + fC2 + fC3 + fC4 + fC5 + fC6 + fC7 + fC8 + fC9 + fC10
        tihC = ihc1 + ihc2 + ihc3 + ihc4 + ihc5 + ihc6 + ihc7 + ihc8 + ihc9 + ihc10
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryMonth4']
        ei5 = x['inventoryMonth5']
        ei6 = x['inventoryMonth6']
        ei7 = x['inventoryMonth7']
        ei8 = x['inventoryMonth8']
        ei9 = x['inventoryMonth9']
        ei10 = x['inventoryFinal']
    return render(request, "main/Ten/viewDetailTen.html", {'detail': detail, 'rd1': rd1, 'rd2': rd2, 'rd3': rd3, 'rd4': rd4, 'rd5': rd5, 'rd6': rd6, 'rd7': rd7, 'rd8': rd8, 'rd9': rd9, 'rd10': rd10, 'ntw1': ntw1, 'ntw2': ntw2, 'ntw3': ntw3, 'ntw4': ntw4, 'ntw5': ntw5, 'ntw6': ntw6, 'ntw7': ntw7, 'ntw8': ntw8, 'ntw9': ntw9, 'ntw10': ntw10, 'ihc1': ihc1, 'ihc2': ihc2, 'ihc3': ihc3, 'ihc4': ihc4, 'ihc5': ihc5, 'ihc6': ihc6, 'ihc7': ihc7, 'ihc8': ihc8, 'ihc9': ihc9, 'ihc10': ihc10, 'ntwH1':ntwH1, 'ntwH2':ntwH2, 'ntwH3':ntwH3, 'ntwH4':ntwH4, 'ntwH5':ntwH5, 'ntwH6':ntwH6, 'ntwH7':ntwH7, 'ntwH8':ntwH8, 'ntwH9':ntwH9, 'ntwH10':ntwH10, 'ntwF1':ntwF1, 'ntwF2':ntwF2, 'ntwF3':ntwF3, 'ntwF4':ntwF4, 'ntwF5':ntwF5, 'ntwF6':ntwF6, 'ntwF7':ntwF7, 'ntwF8':ntwF8, 'ntwF9':ntwF9, 'ntwF10':ntwF10, 'hC1': hC1, 'hC2': hC2, 'hC3': hC3, 'hC4': hC4, 'hC5': hC5, 'hC6': hC6, 'hC7': hC7, 'hC8': hC8, 'hC9': hC9, 'hC10': hC10, 'fC1': fC1, 'fC2': fC2, 'fC3': fC3, 'fC4': fC4, 'fC5': fC5, 'fC6': fC6, 'fC7': fC7, 'fC8': fC8, 'fC9': fC9, 'fC10': fC10, 'ei1': ei1, 'ei2': ei2, 'ei3': ei3, 'ei4': ei4, 'ei5': ei5, 'ei6': ei6, 'ei7': ei7, 'ei8': ei8, 'ei9': ei9, 'ei10': ei10, 'thC': thC, 'tfC': tfC, 'tihC': tihC})

@login_required(login_url='login/')
def viewDetailEleven(request,plan_Name):
    optimizeEleven(plan_Name)
    detail = models.ElevenMonthPlan.objects.filter(planName=plan_Name).values()
    for x in detail:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        ntwH5 = x['hiredTemporary5']
        ntwF5 = x['firedTemporary5']
        ntwH6 = x['hiredTemporary6']
        ntwF6 = x['firedTemporary6']
        ntwH7 = x['hiredTemporary7']
        ntwF7 = x['firedTemporary7']
        ntwH8 = x['hiredTemporary8']
        ntwF8 = x['firedTemporary8']
        ntwH9 = x['hiredTemporary9']
        ntwF9 = x['firedTemporary9']
        ntwH10 = x['hiredTemporary10']
        ntwF10 = x['firedTemporary10']
        ntwH11 = x['hiredTemporary11']
        ntwF11 = x['firedTemporary11']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryMonth4']
        rd5 = x['demand5'] - (x['numPermanent5'] * x['prodPermanent5'])
        if rd5 < 0:
            rd5 = 0
        hC5 = ntwH5 * x['costHiring5']
        fC5 = ntwF5 * x['costFiring5']
        ihc5 = x['costHoldingUnit5'] * x['inventoryMonth5']
        rd6 = x['demand6'] - (x['numPermanent6'] * x['prodPermanent6'])
        if rd6 < 0:
            rd6 = 0
        hC6 = ntwH6 * x['costHiring6']
        fC6 = ntwF6 * x['costFiring6']
        ihc6 = x['costHoldingUnit6'] * x['inventoryMonth6']
        rd7 = x['demand7'] - (x['numPermanent7'] * x['prodPermanent7'])
        if rd7 < 0:
            rd7 = 0
        hC7 = ntwH7 * x['costHiring7']
        fC7 = ntwF7 * x['costFiring7']
        ihc7 = x['costHoldingUnit7'] * x['inventoryMonth7']
        rd8 = x['demand8'] - (x['numPermanent8'] * x['prodPermanent8'])
        if rd8 < 0:
            rd8 = 0
        hC8 = ntwH8 * x['costHiring8']
        fC8 = ntwF8 * x['costFiring8']
        ihc8 = x['costHoldingUnit8'] * x['inventoryMonth8']
        rd9 = x['demand9'] - (x['numPermanent9'] * x['prodPermanent9'])
        if rd9 < 0:
            rd9 = 0
        hC9 = ntwH9 * x['costHiring9']
        fC9 = ntwF9 * x['costFiring9']
        ihc9 = x['costHoldingUnit9'] * x['inventoryMonth9']
        rd10 = x['demand10'] - (x['numPermanent10'] * x['prodPermanent10'])
        if rd10 < 0:
            rd10 = 0
        hC10 = ntwH10 * x['costHiring10']
        fC10 = ntwF10 * x['costFiring10']
        ihc10 = x['costHoldingUnit10'] * x['inventoryMonth10']
        rd11 = x['demand11'] - (x['numPermanent11'] * x['prodPermanent11'])
        if rd11 < 0:
            rd11 = 0
        hC11 = ntwH11 * x['costHiring11']
        fC11 = ntwF11 * x['costFiring11']
        ihc11 = x['costHoldingUnit11'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        ntw5 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5
        ntw6 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6
        ntw7 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7
        ntw8 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8
        ntw9 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9
        ntw10 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9 + ntwH10 - ntwF10
        ntw11 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9 + ntwH10 - ntwF10 + ntwH11 - ntwF11
        thC = hC1 + hC2 + hC3 + hC4 + hC5 + hC6 + hC7 + hC8 + hC9 + hC10 + hC11
        tfC = fC1 + fC2 + fC3 + fC4 + fC5 + fC6 + fC7 + fC8 + fC9 + fC10 + fC11
        tihC = ihc1 + ihc2 + ihc3 + ihc4 + ihc5 + ihc6 + ihc7 + ihc8 + ihc9 + ihc10 + ihc11
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryMonth4']
        ei5 = x['inventoryMonth5']
        ei6 = x['inventoryMonth6']
        ei7 = x['inventoryMonth7']
        ei8 = x['inventoryMonth8']
        ei9 = x['inventoryMonth9']
        ei10 = x['inventoryMonth10']
        ei11 = x['inventoryFinal']
    return render(request, "main/Eleven/viewDetailEleven.html", {'detail': detail, 'rd1': rd1, 'rd2': rd2, 'rd3': rd3, 'rd4': rd4, 'rd5': rd5, 'rd6': rd6, 'rd7': rd7, 'rd8': rd8, 'rd9': rd9, 'rd10': rd10, 'rd11': rd11, 'ntw1': ntw1, 'ntw2': ntw2, 'ntw3': ntw3, 'ntw4': ntw4, 'ntw5': ntw5, 'ntw6': ntw6, 'ntw7': ntw7, 'ntw8': ntw8, 'ntw9': ntw9, 'ntw10': ntw10, 'ntw11': ntw11, 'ihc1': ihc1, 'ihc2': ihc2, 'ihc3': ihc3, 'ihc4': ihc4, 'ihc5': ihc5, 'ihc6': ihc6, 'ihc7': ihc7, 'ihc8': ihc8, 'ihc9': ihc9, 'ihc10': ihc10, 'ihc11': ihc11, 'ntwH1':ntwH1, 'ntwH2':ntwH2, 'ntwH3':ntwH3, 'ntwH4':ntwH4, 'ntwH5':ntwH5, 'ntwH6':ntwH6, 'ntwH7':ntwH7, 'ntwH8':ntwH8, 'ntwH9':ntwH9, 'ntwH10':ntwH10, 'ntwH11':ntwH11, 'ntwF1':ntwF1, 'ntwF2':ntwF2, 'ntwF3':ntwF3, 'ntwF4':ntwF4, 'ntwF5':ntwF5, 'ntwF6':ntwF6, 'ntwF7':ntwF7, 'ntwF8':ntwF8, 'ntwF9':ntwF9, 'ntwF10':ntwF10, 'ntwF11':ntwF11, 'hC1': hC1, 'hC2': hC2, 'hC3': hC3, 'hC4': hC4, 'hC5': hC5, 'hC6': hC6, 'hC7': hC7, 'hC8': hC8, 'hC9': hC9, 'hC10': hC10, 'hC11': hC11, 'fC1': fC1, 'fC2': fC2, 'fC3': fC3, 'fC4': fC4, 'fC5': fC5, 'fC6': fC6, 'fC7': fC7, 'fC8': fC8, 'fC9': fC9, 'fC10': fC10, 'fC11': fC11, 'ei1': ei1, 'ei2': ei2, 'ei3': ei3, 'ei4': ei4, 'ei5': ei5, 'ei6': ei6, 'ei7': ei7, 'ei8': ei8, 'ei9': ei9, 'ei10': ei10, 'ei11': ei11, 'thC': thC, 'tfC': tfC, 'tihC': tihC})

@login_required(login_url='login/')
def viewDetailTwelve(request,plan_Name):
    optimizeTwelve(plan_Name)
    detail = models.TwelveMonthPlan.objects.filter(planName=plan_Name).values()
    for x in detail:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        ntwH5 = x['hiredTemporary5']
        ntwF5 = x['firedTemporary5']
        ntwH6 = x['hiredTemporary6']
        ntwF6 = x['firedTemporary6']
        ntwH7 = x['hiredTemporary7']
        ntwF7 = x['firedTemporary7']
        ntwH8 = x['hiredTemporary8']
        ntwF8 = x['firedTemporary8']
        ntwH9 = x['hiredTemporary9']
        ntwF9 = x['firedTemporary9']
        ntwH10 = x['hiredTemporary10']
        ntwF10 = x['firedTemporary10']
        ntwH11 = x['hiredTemporary11']
        ntwF11 = x['firedTemporary11']
        ntwH12 = x['hiredTemporary12']
        ntwF12 = x['firedTemporary12']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryMonth4']
        rd5 = x['demand5'] - (x['numPermanent5'] * x['prodPermanent5'])
        if rd5 < 0:
            rd5 = 0
        hC5 = ntwH5 * x['costHiring5']
        fC5 = ntwF5 * x['costFiring5']
        ihc5 = x['costHoldingUnit5'] * x['inventoryMonth5']
        rd6 = x['demand6'] - (x['numPermanent6'] * x['prodPermanent6'])
        if rd6 < 0:
            rd6 = 0
        hC6 = ntwH6 * x['costHiring6']
        fC6 = ntwF6 * x['costFiring6']
        ihc6 = x['costHoldingUnit6'] * x['inventoryMonth6']
        rd7 = x['demand7'] - (x['numPermanent7'] * x['prodPermanent7'])
        if rd7 < 0:
            rd7 = 0
        hC7 = ntwH7 * x['costHiring7']
        fC7 = ntwF7 * x['costFiring7']
        ihc7 = x['costHoldingUnit7'] * x['inventoryMonth7']
        rd8 = x['demand8'] - (x['numPermanent8'] * x['prodPermanent8'])
        if rd8 < 0:
            rd8 = 0
        hC8 = ntwH8 * x['costHiring8']
        fC8 = ntwF8 * x['costFiring8']
        ihc8 = x['costHoldingUnit8'] * x['inventoryMonth8']
        rd9 = x['demand9'] - (x['numPermanent9'] * x['prodPermanent9'])
        if rd9 < 0:
            rd9 = 0
        hC9 = ntwH9 * x['costHiring9']
        fC9 = ntwF9 * x['costFiring9']
        ihc9 = x['costHoldingUnit9'] * x['inventoryMonth9']
        rd10 = x['demand10'] - (x['numPermanent10'] * x['prodPermanent10'])
        if rd10 < 0:
            rd10 = 0
        hC10 = ntwH10 * x['costHiring10']
        fC10 = ntwF10 * x['costFiring10']
        ihc10 = x['costHoldingUnit10'] * x['inventoryMonth10']
        rd11 = x['demand11'] - (x['numPermanent11'] * x['prodPermanent11'])
        if rd11 < 0:
            rd11 = 0
        hC11 = ntwH11 * x['costHiring11']
        fC11 = ntwF11 * x['costFiring11']
        ihc11 = x['costHoldingUnit11'] * x['inventoryMonth11']
        rd12 = x['demand12'] - (x['numPermanent12'] * x['prodPermanent12'])
        if rd12 < 0:
            rd12 = 0
        hC12 = ntwH12 * x['costHiring12']
        fC12 = ntwF12 * x['costFiring12']
        ihc12 = x['costHoldingUnit12'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        ntw5 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5
        ntw6 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6
        ntw7 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7
        ntw8 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8
        ntw9 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9
        ntw10 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9 + ntwH10 - ntwF10
        ntw11 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9 + ntwH10 - ntwF10 + ntwH11 - ntwF11
        ntw12 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9 + ntwH10 - ntwF10 + ntwH11 - ntwF11 + ntwH12 - ntwF12
        thC = hC1 + hC2 + hC3 + hC4 + hC5 + hC6 + hC7 + hC8 + hC9 + hC10 + hC11 + hC12
        tfC = fC1 + fC2 + fC3 + fC4 + fC5 + fC6 + fC7 + fC8 + fC9 + fC10 + fC11 + fC12
        tihC = ihc1 + ihc2 + ihc3 + ihc4 + ihc5 + ihc6 + ihc7 + ihc8 + ihc9 + ihc10 + ihc11 + ihc12
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryMonth4']
        ei5 = x['inventoryMonth5']
        ei6 = x['inventoryMonth6']
        ei7 = x['inventoryMonth7']
        ei8 = x['inventoryMonth8']
        ei9 = x['inventoryMonth9']
        ei10 = x['inventoryMonth10']
        ei11 = x['inventoryMonth11']
        ei12 = x['inventoryFinal']
    return render(request, "main/Twelve/viewDetailTwelve.html", {'detail': detail, 'rd1': rd1, 'rd2': rd2, 'rd3': rd3, 'rd4': rd4, 'rd5': rd5, 'rd6': rd6, 'rd7': rd7, 'rd8': rd8, 'rd9': rd9, 'rd10': rd10, 'rd11': rd11, 'rd12': rd12, 'ntw1': ntw1, 'ntw2': ntw2, 'ntw3': ntw3, 'ntw4': ntw4, 'ntw5': ntw5, 'ntw6': ntw6, 'ntw7': ntw7, 'ntw8': ntw8, 'ntw9': ntw9, 'ntw10': ntw10, 'ntw11': ntw11, 'ntw12': ntw12, 'ihc1': ihc1, 'ihc2': ihc2, 'ihc3': ihc3, 'ihc4': ihc4, 'ihc5': ihc5, 'ihc6': ihc6, 'ihc7': ihc7, 'ihc8': ihc8, 'ihc9': ihc9, 'ihc10': ihc10, 'ihc11': ihc11, 'ihc12': ihc12, 'ntwH1':ntwH1, 'ntwH2':ntwH2, 'ntwH3':ntwH3, 'ntwH4':ntwH4, 'ntwH5':ntwH5, 'ntwH6':ntwH6, 'ntwH7':ntwH7, 'ntwH8':ntwH8, 'ntwH9':ntwH9, 'ntwH10':ntwH10, 'ntwH11':ntwH11, 'ntwH12':ntwH12, 'ntwF1':ntwF1, 'ntwF2':ntwF2, 'ntwF3':ntwF3, 'ntwF4':ntwF4, 'ntwF5':ntwF5, 'ntwF6':ntwF6, 'ntwF7':ntwF7, 'ntwF8':ntwF8, 'ntwF9':ntwF9, 'ntwF10':ntwF10, 'ntwF11':ntwF11, 'ntwF12':ntwF12, 'hC1': hC1, 'hC2': hC2, 'hC3': hC3, 'hC4': hC4, 'hC5': hC5, 'hC6': hC6, 'hC7': hC7, 'hC8': hC8, 'hC9': hC9, 'hC10': hC10, 'hC11': hC11, 'hC12': hC12, 'fC1': fC1, 'fC2': fC2, 'fC3': fC3, 'fC4': fC4, 'fC5': fC5, 'fC6': fC6, 'fC7': fC7, 'fC8': fC8, 'fC9': fC9, 'fC10': fC10, 'fC11': fC11, 'fC12': fC12, 'ei1': ei1, 'ei2': ei2, 'ei3': ei3, 'ei4': ei4, 'ei5': ei5, 'ei6': ei6, 'ei7': ei7, 'ei8': ei8, 'ei9': ei9, 'ei10': ei10, 'ei11': ei11, 'ei12': ei12, 'thC': thC, 'tfC': tfC, 'tihC': tihC})


def deleteDetailFour(request,plan_Name):
    detail = models.FourMonthPlan.objects.filter(planName=plan_Name)
    detail.delete()
    return redirect(history)


def deleteDetailFive(request,plan_Name):
    detail = models.FiveMonthPlan.objects.filter(planName=plan_Name)
    detail.delete()
    return redirect(history)


def deleteDetailSix(request,plan_Name):
    detail = models.SixMonthPlan.objects.filter(planName=plan_Name)
    detail.delete()
    return redirect(history)


def deleteDetailSeven(request,plan_Name):
    detail = models.SevenMonthPlan.objects.filter(planName=plan_Name)
    detail.delete()
    return redirect(history)


def deleteDetailEight(request,plan_Name):
    detail = models.EightMonthPlan.objects.filter(planName=plan_Name)
    detail.delete()
    return redirect(history)


def deleteDetailNine(request,plan_Name):
    detail = models.NineMonthPlan.objects.filter(planName=plan_Name)
    detail.delete()
    return redirect(history)


def deleteDetailTen(request,plan_Name):
    detail = models.TenMonthPlan.objects.filter(planName=plan_Name)
    detail.delete()
    return redirect(history)


def deleteDetailEleven(request,plan_Name):
    detail = models.ElevenMonthPlan.objects.filter(planName=plan_Name)
    detail.delete()
    return redirect(history)


def deleteDetailTwelve(request,plan_Name):
    detail = models.TwelveMonthPlan.objects.filter(planName=plan_Name)
    detail.delete()
    return redirect(history)


def optimizeFour(inputPlanName):
    qs = models.FourMonthPlan.objects.filter(planName=inputPlanName).values()
    for x in qs:
        inputInventoryInitial = int(x['inventoryInitial'])
        inputInventoryFinal = x['inventoryFinal']
        
        inputDemand1 = int(x['demand1'])
        inputNumPermanent1 = int(x['numPermanent1'])
        inputProdPermanent1 = int(x['prodPermanent1'])
        inputProdTemporary1 = int(x['prodTemporary1'])
        inputCostHiring1 = float(x['costHiring1'])
        inputCostFiring1 = float(x['costFiring1'])
        inputCostHoldingUnit1 = float(x['costHoldingUnit1'])
        
        inputDemand2 = int(x['demand2'])
        inputNumPermanent2 = int(x['numPermanent2'])
        inputProdPermanent2 = int(x['prodPermanent2'])
        inputProdTemporary2 = int(x['prodTemporary2'])
        inputCostHiring2 = float(x['costHiring2'])
        inputCostFiring2 = float(x['costFiring2'])
        inputCostHoldingUnit2 = float(x['costHoldingUnit2'])
        
        inputDemand3 = int(x['demand3'])
        inputNumPermanent3 = int(x['numPermanent3'])
        inputProdPermanent3 = int(x['prodPermanent3'])
        inputProdTemporary3 = int(x['prodTemporary3'])
        inputCostHiring3 = float(x['costHiring3'])
        inputCostFiring3 = float(x['costFiring3'])
        inputCostHoldingUnit3 = float(x['costHoldingUnit3'])
        
        inputDemand4 = int(x['demand4'])
        inputNumPermanent4 = int(x['numPermanent4'])
        inputProdPermanent4 = int(x['prodPermanent4'])
        inputProdTemporary4 = int(x['prodTemporary4'])
        inputCostHiring4 = float(x['costHiring4'])
        inputCostFiring4 = float(x['costFiring4'])
        inputCostHoldingUnit4 = float(x['costHoldingUnit4'])
    model = LpProblem("Minimize Cost", LpMinimize)
    month = list(range(4))
    ihcDict = LpVariable.dicts(
        'IHC', month, lowBound=0, cat='Continuous')
    ihcDict[3] = inputInventoryFinal
    hcDict = LpVariable.dicts(
        'HC', month, lowBound=0, cat='Continuous')
    fcDict = LpVariable.dicts(
        'FC', month, lowBound=0, cat='Continuous')
    inputCostHoldingUnitDict = [inputCostHoldingUnit1, inputCostHoldingUnit2, inputCostHoldingUnit3, inputCostHoldingUnit4]
    inputCostHiringDict = [inputCostHiring1, inputCostHiring2, inputCostHiring3, inputCostHiring4]
    inputCostFiringDict = [inputCostFiring1, inputCostFiring2, inputCostFiring3, inputCostFiring4]
    model += lpSum([inputCostHoldingUnitDict[i] * ihcDict[i] for i in month]) + lpSum([inputCostHiringDict[i] * hcDict[i] for i in month]) + lpSum([inputCostFiringDict[i] * fcDict[i] for i in month])
    model.addConstraint(inputInventoryInitial + inputProdTemporary1 * hcDict[0] - inputProdTemporary1 * fcDict[0] - ihcDict[0] == inputDemand1 - (inputNumPermanent1 * inputProdPermanent1))
    model.addConstraint(ihcDict[0] + inputProdTemporary2 * hcDict[0] - inputProdTemporary2*fcDict[0] + inputProdTemporary2*hcDict[1] - inputProdTemporary2*fcDict[1] - ihcDict[1] == inputDemand2 - (inputNumPermanent2 * inputProdPermanent2))
    model.addConstraint(ihcDict[1] + inputProdTemporary3 * hcDict[0] - inputProdTemporary3*fcDict[0] + inputProdTemporary3*hcDict[1] - inputProdTemporary3*fcDict[1] + inputProdTemporary3*hcDict[2] - inputProdTemporary3*fcDict[2] - ihcDict[2] == inputDemand3 - (inputNumPermanent3 * inputProdPermanent3))
    model.addConstraint(ihcDict[2] + inputProdTemporary4 * hcDict[0] - inputProdTemporary4*fcDict[0] + inputProdTemporary4*hcDict[1] - inputProdTemporary4*fcDict[1] + inputProdTemporary4*hcDict[2] - inputProdTemporary4*fcDict[2] + inputProdTemporary4*hcDict[3] - inputProdTemporary4*fcDict[3] - ihcDict[3] == inputDemand4 - (inputNumPermanent4 * inputProdPermanent4))
    model.solve()
    models.FourMonthPlan.objects.filter(planName = inputPlanName).update(inventoryInitial = inputInventoryInitial, inventoryFinal = inputInventoryFinal,inventoryMonth1 = ihcDict[0].varValue, inventoryMonth2 = ihcDict[1].varValue, inventoryMonth3 = ihcDict[2].varValue, hiredTemporary1 = hcDict[0].varValue, hiredTemporary2 = hcDict[1].varValue, hiredTemporary3 = hcDict[2].varValue, hiredTemporary4 = hcDict[3].varValue, firedTemporary1 = fcDict[0].varValue, firedTemporary2 = fcDict[1].varValue, firedTemporary3 = fcDict[2].varValue, firedTemporary4 = fcDict[3].varValue, optimalCost = value(model.objective))


def optimizeFive(inputPlanName):
    qs = models.FiveMonthPlan.objects.filter(planName=inputPlanName).values()
    for x in qs:
        inputInventoryInitial = int(x['inventoryInitial'])
        inputInventoryFinal = x['inventoryFinal']
        
        inputDemand1 = int(x['demand1'])
        inputNumPermanent1 = int(x['numPermanent1'])
        inputProdPermanent1 = int(x['prodPermanent1'])
        inputProdTemporary1 = int(x['prodTemporary1'])
        inputCostHiring1 = float(x['costHiring1'])
        inputCostFiring1 = float(x['costFiring1'])
        inputCostHoldingUnit1 = float(x['costHoldingUnit1'])
        
        inputDemand2 = int(x['demand2'])
        inputNumPermanent2 = int(x['numPermanent2'])
        inputProdPermanent2 = int(x['prodPermanent2'])
        inputProdTemporary2 = int(x['prodTemporary2'])
        inputCostHiring2 = float(x['costHiring2'])
        inputCostFiring2 = float(x['costFiring2'])
        inputCostHoldingUnit2 = float(x['costHoldingUnit2'])
        
        inputDemand3 = int(x['demand3'])
        inputNumPermanent3 = int(x['numPermanent3'])
        inputProdPermanent3 = int(x['prodPermanent3'])
        inputProdTemporary3 = int(x['prodTemporary3'])
        inputCostHiring3 = float(x['costHiring3'])
        inputCostFiring3 = float(x['costFiring3'])
        inputCostHoldingUnit3 = float(x['costHoldingUnit3'])
        
        inputDemand4 = int(x['demand4'])
        inputNumPermanent4 = int(x['numPermanent4'])
        inputProdPermanent4 = int(x['prodPermanent4'])
        inputProdTemporary4 = int(x['prodTemporary4'])
        inputCostHiring4 = float(x['costHiring4'])
        inputCostFiring4 = float(x['costFiring4'])
        inputCostHoldingUnit4 = float(x['costHoldingUnit4'])
        
        inputDemand5 = int(x['demand5'])
        inputNumPermanent5 = int(x['numPermanent5'])
        inputProdPermanent5 = int(x['prodPermanent5'])
        inputProdTemporary5 = int(x['prodTemporary5'])
        inputCostHiring5 = float(x['costHiring5'])
        inputCostFiring5 = float(x['costFiring5'])
        inputCostHoldingUnit5 = float(x['costHoldingUnit5'])
    model = LpProblem("Minimize Cost", LpMinimize)
    month = list(range(5))
    ihcDict = LpVariable.dicts(
        'IHC', month, lowBound=0, cat='Continuous')
    ihcDict[4] = inputInventoryFinal
    hcDict = LpVariable.dicts(
        'HC', month, lowBound=0, cat='Continuous')
    fcDict = LpVariable.dicts(
        'FC', month, lowBound=0, cat='Continuous')
    inputCostHoldingUnitDict = [inputCostHoldingUnit1, inputCostHoldingUnit2, inputCostHoldingUnit3, inputCostHoldingUnit4, inputCostHoldingUnit5]
    inputCostHiringDict = [inputCostHiring1, inputCostHiring2, inputCostHiring3, inputCostHiring4, inputCostHiring5]
    inputCostFiringDict = [inputCostFiring1, inputCostFiring2, inputCostFiring3, inputCostFiring4, inputCostFiring5]
    model += lpSum([inputCostHoldingUnitDict[i] * ihcDict[i] for i in month]) + lpSum([inputCostHiringDict[i] * hcDict[i] for i in month]) + lpSum([inputCostFiringDict[i] * fcDict[i] for i in month])
    model.addConstraint(inputInventoryInitial + inputProdTemporary1 * hcDict[0] - inputProdTemporary1 * fcDict[0] - ihcDict[0] == inputDemand1 - (inputNumPermanent1 * inputProdPermanent1))
    model.addConstraint(ihcDict[0] + inputProdTemporary2 * hcDict[0] - inputProdTemporary2*fcDict[0] + inputProdTemporary2*hcDict[1] - inputProdTemporary2*fcDict[1] - ihcDict[1] == inputDemand2 - (inputNumPermanent2 * inputProdPermanent2))
    model.addConstraint(ihcDict[1] + inputProdTemporary3 * hcDict[0] - inputProdTemporary3*fcDict[0] + inputProdTemporary3*hcDict[1] - inputProdTemporary3*fcDict[1] + inputProdTemporary3*hcDict[2] - inputProdTemporary3*fcDict[2] - ihcDict[2] == inputDemand3 - (inputNumPermanent3 * inputProdPermanent3))
    model.addConstraint(ihcDict[2] + inputProdTemporary4 * hcDict[0] - inputProdTemporary4*fcDict[0] + inputProdTemporary4*hcDict[1] - inputProdTemporary4*fcDict[1] + inputProdTemporary4*hcDict[2] - inputProdTemporary4*fcDict[2] + inputProdTemporary4*hcDict[3] - inputProdTemporary4*fcDict[3] - ihcDict[3] == inputDemand4 - (inputNumPermanent4 * inputProdPermanent4))
    model.addConstraint(ihcDict[3] + inputProdTemporary5 * hcDict[0] - inputProdTemporary5*fcDict[0] + inputProdTemporary5*hcDict[1] - inputProdTemporary5*fcDict[1] + inputProdTemporary5*hcDict[2] - inputProdTemporary5*fcDict[2] + inputProdTemporary5*hcDict[3] - inputProdTemporary5*fcDict[3] + inputProdTemporary5*hcDict[4] - inputProdTemporary5*fcDict[4] - ihcDict[4] == inputDemand5 - (inputNumPermanent5 * inputProdPermanent5))
    model.solve()
    models.FiveMonthPlan.objects.filter(planName = inputPlanName).update(inventoryInitial = inputInventoryInitial, inventoryFinal = inputInventoryFinal,inventoryMonth1 = ihcDict[0].varValue, inventoryMonth2 = ihcDict[1].varValue, inventoryMonth3 = ihcDict[2].varValue, inventoryMonth4 = ihcDict[3].varValue, hiredTemporary1 = hcDict[0].varValue, hiredTemporary2 = hcDict[1].varValue, hiredTemporary3 = hcDict[2].varValue, hiredTemporary4 = hcDict[3].varValue, hiredTemporary5 = hcDict[4].varValue, firedTemporary1 = fcDict[0].varValue, firedTemporary2 = fcDict[1].varValue, firedTemporary3 = fcDict[2].varValue, firedTemporary4 = fcDict[3].varValue, firedTemporary5 = fcDict[4].varValue, optimalCost = value(model.objective))


def optimizeSix(inputPlanName):
    qs = models.SixMonthPlan.objects.filter(planName=inputPlanName).values()
    for x in qs:
        inputInventoryInitial = int(x['inventoryInitial'])
        inputInventoryFinal = x['inventoryFinal']
        
        inputDemand1 = int(x['demand1'])
        inputNumPermanent1 = int(x['numPermanent1'])
        inputProdPermanent1 = int(x['prodPermanent1'])
        inputProdTemporary1 = int(x['prodTemporary1'])
        inputCostHiring1 = float(x['costHiring1'])
        inputCostFiring1 = float(x['costFiring1'])
        inputCostHoldingUnit1 = float(x['costHoldingUnit1'])
        
        inputDemand2 = int(x['demand2'])
        inputNumPermanent2 = int(x['numPermanent2'])
        inputProdPermanent2 = int(x['prodPermanent2'])
        inputProdTemporary2 = int(x['prodTemporary2'])
        inputCostHiring2 = float(x['costHiring2'])
        inputCostFiring2 = float(x['costFiring2'])
        inputCostHoldingUnit2 = float(x['costHoldingUnit2'])
        
        inputDemand3 = int(x['demand3'])
        inputNumPermanent3 = int(x['numPermanent3'])
        inputProdPermanent3 = int(x['prodPermanent3'])
        inputProdTemporary3 = int(x['prodTemporary3'])
        inputCostHiring3 = float(x['costHiring3'])
        inputCostFiring3 = float(x['costFiring3'])
        inputCostHoldingUnit3 = float(x['costHoldingUnit3'])
        
        inputDemand4 = int(x['demand4'])
        inputNumPermanent4 = int(x['numPermanent4'])
        inputProdPermanent4 = int(x['prodPermanent4'])
        inputProdTemporary4 = int(x['prodTemporary4'])
        inputCostHiring4 = float(x['costHiring4'])
        inputCostFiring4 = float(x['costFiring4'])
        inputCostHoldingUnit4 = float(x['costHoldingUnit4'])
        
        inputDemand5 = int(x['demand5'])
        inputNumPermanent5 = int(x['numPermanent5'])
        inputProdPermanent5 = int(x['prodPermanent5'])
        inputProdTemporary5 = int(x['prodTemporary5'])
        inputCostHiring5 = float(x['costHiring5'])
        inputCostFiring5 = float(x['costFiring5'])
        inputCostHoldingUnit5 = float(x['costHoldingUnit5'])
        
        inputDemand6 = int(x['demand6'])
        inputNumPermanent6 = int(x['numPermanent6'])
        inputProdPermanent6 = int(x['prodPermanent6'])
        inputProdTemporary6 = int(x['prodTemporary6'])
        inputCostHiring6 = float(x['costHiring6'])
        inputCostFiring6 = float(x['costFiring6'])
        inputCostHoldingUnit6 = float(x['costHoldingUnit6'])
    model = LpProblem("Minimize Cost", LpMinimize)
    month = list(range(6))
    ihcDict = LpVariable.dicts(
        'IHC', month, lowBound=0, cat='Continuous')
    ihcDict[5] = inputInventoryFinal
    hcDict = LpVariable.dicts(
        'HC', month, lowBound=0, cat='Continuous')
    fcDict = LpVariable.dicts(
        'FC', month, lowBound=0, cat='Continuous')
    inputCostHoldingUnitDict = [inputCostHoldingUnit1, inputCostHoldingUnit2, inputCostHoldingUnit3, inputCostHoldingUnit4, inputCostHoldingUnit5, inputCostHoldingUnit6]
    inputCostHiringDict = [inputCostHiring1, inputCostHiring2, inputCostHiring3, inputCostHiring4, inputCostHiring5, inputCostHiring6]
    inputCostFiringDict = [inputCostFiring1, inputCostFiring2, inputCostFiring3, inputCostFiring4, inputCostFiring5, inputCostFiring6]
    model += lpSum([inputCostHoldingUnitDict[i] * ihcDict[i] for i in month]) + lpSum([inputCostHiringDict[i] * hcDict[i] for i in month]) + lpSum([inputCostFiringDict[i] * fcDict[i] for i in month])
    model.addConstraint(inputInventoryInitial + inputProdTemporary1 * hcDict[0] - inputProdTemporary1 * fcDict[0] - ihcDict[0] == inputDemand1 - (inputNumPermanent1 * inputProdPermanent1))
    model.addConstraint(ihcDict[0] + inputProdTemporary2 * hcDict[0] - inputProdTemporary2*fcDict[0] + inputProdTemporary2*hcDict[1] - inputProdTemporary2*fcDict[1] - ihcDict[1] == inputDemand2 - (inputNumPermanent2 * inputProdPermanent2))
    model.addConstraint(ihcDict[1] + inputProdTemporary3 * hcDict[0] - inputProdTemporary3*fcDict[0] + inputProdTemporary3*hcDict[1] - inputProdTemporary3*fcDict[1] + inputProdTemporary3*hcDict[2] - inputProdTemporary3*fcDict[2] - ihcDict[2] == inputDemand3 - (inputNumPermanent3 * inputProdPermanent3))
    model.addConstraint(ihcDict[2] + inputProdTemporary4 * hcDict[0] - inputProdTemporary4*fcDict[0] + inputProdTemporary4*hcDict[1] - inputProdTemporary4*fcDict[1] + inputProdTemporary4*hcDict[2] - inputProdTemporary4*fcDict[2] + inputProdTemporary4*hcDict[3] - inputProdTemporary4*fcDict[3] - ihcDict[3] == inputDemand4 - (inputNumPermanent4 * inputProdPermanent4))
    model.addConstraint(ihcDict[3] + inputProdTemporary5 * hcDict[0] - inputProdTemporary5*fcDict[0] + inputProdTemporary5*hcDict[1] - inputProdTemporary5*fcDict[1] + inputProdTemporary5*hcDict[2] - inputProdTemporary5*fcDict[2] + inputProdTemporary5*hcDict[3] - inputProdTemporary5*fcDict[3] + inputProdTemporary5*hcDict[4] - inputProdTemporary5*fcDict[4] - ihcDict[4] == inputDemand5 - (inputNumPermanent5 * inputProdPermanent5))
    model.addConstraint(ihcDict[4] + inputProdTemporary6 * hcDict[0] - inputProdTemporary6*fcDict[0] + inputProdTemporary6*hcDict[1] - inputProdTemporary6*fcDict[1] + inputProdTemporary6*hcDict[2] - inputProdTemporary6*fcDict[2] + inputProdTemporary6*hcDict[3] - inputProdTemporary6*fcDict[3] + inputProdTemporary6*hcDict[4] - inputProdTemporary6*fcDict[4] + inputProdTemporary6*hcDict[5] - inputProdTemporary6*fcDict[5] - ihcDict[5] == inputDemand6 - (inputNumPermanent6 * inputProdPermanent6))
    model.solve()
    models.SixMonthPlan.objects.filter(planName = inputPlanName).update(inventoryInitial = inputInventoryInitial, inventoryFinal = inputInventoryFinal,inventoryMonth1 = ihcDict[0].varValue, inventoryMonth2 = ihcDict[1].varValue, inventoryMonth3 = ihcDict[2].varValue, inventoryMonth4 = ihcDict[3].varValue, inventoryMonth5 = ihcDict[4].varValue, hiredTemporary1 = hcDict[0].varValue, hiredTemporary2 = hcDict[1].varValue, hiredTemporary3 = hcDict[2].varValue, hiredTemporary4 = hcDict[3].varValue, hiredTemporary5 = hcDict[4].varValue, hiredTemporary6 = hcDict[5].varValue, firedTemporary1 = fcDict[0].varValue, firedTemporary2 = fcDict[1].varValue, firedTemporary3 = fcDict[2].varValue, firedTemporary4 = fcDict[3].varValue, firedTemporary5 = fcDict[4].varValue, firedTemporary6 = fcDict[5].varValue, optimalCost = value(model.objective))


def optimizeSeven(inputPlanName):
    qs = models.SevenMonthPlan.objects.filter(planName=inputPlanName).values()
    for x in qs:
        inputInventoryInitial = int(x['inventoryInitial'])
        inputInventoryFinal = x['inventoryFinal']
        
        inputDemand1 = int(x['demand1'])
        inputNumPermanent1 = int(x['numPermanent1'])
        inputProdPermanent1 = int(x['prodPermanent1'])
        inputProdTemporary1 = int(x['prodTemporary1'])
        inputCostHiring1 = float(x['costHiring1'])
        inputCostFiring1 = float(x['costFiring1'])
        inputCostHoldingUnit1 = float(x['costHoldingUnit1'])
        
        inputDemand2 = int(x['demand2'])
        inputNumPermanent2 = int(x['numPermanent2'])
        inputProdPermanent2 = int(x['prodPermanent2'])
        inputProdTemporary2 = int(x['prodTemporary2'])
        inputCostHiring2 = float(x['costHiring2'])
        inputCostFiring2 = float(x['costFiring2'])
        inputCostHoldingUnit2 = float(x['costHoldingUnit2'])
        
        inputDemand3 = int(x['demand3'])
        inputNumPermanent3 = int(x['numPermanent3'])
        inputProdPermanent3 = int(x['prodPermanent3'])
        inputProdTemporary3 = int(x['prodTemporary3'])
        inputCostHiring3 = float(x['costHiring3'])
        inputCostFiring3 = float(x['costFiring3'])
        inputCostHoldingUnit3 = float(x['costHoldingUnit3'])
        
        inputDemand4 = int(x['demand4'])
        inputNumPermanent4 = int(x['numPermanent4'])
        inputProdPermanent4 = int(x['prodPermanent4'])
        inputProdTemporary4 = int(x['prodTemporary4'])
        inputCostHiring4 = float(x['costHiring4'])
        inputCostFiring4 = float(x['costFiring4'])
        inputCostHoldingUnit4 = float(x['costHoldingUnit4'])
        
        inputDemand5 = int(x['demand5'])
        inputNumPermanent5 = int(x['numPermanent5'])
        inputProdPermanent5 = int(x['prodPermanent5'])
        inputProdTemporary5 = int(x['prodTemporary5'])
        inputCostHiring5 = float(x['costHiring5'])
        inputCostFiring5 = float(x['costFiring5'])
        inputCostHoldingUnit5 = float(x['costHoldingUnit5'])
        
        inputDemand6 = int(x['demand6'])
        inputNumPermanent6 = int(x['numPermanent6'])
        inputProdPermanent6 = int(x['prodPermanent6'])
        inputProdTemporary6 = int(x['prodTemporary6'])
        inputCostHiring6 = float(x['costHiring6'])
        inputCostFiring6 = float(x['costFiring6'])
        inputCostHoldingUnit6 = float(x['costHoldingUnit6'])
        
        inputDemand7 = int(x['demand7'])
        inputNumPermanent7 = int(x['numPermanent7'])
        inputProdPermanent7 = int(x['prodPermanent7'])
        inputProdTemporary7 = int(x['prodTemporary7'])
        inputCostHiring7 = float(x['costHiring7'])
        inputCostFiring7 = float(x['costFiring7'])
        inputCostHoldingUnit7 = float(x['costHoldingUnit7'])
    model = LpProblem("Minimize Cost", LpMinimize)
    month = list(range(7))
    ihcDict = LpVariable.dicts(
        'IHC', month, lowBound=0, cat='Continuous')
    ihcDict[6] = inputInventoryFinal
    hcDict = LpVariable.dicts(
        'HC', month, lowBound=0, cat='Continuous')
    fcDict = LpVariable.dicts(
        'FC', month, lowBound=0, cat='Continuous')
    inputCostHoldingUnitDict = [inputCostHoldingUnit1, inputCostHoldingUnit2, inputCostHoldingUnit3, inputCostHoldingUnit4, inputCostHoldingUnit5, inputCostHoldingUnit6, inputCostHoldingUnit7]
    inputCostHiringDict = [inputCostHiring1, inputCostHiring2, inputCostHiring3, inputCostHiring4, inputCostHiring5, inputCostHiring6, inputCostHiring7]
    inputCostFiringDict = [inputCostFiring1, inputCostFiring2, inputCostFiring3, inputCostFiring4, inputCostFiring5, inputCostFiring6, inputCostFiring7]
    model += lpSum([inputCostHoldingUnitDict[i] * ihcDict[i] for i in month]) + lpSum([inputCostHiringDict[i] * hcDict[i] for i in month]) + lpSum([inputCostFiringDict[i] * fcDict[i] for i in month])
    model.addConstraint(inputInventoryInitial + inputProdTemporary1 * hcDict[0] - inputProdTemporary1 * fcDict[0] - ihcDict[0] == inputDemand1 - (inputNumPermanent1 * inputProdPermanent1))
    model.addConstraint(ihcDict[0] + inputProdTemporary2 * hcDict[0] - inputProdTemporary2*fcDict[0] + inputProdTemporary2*hcDict[1] - inputProdTemporary2*fcDict[1] - ihcDict[1] == inputDemand2 - (inputNumPermanent2 * inputProdPermanent2))
    model.addConstraint(ihcDict[1] + inputProdTemporary3 * hcDict[0] - inputProdTemporary3*fcDict[0] + inputProdTemporary3*hcDict[1] - inputProdTemporary3*fcDict[1] + inputProdTemporary3*hcDict[2] - inputProdTemporary3*fcDict[2] - ihcDict[2] == inputDemand3 - (inputNumPermanent3 * inputProdPermanent3))
    model.addConstraint(ihcDict[2] + inputProdTemporary4 * hcDict[0] - inputProdTemporary4*fcDict[0] + inputProdTemporary4*hcDict[1] - inputProdTemporary4*fcDict[1] + inputProdTemporary4*hcDict[2] - inputProdTemporary4*fcDict[2] + inputProdTemporary4*hcDict[3] - inputProdTemporary4*fcDict[3] - ihcDict[3] == inputDemand4 - (inputNumPermanent4 * inputProdPermanent4))
    model.addConstraint(ihcDict[3] + inputProdTemporary5 * hcDict[0] - inputProdTemporary5*fcDict[0] + inputProdTemporary5*hcDict[1] - inputProdTemporary5*fcDict[1] + inputProdTemporary5*hcDict[2] - inputProdTemporary5*fcDict[2] + inputProdTemporary5*hcDict[3] - inputProdTemporary5*fcDict[3] + inputProdTemporary5*hcDict[4] - inputProdTemporary5*fcDict[4] - ihcDict[4] == inputDemand5 - (inputNumPermanent5 * inputProdPermanent5))
    model.addConstraint(ihcDict[4] + inputProdTemporary6 * hcDict[0] - inputProdTemporary6*fcDict[0] + inputProdTemporary6*hcDict[1] - inputProdTemporary6*fcDict[1] + inputProdTemporary6*hcDict[2] - inputProdTemporary6*fcDict[2] + inputProdTemporary6*hcDict[3] - inputProdTemporary6*fcDict[3] + inputProdTemporary6*hcDict[4] - inputProdTemporary6*fcDict[4] + inputProdTemporary6*hcDict[5] - inputProdTemporary6*fcDict[5] - ihcDict[5] == inputDemand6 - (inputNumPermanent6 * inputProdPermanent6))
    model.addConstraint(ihcDict[5] + inputProdTemporary7 * hcDict[0] - inputProdTemporary7*fcDict[0] + inputProdTemporary7*hcDict[1] - inputProdTemporary7*fcDict[1] + inputProdTemporary7*hcDict[2] - inputProdTemporary7*fcDict[2] + inputProdTemporary7*hcDict[3] - inputProdTemporary7*fcDict[3] + inputProdTemporary7*hcDict[4] - inputProdTemporary7*fcDict[4] + inputProdTemporary7*hcDict[5] - inputProdTemporary7*fcDict[5] + inputProdTemporary7*hcDict[6] - inputProdTemporary7*fcDict[6] - ihcDict[6] == inputDemand7 - (inputNumPermanent7 * inputProdPermanent7))
    model.solve()
    models.SevenMonthPlan.objects.filter(planName = inputPlanName).update(inventoryInitial = inputInventoryInitial, inventoryFinal = inputInventoryFinal,inventoryMonth1 = ihcDict[0].varValue, inventoryMonth2 = ihcDict[1].varValue, inventoryMonth3 = ihcDict[2].varValue, inventoryMonth4 = ihcDict[3].varValue, inventoryMonth5 = ihcDict[4].varValue, inventoryMonth6 = ihcDict[5].varValue, hiredTemporary1 = hcDict[0].varValue, hiredTemporary2 = hcDict[1].varValue, hiredTemporary3 = hcDict[2].varValue, hiredTemporary4 = hcDict[3].varValue, hiredTemporary5 = hcDict[4].varValue, hiredTemporary6 = hcDict[5].varValue, hiredTemporary7 = hcDict[6].varValue, firedTemporary1 = fcDict[0].varValue, firedTemporary2 = fcDict[1].varValue, firedTemporary3 = fcDict[2].varValue, firedTemporary4 = fcDict[3].varValue, firedTemporary5 = fcDict[4].varValue, firedTemporary6 = fcDict[5].varValue, firedTemporary7 = fcDict[6].varValue, optimalCost = value(model.objective))


def optimizeEight(inputPlanName):
    qs = models.EightMonthPlan.objects.filter(planName=inputPlanName).values()
    for x in qs:
        inputInventoryInitial = int(x['inventoryInitial'])
        inputInventoryFinal = x['inventoryFinal']
        
        inputDemand1 = int(x['demand1'])
        inputNumPermanent1 = int(x['numPermanent1'])
        inputProdPermanent1 = int(x['prodPermanent1'])
        inputProdTemporary1 = int(x['prodTemporary1'])
        inputCostHiring1 = float(x['costHiring1'])
        inputCostFiring1 = float(x['costFiring1'])
        inputCostHoldingUnit1 = float(x['costHoldingUnit1'])
        
        inputDemand2 = int(x['demand2'])
        inputNumPermanent2 = int(x['numPermanent2'])
        inputProdPermanent2 = int(x['prodPermanent2'])
        inputProdTemporary2 = int(x['prodTemporary2'])
        inputCostHiring2 = float(x['costHiring2'])
        inputCostFiring2 = float(x['costFiring2'])
        inputCostHoldingUnit2 = float(x['costHoldingUnit2'])
        
        inputDemand3 = int(x['demand3'])
        inputNumPermanent3 = int(x['numPermanent3'])
        inputProdPermanent3 = int(x['prodPermanent3'])
        inputProdTemporary3 = int(x['prodTemporary3'])
        inputCostHiring3 = float(x['costHiring3'])
        inputCostFiring3 = float(x['costFiring3'])
        inputCostHoldingUnit3 = float(x['costHoldingUnit3'])
        
        inputDemand4 = int(x['demand4'])
        inputNumPermanent4 = int(x['numPermanent4'])
        inputProdPermanent4 = int(x['prodPermanent4'])
        inputProdTemporary4 = int(x['prodTemporary4'])
        inputCostHiring4 = float(x['costHiring4'])
        inputCostFiring4 = float(x['costFiring4'])
        inputCostHoldingUnit4 = float(x['costHoldingUnit4'])
        
        inputDemand5 = int(x['demand5'])
        inputNumPermanent5 = int(x['numPermanent5'])
        inputProdPermanent5 = int(x['prodPermanent5'])
        inputProdTemporary5 = int(x['prodTemporary5'])
        inputCostHiring5 = float(x['costHiring5'])
        inputCostFiring5 = float(x['costFiring5'])
        inputCostHoldingUnit5 = float(x['costHoldingUnit5'])
        
        inputDemand6 = int(x['demand6'])
        inputNumPermanent6 = int(x['numPermanent6'])
        inputProdPermanent6 = int(x['prodPermanent6'])
        inputProdTemporary6 = int(x['prodTemporary6'])
        inputCostHiring6 = float(x['costHiring6'])
        inputCostFiring6 = float(x['costFiring6'])
        inputCostHoldingUnit6 = float(x['costHoldingUnit6'])
        
        inputDemand7 = int(x['demand7'])
        inputNumPermanent7 = int(x['numPermanent7'])
        inputProdPermanent7 = int(x['prodPermanent7'])
        inputProdTemporary7 = int(x['prodTemporary7'])
        inputCostHiring7 = float(x['costHiring7'])
        inputCostFiring7 = float(x['costFiring7'])
        inputCostHoldingUnit7 = float(x['costHoldingUnit7'])
        
        inputDemand8 = int(x['demand8'])
        inputNumPermanent8 = int(x['numPermanent8'])
        inputProdPermanent8 = int(x['prodPermanent8'])
        inputProdTemporary8 = int(x['prodTemporary8'])
        inputCostHiring8 = float(x['costHiring8'])
        inputCostFiring8 = float(x['costFiring8'])
        inputCostHoldingUnit8 = float(x['costHoldingUnit8'])
    model = LpProblem("Minimize Cost", LpMinimize)
    month = list(range(8))
    ihcDict = LpVariable.dicts(
        'IHC', month, lowBound=0, cat='Continuous')
    ihcDict[7] = inputInventoryFinal
    hcDict = LpVariable.dicts(
        'HC', month, lowBound=0, cat='Continuous')
    fcDict = LpVariable.dicts(
        'FC', month, lowBound=0, cat='Continuous')
    inputCostHoldingUnitDict = [inputCostHoldingUnit1, inputCostHoldingUnit2, inputCostHoldingUnit3, inputCostHoldingUnit4, inputCostHoldingUnit5, inputCostHoldingUnit6, inputCostHoldingUnit7, inputCostHoldingUnit8]
    inputCostHiringDict = [inputCostHiring1, inputCostHiring2, inputCostHiring3, inputCostHiring4, inputCostHiring5, inputCostHiring6, inputCostHiring7, inputCostHiring8]
    inputCostFiringDict = [inputCostFiring1, inputCostFiring2, inputCostFiring3, inputCostFiring4, inputCostFiring5, inputCostFiring6, inputCostFiring7, inputCostFiring8]
    model += lpSum([inputCostHoldingUnitDict[i] * ihcDict[i] for i in month]) + lpSum([inputCostHiringDict[i] * hcDict[i] for i in month]) + lpSum([inputCostFiringDict[i] * fcDict[i] for i in month])
    model.addConstraint(inputInventoryInitial + inputProdTemporary1 * hcDict[0] - inputProdTemporary1 * fcDict[0] - ihcDict[0] == inputDemand1 - (inputNumPermanent1 * inputProdPermanent1))
    model.addConstraint(ihcDict[0] + inputProdTemporary2 * hcDict[0] - inputProdTemporary2*fcDict[0] + inputProdTemporary2*hcDict[1] - inputProdTemporary2*fcDict[1] - ihcDict[1] == inputDemand2 - (inputNumPermanent2 * inputProdPermanent2))
    model.addConstraint(ihcDict[1] + inputProdTemporary3 * hcDict[0] - inputProdTemporary3*fcDict[0] + inputProdTemporary3*hcDict[1] - inputProdTemporary3*fcDict[1] + inputProdTemporary3*hcDict[2] - inputProdTemporary3*fcDict[2] - ihcDict[2] == inputDemand3 - (inputNumPermanent3 * inputProdPermanent3))
    model.addConstraint(ihcDict[2] + inputProdTemporary4 * hcDict[0] - inputProdTemporary4*fcDict[0] + inputProdTemporary4*hcDict[1] - inputProdTemporary4*fcDict[1] + inputProdTemporary4*hcDict[2] - inputProdTemporary4*fcDict[2] + inputProdTemporary4*hcDict[3] - inputProdTemporary4*fcDict[3] - ihcDict[3] == inputDemand4 - (inputNumPermanent4 * inputProdPermanent4))
    model.addConstraint(ihcDict[3] + inputProdTemporary5 * hcDict[0] - inputProdTemporary5*fcDict[0] + inputProdTemporary5*hcDict[1] - inputProdTemporary5*fcDict[1] + inputProdTemporary5*hcDict[2] - inputProdTemporary5*fcDict[2] + inputProdTemporary5*hcDict[3] - inputProdTemporary5*fcDict[3] + inputProdTemporary5*hcDict[4] - inputProdTemporary5*fcDict[4] - ihcDict[4] == inputDemand5 - (inputNumPermanent5 * inputProdPermanent5))
    model.addConstraint(ihcDict[4] + inputProdTemporary6 * hcDict[0] - inputProdTemporary6*fcDict[0] + inputProdTemporary6*hcDict[1] - inputProdTemporary6*fcDict[1] + inputProdTemporary6*hcDict[2] - inputProdTemporary6*fcDict[2] + inputProdTemporary6*hcDict[3] - inputProdTemporary6*fcDict[3] + inputProdTemporary6*hcDict[4] - inputProdTemporary6*fcDict[4] + inputProdTemporary6*hcDict[5] - inputProdTemporary6*fcDict[5] - ihcDict[5] == inputDemand6 - (inputNumPermanent6 * inputProdPermanent6))
    model.addConstraint(ihcDict[5] + inputProdTemporary7 * hcDict[0] - inputProdTemporary7*fcDict[0] + inputProdTemporary7*hcDict[1] - inputProdTemporary7*fcDict[1] + inputProdTemporary7*hcDict[2] - inputProdTemporary7*fcDict[2] + inputProdTemporary7*hcDict[3] - inputProdTemporary7*fcDict[3] + inputProdTemporary7*hcDict[4] - inputProdTemporary7*fcDict[4] + inputProdTemporary7*hcDict[5] - inputProdTemporary7*fcDict[5] + inputProdTemporary7*hcDict[6] - inputProdTemporary7*fcDict[6] - ihcDict[6] == inputDemand7 - (inputNumPermanent7 * inputProdPermanent7))
    model.addConstraint(ihcDict[6] + inputProdTemporary8 * hcDict[0] - inputProdTemporary8*fcDict[0] + inputProdTemporary8*hcDict[1] - inputProdTemporary8*fcDict[1] + inputProdTemporary8*hcDict[2] - inputProdTemporary8*fcDict[2] + inputProdTemporary8*hcDict[3] - inputProdTemporary8*fcDict[3] + inputProdTemporary8*hcDict[4] - inputProdTemporary8*fcDict[4] + inputProdTemporary8*hcDict[5] - inputProdTemporary8*fcDict[5] + inputProdTemporary8*hcDict[6] - inputProdTemporary8*fcDict[6] + inputProdTemporary8*hcDict[7] - inputProdTemporary8*fcDict[7] - ihcDict[7] == inputDemand8 - (inputNumPermanent8 * inputProdPermanent8))
    model.solve()
    models.EightMonthPlan.objects.filter(planName = inputPlanName).update(inventoryInitial = inputInventoryInitial, inventoryFinal = inputInventoryFinal,inventoryMonth1 = ihcDict[0].varValue, inventoryMonth2 = ihcDict[1].varValue, inventoryMonth3 = ihcDict[2].varValue, inventoryMonth4 = ihcDict[3].varValue, inventoryMonth5 = ihcDict[4].varValue, inventoryMonth6 = ihcDict[5].varValue, inventoryMonth7 = ihcDict[6].varValue, hiredTemporary1 = hcDict[0].varValue, hiredTemporary2 = hcDict[1].varValue, hiredTemporary3 = hcDict[2].varValue, hiredTemporary4 = hcDict[3].varValue, hiredTemporary5 = hcDict[4].varValue, hiredTemporary6 = hcDict[5].varValue, hiredTemporary7 = hcDict[6].varValue, hiredTemporary8 = hcDict[7].varValue, firedTemporary1 = fcDict[0].varValue, firedTemporary2 = fcDict[1].varValue, firedTemporary3 = fcDict[2].varValue, firedTemporary4 = fcDict[3].varValue, firedTemporary5 = fcDict[4].varValue, firedTemporary6 = fcDict[5].varValue, firedTemporary7 = fcDict[6].varValue, firedTemporary8 = fcDict[7].varValue, optimalCost = value(model.objective))


def optimizeNine(inputPlanName):
    qs = models.NineMonthPlan.objects.filter(planName=inputPlanName).values()
    for x in qs:
        inputInventoryInitial = int(x['inventoryInitial'])
        inputInventoryFinal = x['inventoryFinal']
        
        inputDemand1 = int(x['demand1'])
        inputNumPermanent1 = int(x['numPermanent1'])
        inputProdPermanent1 = int(x['prodPermanent1'])
        inputProdTemporary1 = int(x['prodTemporary1'])
        inputCostHiring1 = float(x['costHiring1'])
        inputCostFiring1 = float(x['costFiring1'])
        inputCostHoldingUnit1 = float(x['costHoldingUnit1'])
        
        inputDemand2 = int(x['demand2'])
        inputNumPermanent2 = int(x['numPermanent2'])
        inputProdPermanent2 = int(x['prodPermanent2'])
        inputProdTemporary2 = int(x['prodTemporary2'])
        inputCostHiring2 = float(x['costHiring2'])
        inputCostFiring2 = float(x['costFiring2'])
        inputCostHoldingUnit2 = float(x['costHoldingUnit2'])
        
        inputDemand3 = int(x['demand3'])
        inputNumPermanent3 = int(x['numPermanent3'])
        inputProdPermanent3 = int(x['prodPermanent3'])
        inputProdTemporary3 = int(x['prodTemporary3'])
        inputCostHiring3 = float(x['costHiring3'])
        inputCostFiring3 = float(x['costFiring3'])
        inputCostHoldingUnit3 = float(x['costHoldingUnit3'])
        
        inputDemand4 = int(x['demand4'])
        inputNumPermanent4 = int(x['numPermanent4'])
        inputProdPermanent4 = int(x['prodPermanent4'])
        inputProdTemporary4 = int(x['prodTemporary4'])
        inputCostHiring4 = float(x['costHiring4'])
        inputCostFiring4 = float(x['costFiring4'])
        inputCostHoldingUnit4 = float(x['costHoldingUnit4'])
        
        inputDemand5 = int(x['demand5'])
        inputNumPermanent5 = int(x['numPermanent5'])
        inputProdPermanent5 = int(x['prodPermanent5'])
        inputProdTemporary5 = int(x['prodTemporary5'])
        inputCostHiring5 = float(x['costHiring5'])
        inputCostFiring5 = float(x['costFiring5'])
        inputCostHoldingUnit5 = float(x['costHoldingUnit5'])
        
        inputDemand6 = int(x['demand6'])
        inputNumPermanent6 = int(x['numPermanent6'])
        inputProdPermanent6 = int(x['prodPermanent6'])
        inputProdTemporary6 = int(x['prodTemporary6'])
        inputCostHiring6 = float(x['costHiring6'])
        inputCostFiring6 = float(x['costFiring6'])
        inputCostHoldingUnit6 = float(x['costHoldingUnit6'])
        
        inputDemand7 = int(x['demand7'])
        inputNumPermanent7 = int(x['numPermanent7'])
        inputProdPermanent7 = int(x['prodPermanent7'])
        inputProdTemporary7 = int(x['prodTemporary7'])
        inputCostHiring7 = float(x['costHiring7'])
        inputCostFiring7 = float(x['costFiring7'])
        inputCostHoldingUnit7 = float(x['costHoldingUnit7'])
        
        inputDemand8 = int(x['demand8'])
        inputNumPermanent8 = int(x['numPermanent8'])
        inputProdPermanent8 = int(x['prodPermanent8'])
        inputProdTemporary8 = int(x['prodTemporary8'])
        inputCostHiring8 = float(x['costHiring8'])
        inputCostFiring8 = float(x['costFiring8'])
        inputCostHoldingUnit8 = float(x['costHoldingUnit8'])
        
        inputDemand9 = int(x['demand9'])
        inputNumPermanent9 = int(x['numPermanent9'])
        inputProdPermanent9 = int(x['prodPermanent9'])
        inputProdTemporary9 = int(x['prodTemporary9'])
        inputCostHiring9 = float(x['costHiring9'])
        inputCostFiring9 = float(x['costFiring9'])
        inputCostHoldingUnit9 = float(x['costHoldingUnit9'])
    model = LpProblem("Minimize Cost", LpMinimize)
    month = list(range(9))
    ihcDict = LpVariable.dicts(
        'IHC', month, lowBound=0, cat='Continuous')
    ihcDict[8] = inputInventoryFinal
    hcDict = LpVariable.dicts(
        'HC', month, lowBound=0, cat='Continuous')
    fcDict = LpVariable.dicts(
        'FC', month, lowBound=0, cat='Continuous')
    inputCostHoldingUnitDict = [inputCostHoldingUnit1, inputCostHoldingUnit2, inputCostHoldingUnit3, inputCostHoldingUnit4, inputCostHoldingUnit5, inputCostHoldingUnit6, inputCostHoldingUnit7, inputCostHoldingUnit8, inputCostHoldingUnit9]
    inputCostHiringDict = [inputCostHiring1, inputCostHiring2, inputCostHiring3, inputCostHiring4, inputCostHiring5, inputCostHiring6, inputCostHiring7, inputCostHiring8, inputCostHiring9]
    inputCostFiringDict = [inputCostFiring1, inputCostFiring2, inputCostFiring3, inputCostFiring4, inputCostFiring5, inputCostFiring6, inputCostFiring7, inputCostFiring8, inputCostFiring9]
    model += lpSum([inputCostHoldingUnitDict[i] * ihcDict[i] for i in month]) + lpSum([inputCostHiringDict[i] * hcDict[i] for i in month]) + lpSum([inputCostFiringDict[i] * fcDict[i] for i in month])
    model.addConstraint(inputInventoryInitial + inputProdTemporary1 * hcDict[0] - inputProdTemporary1 * fcDict[0] - ihcDict[0] == inputDemand1 - (inputNumPermanent1 * inputProdPermanent1))
    model.addConstraint(ihcDict[0] + inputProdTemporary2 * hcDict[0] - inputProdTemporary2*fcDict[0] + inputProdTemporary2*hcDict[1] - inputProdTemporary2*fcDict[1] - ihcDict[1] == inputDemand2 - (inputNumPermanent2 * inputProdPermanent2))
    model.addConstraint(ihcDict[1] + inputProdTemporary3 * hcDict[0] - inputProdTemporary3*fcDict[0] + inputProdTemporary3*hcDict[1] - inputProdTemporary3*fcDict[1] + inputProdTemporary3*hcDict[2] - inputProdTemporary3*fcDict[2] - ihcDict[2] == inputDemand3 - (inputNumPermanent3 * inputProdPermanent3))
    model.addConstraint(ihcDict[2] + inputProdTemporary4 * hcDict[0] - inputProdTemporary4*fcDict[0] + inputProdTemporary4*hcDict[1] - inputProdTemporary4*fcDict[1] + inputProdTemporary4*hcDict[2] - inputProdTemporary4*fcDict[2] + inputProdTemporary4*hcDict[3] - inputProdTemporary4*fcDict[3] - ihcDict[3] == inputDemand4 - (inputNumPermanent4 * inputProdPermanent4))
    model.addConstraint(ihcDict[3] + inputProdTemporary5 * hcDict[0] - inputProdTemporary5*fcDict[0] + inputProdTemporary5*hcDict[1] - inputProdTemporary5*fcDict[1] + inputProdTemporary5*hcDict[2] - inputProdTemporary5*fcDict[2] + inputProdTemporary5*hcDict[3] - inputProdTemporary5*fcDict[3] + inputProdTemporary5*hcDict[4] - inputProdTemporary5*fcDict[4] - ihcDict[4] == inputDemand5 - (inputNumPermanent5 * inputProdPermanent5))
    model.addConstraint(ihcDict[4] + inputProdTemporary6 * hcDict[0] - inputProdTemporary6*fcDict[0] + inputProdTemporary6*hcDict[1] - inputProdTemporary6*fcDict[1] + inputProdTemporary6*hcDict[2] - inputProdTemporary6*fcDict[2] + inputProdTemporary6*hcDict[3] - inputProdTemporary6*fcDict[3] + inputProdTemporary6*hcDict[4] - inputProdTemporary6*fcDict[4] + inputProdTemporary6*hcDict[5] - inputProdTemporary6*fcDict[5] - ihcDict[5] == inputDemand6 - (inputNumPermanent6 * inputProdPermanent6))
    model.addConstraint(ihcDict[5] + inputProdTemporary7 * hcDict[0] - inputProdTemporary7*fcDict[0] + inputProdTemporary7*hcDict[1] - inputProdTemporary7*fcDict[1] + inputProdTemporary7*hcDict[2] - inputProdTemporary7*fcDict[2] + inputProdTemporary7*hcDict[3] - inputProdTemporary7*fcDict[3] + inputProdTemporary7*hcDict[4] - inputProdTemporary7*fcDict[4] + inputProdTemporary7*hcDict[5] - inputProdTemporary7*fcDict[5] + inputProdTemporary7*hcDict[6] - inputProdTemporary7*fcDict[6] - ihcDict[6] == inputDemand7 - (inputNumPermanent7 * inputProdPermanent7))
    model.addConstraint(ihcDict[6] + inputProdTemporary8 * hcDict[0] - inputProdTemporary8*fcDict[0] + inputProdTemporary8*hcDict[1] - inputProdTemporary8*fcDict[1] + inputProdTemporary8*hcDict[2] - inputProdTemporary8*fcDict[2] + inputProdTemporary8*hcDict[3] - inputProdTemporary8*fcDict[3] + inputProdTemporary8*hcDict[4] - inputProdTemporary8*fcDict[4] + inputProdTemporary8*hcDict[5] - inputProdTemporary8*fcDict[5] + inputProdTemporary8*hcDict[6] - inputProdTemporary8*fcDict[6] + inputProdTemporary8*hcDict[7] - inputProdTemporary8*fcDict[7] - ihcDict[7] == inputDemand8 - (inputNumPermanent8 * inputProdPermanent8))
    model.addConstraint(ihcDict[7] + inputProdTemporary9 * hcDict[0] - inputProdTemporary9*fcDict[0] + inputProdTemporary9*hcDict[1] - inputProdTemporary9*fcDict[1] + inputProdTemporary9*hcDict[2] - inputProdTemporary9*fcDict[2] + inputProdTemporary9*hcDict[3] - inputProdTemporary9*fcDict[3] + inputProdTemporary9*hcDict[4] - inputProdTemporary9*fcDict[4] + inputProdTemporary9*hcDict[5] - inputProdTemporary9*fcDict[5] + inputProdTemporary9*hcDict[6] - inputProdTemporary9*fcDict[6] + inputProdTemporary9*hcDict[7] - inputProdTemporary9*fcDict[7] + inputProdTemporary9*hcDict[8] - inputProdTemporary9*fcDict[8] - ihcDict[8] == inputDemand9 - (inputNumPermanent9 * inputProdPermanent9))
    model.solve()
    models.NineMonthPlan.objects.filter(planName = inputPlanName).update(inventoryInitial = inputInventoryInitial, inventoryFinal = inputInventoryFinal,inventoryMonth1 = ihcDict[0].varValue, inventoryMonth2 = ihcDict[1].varValue, inventoryMonth3 = ihcDict[2].varValue, inventoryMonth4 = ihcDict[3].varValue, inventoryMonth5 = ihcDict[4].varValue, inventoryMonth6 = ihcDict[5].varValue, inventoryMonth7 = ihcDict[6].varValue, inventoryMonth8 = ihcDict[7].varValue, hiredTemporary1 = hcDict[0].varValue, hiredTemporary2 = hcDict[1].varValue, hiredTemporary3 = hcDict[2].varValue, hiredTemporary4 = hcDict[3].varValue, hiredTemporary5 = hcDict[4].varValue, hiredTemporary6 = hcDict[5].varValue, hiredTemporary7 = hcDict[6].varValue, hiredTemporary8 = hcDict[7].varValue, hiredTemporary9 = hcDict[8].varValue, firedTemporary1 = fcDict[0].varValue, firedTemporary2 = fcDict[1].varValue, firedTemporary3 = fcDict[2].varValue, firedTemporary4 = fcDict[3].varValue, firedTemporary5 = fcDict[4].varValue, firedTemporary6 = fcDict[5].varValue, firedTemporary7 = fcDict[6].varValue, firedTemporary8 = fcDict[7].varValue, firedTemporary9 = fcDict[8].varValue, optimalCost = value(model.objective))


def optimizeTen(inputPlanName):
    qs = models.TenMonthPlan.objects.filter(planName=inputPlanName).values()
    for x in qs:
        inputInventoryInitial = int(x['inventoryInitial'])
        inputInventoryFinal = x['inventoryFinal']
        
        inputDemand1 = int(x['demand1'])
        inputNumPermanent1 = int(x['numPermanent1'])
        inputProdPermanent1 = int(x['prodPermanent1'])
        inputProdTemporary1 = int(x['prodTemporary1'])
        inputCostHiring1 = float(x['costHiring1'])
        inputCostFiring1 = float(x['costFiring1'])
        inputCostHoldingUnit1 = float(x['costHoldingUnit1'])
        
        inputDemand2 = int(x['demand2'])
        inputNumPermanent2 = int(x['numPermanent2'])
        inputProdPermanent2 = int(x['prodPermanent2'])
        inputProdTemporary2 = int(x['prodTemporary2'])
        inputCostHiring2 = float(x['costHiring2'])
        inputCostFiring2 = float(x['costFiring2'])
        inputCostHoldingUnit2 = float(x['costHoldingUnit2'])
        
        inputDemand3 = int(x['demand3'])
        inputNumPermanent3 = int(x['numPermanent3'])
        inputProdPermanent3 = int(x['prodPermanent3'])
        inputProdTemporary3 = int(x['prodTemporary3'])
        inputCostHiring3 = float(x['costHiring3'])
        inputCostFiring3 = float(x['costFiring3'])
        inputCostHoldingUnit3 = float(x['costHoldingUnit3'])
        
        inputDemand4 = int(x['demand4'])
        inputNumPermanent4 = int(x['numPermanent4'])
        inputProdPermanent4 = int(x['prodPermanent4'])
        inputProdTemporary4 = int(x['prodTemporary4'])
        inputCostHiring4 = float(x['costHiring4'])
        inputCostFiring4 = float(x['costFiring4'])
        inputCostHoldingUnit4 = float(x['costHoldingUnit4'])
        
        inputDemand5 = int(x['demand5'])
        inputNumPermanent5 = int(x['numPermanent5'])
        inputProdPermanent5 = int(x['prodPermanent5'])
        inputProdTemporary5 = int(x['prodTemporary5'])
        inputCostHiring5 = float(x['costHiring5'])
        inputCostFiring5 = float(x['costFiring5'])
        inputCostHoldingUnit5 = float(x['costHoldingUnit5'])
        
        inputDemand6 = int(x['demand6'])
        inputNumPermanent6 = int(x['numPermanent6'])
        inputProdPermanent6 = int(x['prodPermanent6'])
        inputProdTemporary6 = int(x['prodTemporary6'])
        inputCostHiring6 = float(x['costHiring6'])
        inputCostFiring6 = float(x['costFiring6'])
        inputCostHoldingUnit6 = float(x['costHoldingUnit6'])
        
        inputDemand7 = int(x['demand7'])
        inputNumPermanent7 = int(x['numPermanent7'])
        inputProdPermanent7 = int(x['prodPermanent7'])
        inputProdTemporary7 = int(x['prodTemporary7'])
        inputCostHiring7 = float(x['costHiring7'])
        inputCostFiring7 = float(x['costFiring7'])
        inputCostHoldingUnit7 = float(x['costHoldingUnit7'])
        
        inputDemand8 = int(x['demand8'])
        inputNumPermanent8 = int(x['numPermanent8'])
        inputProdPermanent8 = int(x['prodPermanent8'])
        inputProdTemporary8 = int(x['prodTemporary8'])
        inputCostHiring8 = float(x['costHiring8'])
        inputCostFiring8 = float(x['costFiring8'])
        inputCostHoldingUnit8 = float(x['costHoldingUnit8'])
        
        inputDemand9 = int(x['demand9'])
        inputNumPermanent9 = int(x['numPermanent9'])
        inputProdPermanent9 = int(x['prodPermanent9'])
        inputProdTemporary9 = int(x['prodTemporary9'])
        inputCostHiring9 = float(x['costHiring9'])
        inputCostFiring9 = float(x['costFiring9'])
        inputCostHoldingUnit9 = float(x['costHoldingUnit9'])
        
        inputDemand10 = int(x['demand10'])
        inputNumPermanent10 = int(x['numPermanent10'])
        inputProdPermanent10 = int(x['prodPermanent10'])
        inputProdTemporary10 = int(x['prodTemporary10'])
        inputCostHiring10 = float(x['costHiring10'])
        inputCostFiring10 = float(x['costFiring10'])
        inputCostHoldingUnit10 = float(x['costHoldingUnit10'])
    model = LpProblem("Minimize Cost", LpMinimize)
    month = list(range(10))
    ihcDict = LpVariable.dicts(
        'IHC', month, lowBound=0, cat='Continuous')
    ihcDict[9] = inputInventoryFinal
    hcDict = LpVariable.dicts(
        'HC', month, lowBound=0, cat='Continuous')
    fcDict = LpVariable.dicts(
        'FC', month, lowBound=0, cat='Continuous')
    inputCostHoldingUnitDict = [inputCostHoldingUnit1, inputCostHoldingUnit2, inputCostHoldingUnit3, inputCostHoldingUnit4, inputCostHoldingUnit5, inputCostHoldingUnit6, inputCostHoldingUnit7, inputCostHoldingUnit8, inputCostHoldingUnit9, inputCostHoldingUnit10]
    inputCostHiringDict = [inputCostHiring1, inputCostHiring2, inputCostHiring3, inputCostHiring4, inputCostHiring5, inputCostHiring6, inputCostHiring7, inputCostHiring8, inputCostHiring9, inputCostHiring10]
    inputCostFiringDict = [inputCostFiring1, inputCostFiring2, inputCostFiring3, inputCostFiring4, inputCostFiring5, inputCostFiring6, inputCostFiring7, inputCostFiring8, inputCostFiring9, inputCostFiring10]
    model += lpSum([inputCostHoldingUnitDict[i] * ihcDict[i] for i in month]) + lpSum([inputCostHiringDict[i] * hcDict[i] for i in month]) + lpSum([inputCostFiringDict[i] * fcDict[i] for i in month])
    model.addConstraint(inputInventoryInitial + inputProdTemporary1 * hcDict[0] - inputProdTemporary1 * fcDict[0] - ihcDict[0] == inputDemand1 - (inputNumPermanent1 * inputProdPermanent1))
    model.addConstraint(ihcDict[0] + inputProdTemporary2 * hcDict[0] - inputProdTemporary2*fcDict[0] + inputProdTemporary2*hcDict[1] - inputProdTemporary2*fcDict[1] - ihcDict[1] == inputDemand2 - (inputNumPermanent2 * inputProdPermanent2))
    model.addConstraint(ihcDict[1] + inputProdTemporary3 * hcDict[0] - inputProdTemporary3*fcDict[0] + inputProdTemporary3*hcDict[1] - inputProdTemporary3*fcDict[1] + inputProdTemporary3*hcDict[2] - inputProdTemporary3*fcDict[2] - ihcDict[2] == inputDemand3 - (inputNumPermanent3 * inputProdPermanent3))
    model.addConstraint(ihcDict[2] + inputProdTemporary4 * hcDict[0] - inputProdTemporary4*fcDict[0] + inputProdTemporary4*hcDict[1] - inputProdTemporary4*fcDict[1] + inputProdTemporary4*hcDict[2] - inputProdTemporary4*fcDict[2] + inputProdTemporary4*hcDict[3] - inputProdTemporary4*fcDict[3] - ihcDict[3] == inputDemand4 - (inputNumPermanent4 * inputProdPermanent4))
    model.addConstraint(ihcDict[3] + inputProdTemporary5 * hcDict[0] - inputProdTemporary5*fcDict[0] + inputProdTemporary5*hcDict[1] - inputProdTemporary5*fcDict[1] + inputProdTemporary5*hcDict[2] - inputProdTemporary5*fcDict[2] + inputProdTemporary5*hcDict[3] - inputProdTemporary5*fcDict[3] + inputProdTemporary5*hcDict[4] - inputProdTemporary5*fcDict[4] - ihcDict[4] == inputDemand5 - (inputNumPermanent5 * inputProdPermanent5))
    model.addConstraint(ihcDict[4] + inputProdTemporary6 * hcDict[0] - inputProdTemporary6*fcDict[0] + inputProdTemporary6*hcDict[1] - inputProdTemporary6*fcDict[1] + inputProdTemporary6*hcDict[2] - inputProdTemporary6*fcDict[2] + inputProdTemporary6*hcDict[3] - inputProdTemporary6*fcDict[3] + inputProdTemporary6*hcDict[4] - inputProdTemporary6*fcDict[4] + inputProdTemporary6*hcDict[5] - inputProdTemporary6*fcDict[5] - ihcDict[5] == inputDemand6 - (inputNumPermanent6 * inputProdPermanent6))
    model.addConstraint(ihcDict[5] + inputProdTemporary7 * hcDict[0] - inputProdTemporary7*fcDict[0] + inputProdTemporary7*hcDict[1] - inputProdTemporary7*fcDict[1] + inputProdTemporary7*hcDict[2] - inputProdTemporary7*fcDict[2] + inputProdTemporary7*hcDict[3] - inputProdTemporary7*fcDict[3] + inputProdTemporary7*hcDict[4] - inputProdTemporary7*fcDict[4] + inputProdTemporary7*hcDict[5] - inputProdTemporary7*fcDict[5] + inputProdTemporary7*hcDict[6] - inputProdTemporary7*fcDict[6] - ihcDict[6] == inputDemand7 - (inputNumPermanent7 * inputProdPermanent7))
    model.addConstraint(ihcDict[6] + inputProdTemporary8 * hcDict[0] - inputProdTemporary8*fcDict[0] + inputProdTemporary8*hcDict[1] - inputProdTemporary8*fcDict[1] + inputProdTemporary8*hcDict[2] - inputProdTemporary8*fcDict[2] + inputProdTemporary8*hcDict[3] - inputProdTemporary8*fcDict[3] + inputProdTemporary8*hcDict[4] - inputProdTemporary8*fcDict[4] + inputProdTemporary8*hcDict[5] - inputProdTemporary8*fcDict[5] + inputProdTemporary8*hcDict[6] - inputProdTemporary8*fcDict[6] + inputProdTemporary8*hcDict[7] - inputProdTemporary8*fcDict[7] - ihcDict[7] == inputDemand8 - (inputNumPermanent8 * inputProdPermanent8))
    model.addConstraint(ihcDict[7] + inputProdTemporary9 * hcDict[0] - inputProdTemporary9*fcDict[0] + inputProdTemporary9*hcDict[1] - inputProdTemporary9*fcDict[1] + inputProdTemporary9*hcDict[2] - inputProdTemporary9*fcDict[2] + inputProdTemporary9*hcDict[3] - inputProdTemporary9*fcDict[3] + inputProdTemporary9*hcDict[4] - inputProdTemporary9*fcDict[4] + inputProdTemporary9*hcDict[5] - inputProdTemporary9*fcDict[5] + inputProdTemporary9*hcDict[6] - inputProdTemporary9*fcDict[6] + inputProdTemporary9*hcDict[7] - inputProdTemporary9*fcDict[7] + inputProdTemporary9*hcDict[8] - inputProdTemporary9*fcDict[8] - ihcDict[8] == inputDemand9 - (inputNumPermanent9 * inputProdPermanent9))
    model.addConstraint(ihcDict[8] + inputProdTemporary10 * hcDict[0] - inputProdTemporary10*fcDict[0] + inputProdTemporary10*hcDict[1] - inputProdTemporary10*fcDict[1] + inputProdTemporary10*hcDict[2] - inputProdTemporary10*fcDict[2] + inputProdTemporary10*hcDict[3] - inputProdTemporary10*fcDict[3] + inputProdTemporary10*hcDict[4] - inputProdTemporary10*fcDict[4] + inputProdTemporary10*hcDict[5] - inputProdTemporary10*fcDict[5] + inputProdTemporary10*hcDict[6] - inputProdTemporary10*fcDict[6] + inputProdTemporary10*hcDict[7] - inputProdTemporary10*fcDict[7] + inputProdTemporary10*hcDict[8] - inputProdTemporary10*fcDict[8] + inputProdTemporary10*hcDict[9] - inputProdTemporary10*fcDict[9] - ihcDict[9] == inputDemand10 - (inputNumPermanent10 * inputProdPermanent10))
    model.solve()
    models.TenMonthPlan.objects.filter(planName = inputPlanName).update(inventoryInitial = inputInventoryInitial, inventoryFinal = inputInventoryFinal,inventoryMonth1 = ihcDict[0].varValue, inventoryMonth2 = ihcDict[1].varValue, inventoryMonth3 = ihcDict[2].varValue, inventoryMonth4 = ihcDict[3].varValue, inventoryMonth5 = ihcDict[4].varValue, inventoryMonth6 = ihcDict[5].varValue, inventoryMonth7 = ihcDict[6].varValue, inventoryMonth8 = ihcDict[7].varValue, inventoryMonth9 = ihcDict[8].varValue, hiredTemporary1 = hcDict[0].varValue, hiredTemporary2 = hcDict[1].varValue, hiredTemporary3 = hcDict[2].varValue, hiredTemporary4 = hcDict[3].varValue, hiredTemporary5 = hcDict[4].varValue, hiredTemporary6 = hcDict[5].varValue, hiredTemporary7 = hcDict[6].varValue, hiredTemporary8 = hcDict[7].varValue, hiredTemporary9 = hcDict[8].varValue, hiredTemporary10 = hcDict[9].varValue, firedTemporary1 = fcDict[0].varValue, firedTemporary2 = fcDict[1].varValue, firedTemporary3 = fcDict[2].varValue, firedTemporary4 = fcDict[3].varValue, firedTemporary5 = fcDict[4].varValue, firedTemporary6 = fcDict[5].varValue, firedTemporary7 = fcDict[6].varValue, firedTemporary8 = fcDict[7].varValue, firedTemporary9 = fcDict[8].varValue, firedTemporary10 = fcDict[9].varValue, optimalCost = value(model.objective))


def optimizeEleven(inputPlanName):
    qs = models.ElevenMonthPlan.objects.filter(planName=inputPlanName).values()
    for x in qs:
        inputInventoryInitial = int(x['inventoryInitial'])
        inputInventoryFinal = x['inventoryFinal']
        
        inputDemand1 = int(x['demand1'])
        inputNumPermanent1 = int(x['numPermanent1'])
        inputProdPermanent1 = int(x['prodPermanent1'])
        inputProdTemporary1 = int(x['prodTemporary1'])
        inputCostHiring1 = float(x['costHiring1'])
        inputCostFiring1 = float(x['costFiring1'])
        inputCostHoldingUnit1 = float(x['costHoldingUnit1'])
        
        inputDemand2 = int(x['demand2'])
        inputNumPermanent2 = int(x['numPermanent2'])
        inputProdPermanent2 = int(x['prodPermanent2'])
        inputProdTemporary2 = int(x['prodTemporary2'])
        inputCostHiring2 = float(x['costHiring2'])
        inputCostFiring2 = float(x['costFiring2'])
        inputCostHoldingUnit2 = float(x['costHoldingUnit2'])
        
        inputDemand3 = int(x['demand3'])
        inputNumPermanent3 = int(x['numPermanent3'])
        inputProdPermanent3 = int(x['prodPermanent3'])
        inputProdTemporary3 = int(x['prodTemporary3'])
        inputCostHiring3 = float(x['costHiring3'])
        inputCostFiring3 = float(x['costFiring3'])
        inputCostHoldingUnit3 = float(x['costHoldingUnit3'])
        
        inputDemand4 = int(x['demand4'])
        inputNumPermanent4 = int(x['numPermanent4'])
        inputProdPermanent4 = int(x['prodPermanent4'])
        inputProdTemporary4 = int(x['prodTemporary4'])
        inputCostHiring4 = float(x['costHiring4'])
        inputCostFiring4 = float(x['costFiring4'])
        inputCostHoldingUnit4 = float(x['costHoldingUnit4'])
        
        inputDemand5 = int(x['demand5'])
        inputNumPermanent5 = int(x['numPermanent5'])
        inputProdPermanent5 = int(x['prodPermanent5'])
        inputProdTemporary5 = int(x['prodTemporary5'])
        inputCostHiring5 = float(x['costHiring5'])
        inputCostFiring5 = float(x['costFiring5'])
        inputCostHoldingUnit5 = float(x['costHoldingUnit5'])
        
        inputDemand6 = int(x['demand6'])
        inputNumPermanent6 = int(x['numPermanent6'])
        inputProdPermanent6 = int(x['prodPermanent6'])
        inputProdTemporary6 = int(x['prodTemporary6'])
        inputCostHiring6 = float(x['costHiring6'])
        inputCostFiring6 = float(x['costFiring6'])
        inputCostHoldingUnit6 = float(x['costHoldingUnit6'])
        
        inputDemand7 = int(x['demand7'])
        inputNumPermanent7 = int(x['numPermanent7'])
        inputProdPermanent7 = int(x['prodPermanent7'])
        inputProdTemporary7 = int(x['prodTemporary7'])
        inputCostHiring7 = float(x['costHiring7'])
        inputCostFiring7 = float(x['costFiring7'])
        inputCostHoldingUnit7 = float(x['costHoldingUnit7'])
        
        inputDemand8 = int(x['demand8'])
        inputNumPermanent8 = int(x['numPermanent8'])
        inputProdPermanent8 = int(x['prodPermanent8'])
        inputProdTemporary8 = int(x['prodTemporary8'])
        inputCostHiring8 = float(x['costHiring8'])
        inputCostFiring8 = float(x['costFiring8'])
        inputCostHoldingUnit8 = float(x['costHoldingUnit8'])
        
        inputDemand9 = int(x['demand9'])
        inputNumPermanent9 = int(x['numPermanent9'])
        inputProdPermanent9 = int(x['prodPermanent9'])
        inputProdTemporary9 = int(x['prodTemporary9'])
        inputCostHiring9 = float(x['costHiring9'])
        inputCostFiring9 = float(x['costFiring9'])
        inputCostHoldingUnit9 = float(x['costHoldingUnit9'])
        
        inputDemand10 = int(x['demand10'])
        inputNumPermanent10 = int(x['numPermanent10'])
        inputProdPermanent10 = int(x['prodPermanent10'])
        inputProdTemporary10 = int(x['prodTemporary10'])
        inputCostHiring10 = float(x['costHiring10'])
        inputCostFiring10 = float(x['costFiring10'])
        inputCostHoldingUnit10 = float(x['costHoldingUnit10'])
        
        inputDemand11 = int(x['demand11'])
        inputNumPermanent11 = int(x['numPermanent11'])
        inputProdPermanent11 = int(x['prodPermanent11'])
        inputProdTemporary11 = int(x['prodTemporary11'])
        inputCostHiring11 = float(x['costHiring11'])
        inputCostFiring11 = float(x['costFiring11'])
        inputCostHoldingUnit11 = float(x['costHoldingUnit11'])
    model = LpProblem("Minimize Cost", LpMinimize)
    month = list(range(11))
    ihcDict = LpVariable.dicts(
        'IHC', month, lowBound=0, cat='Continuous')
    ihcDict[10] = inputInventoryFinal
    hcDict = LpVariable.dicts(
        'HC', month, lowBound=0, cat='Continuous')
    fcDict = LpVariable.dicts(
        'FC', month, lowBound=0, cat='Continuous')
    inputCostHoldingUnitDict = [inputCostHoldingUnit1, inputCostHoldingUnit2, inputCostHoldingUnit3, inputCostHoldingUnit4, inputCostHoldingUnit5, inputCostHoldingUnit6, inputCostHoldingUnit7, inputCostHoldingUnit8, inputCostHoldingUnit9, inputCostHoldingUnit10, inputCostHoldingUnit11]
    inputCostHiringDict = [inputCostHiring1, inputCostHiring2, inputCostHiring3, inputCostHiring4, inputCostHiring5, inputCostHiring6, inputCostHiring7, inputCostHiring8, inputCostHiring9, inputCostHiring10, inputCostHiring11]
    inputCostFiringDict = [inputCostFiring1, inputCostFiring2, inputCostFiring3, inputCostFiring4, inputCostFiring5, inputCostFiring6, inputCostFiring7, inputCostFiring8, inputCostFiring9, inputCostFiring10, inputCostFiring11]
    model += lpSum([inputCostHoldingUnitDict[i] * ihcDict[i] for i in month]) + lpSum([inputCostHiringDict[i] * hcDict[i] for i in month]) + lpSum([inputCostFiringDict[i] * fcDict[i] for i in month])
    model.addConstraint(inputInventoryInitial + inputProdTemporary1 * hcDict[0] - inputProdTemporary1 * fcDict[0] - ihcDict[0] == inputDemand1 - (inputNumPermanent1 * inputProdPermanent1))
    model.addConstraint(ihcDict[0] + inputProdTemporary2 * hcDict[0] - inputProdTemporary2*fcDict[0] + inputProdTemporary2*hcDict[1] - inputProdTemporary2*fcDict[1] - ihcDict[1] == inputDemand2 - (inputNumPermanent2 * inputProdPermanent2))
    model.addConstraint(ihcDict[1] + inputProdTemporary3 * hcDict[0] - inputProdTemporary3*fcDict[0] + inputProdTemporary3*hcDict[1] - inputProdTemporary3*fcDict[1] + inputProdTemporary3*hcDict[2] - inputProdTemporary3*fcDict[2] - ihcDict[2] == inputDemand3 - (inputNumPermanent3 * inputProdPermanent3))
    model.addConstraint(ihcDict[2] + inputProdTemporary4 * hcDict[0] - inputProdTemporary4*fcDict[0] + inputProdTemporary4*hcDict[1] - inputProdTemporary4*fcDict[1] + inputProdTemporary4*hcDict[2] - inputProdTemporary4*fcDict[2] + inputProdTemporary4*hcDict[3] - inputProdTemporary4*fcDict[3] - ihcDict[3] == inputDemand4 - (inputNumPermanent4 * inputProdPermanent4))
    model.addConstraint(ihcDict[3] + inputProdTemporary5 * hcDict[0] - inputProdTemporary5*fcDict[0] + inputProdTemporary5*hcDict[1] - inputProdTemporary5*fcDict[1] + inputProdTemporary5*hcDict[2] - inputProdTemporary5*fcDict[2] + inputProdTemporary5*hcDict[3] - inputProdTemporary5*fcDict[3] + inputProdTemporary5*hcDict[4] - inputProdTemporary5*fcDict[4] - ihcDict[4] == inputDemand5 - (inputNumPermanent5 * inputProdPermanent5))
    model.addConstraint(ihcDict[4] + inputProdTemporary6 * hcDict[0] - inputProdTemporary6*fcDict[0] + inputProdTemporary6*hcDict[1] - inputProdTemporary6*fcDict[1] + inputProdTemporary6*hcDict[2] - inputProdTemporary6*fcDict[2] + inputProdTemporary6*hcDict[3] - inputProdTemporary6*fcDict[3] + inputProdTemporary6*hcDict[4] - inputProdTemporary6*fcDict[4] + inputProdTemporary6*hcDict[5] - inputProdTemporary6*fcDict[5] - ihcDict[5] == inputDemand6 - (inputNumPermanent6 * inputProdPermanent6))
    model.addConstraint(ihcDict[5] + inputProdTemporary7 * hcDict[0] - inputProdTemporary7*fcDict[0] + inputProdTemporary7*hcDict[1] - inputProdTemporary7*fcDict[1] + inputProdTemporary7*hcDict[2] - inputProdTemporary7*fcDict[2] + inputProdTemporary7*hcDict[3] - inputProdTemporary7*fcDict[3] + inputProdTemporary7*hcDict[4] - inputProdTemporary7*fcDict[4] + inputProdTemporary7*hcDict[5] - inputProdTemporary7*fcDict[5] + inputProdTemporary7*hcDict[6] - inputProdTemporary7*fcDict[6] - ihcDict[6] == inputDemand7 - (inputNumPermanent7 * inputProdPermanent7))
    model.addConstraint(ihcDict[6] + inputProdTemporary8 * hcDict[0] - inputProdTemporary8*fcDict[0] + inputProdTemporary8*hcDict[1] - inputProdTemporary8*fcDict[1] + inputProdTemporary8*hcDict[2] - inputProdTemporary8*fcDict[2] + inputProdTemporary8*hcDict[3] - inputProdTemporary8*fcDict[3] + inputProdTemporary8*hcDict[4] - inputProdTemporary8*fcDict[4] + inputProdTemporary8*hcDict[5] - inputProdTemporary8*fcDict[5] + inputProdTemporary8*hcDict[6] - inputProdTemporary8*fcDict[6] + inputProdTemporary8*hcDict[7] - inputProdTemporary8*fcDict[7] - ihcDict[7] == inputDemand8 - (inputNumPermanent8 * inputProdPermanent8))
    model.addConstraint(ihcDict[7] + inputProdTemporary9 * hcDict[0] - inputProdTemporary9*fcDict[0] + inputProdTemporary9*hcDict[1] - inputProdTemporary9*fcDict[1] + inputProdTemporary9*hcDict[2] - inputProdTemporary9*fcDict[2] + inputProdTemporary9*hcDict[3] - inputProdTemporary9*fcDict[3] + inputProdTemporary9*hcDict[4] - inputProdTemporary9*fcDict[4] + inputProdTemporary9*hcDict[5] - inputProdTemporary9*fcDict[5] + inputProdTemporary9*hcDict[6] - inputProdTemporary9*fcDict[6] + inputProdTemporary9*hcDict[7] - inputProdTemporary9*fcDict[7] + inputProdTemporary9*hcDict[8] - inputProdTemporary9*fcDict[8] - ihcDict[8] == inputDemand9 - (inputNumPermanent9 * inputProdPermanent9))
    model.addConstraint(ihcDict[8] + inputProdTemporary10 * hcDict[0] - inputProdTemporary10*fcDict[0] + inputProdTemporary10*hcDict[1] - inputProdTemporary10*fcDict[1] + inputProdTemporary10*hcDict[2] - inputProdTemporary10*fcDict[2] + inputProdTemporary10*hcDict[3] - inputProdTemporary10*fcDict[3] + inputProdTemporary10*hcDict[4] - inputProdTemporary10*fcDict[4] + inputProdTemporary10*hcDict[5] - inputProdTemporary10*fcDict[5] + inputProdTemporary10*hcDict[6] - inputProdTemporary10*fcDict[6] + inputProdTemporary10*hcDict[7] - inputProdTemporary10*fcDict[7] + inputProdTemporary10*hcDict[8] - inputProdTemporary10*fcDict[8] + inputProdTemporary10*hcDict[9] - inputProdTemporary10*fcDict[9] - ihcDict[9] == inputDemand10 - (inputNumPermanent10 * inputProdPermanent10))
    model.addConstraint(ihcDict[9] + inputProdTemporary11 * hcDict[0] - inputProdTemporary11*fcDict[0] + inputProdTemporary11*hcDict[1] - inputProdTemporary11*fcDict[1] + inputProdTemporary11*hcDict[2] - inputProdTemporary11*fcDict[2] + inputProdTemporary11*hcDict[3] - inputProdTemporary11*fcDict[3] + inputProdTemporary11*hcDict[4] - inputProdTemporary11*fcDict[4] + inputProdTemporary11*hcDict[5] - inputProdTemporary11*fcDict[5] + inputProdTemporary11*hcDict[6] - inputProdTemporary11*fcDict[6] + inputProdTemporary11*hcDict[7] - inputProdTemporary11*fcDict[7] + inputProdTemporary11*hcDict[8] - inputProdTemporary11*fcDict[8] + inputProdTemporary11*hcDict[9] - inputProdTemporary11*fcDict[9] + inputProdTemporary11*hcDict[10] - inputProdTemporary11*fcDict[10] - ihcDict[10] == inputDemand11 - (inputNumPermanent11 * inputProdPermanent11))
    model.solve()
    models.ElevenMonthPlan.objects.filter(planName = inputPlanName).update(inventoryInitial = inputInventoryInitial, inventoryFinal = inputInventoryFinal,inventoryMonth1 = ihcDict[0].varValue, inventoryMonth2 = ihcDict[1].varValue, inventoryMonth3 = ihcDict[2].varValue, inventoryMonth4 = ihcDict[3].varValue, inventoryMonth5 = ihcDict[4].varValue, inventoryMonth6 = ihcDict[5].varValue, inventoryMonth7 = ihcDict[6].varValue, inventoryMonth8 = ihcDict[7].varValue, inventoryMonth9 = ihcDict[8].varValue, inventoryMonth10 = ihcDict[9].varValue, hiredTemporary1 = hcDict[0].varValue, hiredTemporary2 = hcDict[1].varValue, hiredTemporary3 = hcDict[2].varValue, hiredTemporary4 = hcDict[3].varValue, hiredTemporary5 = hcDict[4].varValue, hiredTemporary6 = hcDict[5].varValue, hiredTemporary7 = hcDict[6].varValue, hiredTemporary8 = hcDict[7].varValue, hiredTemporary9 = hcDict[8].varValue, hiredTemporary10 = hcDict[9].varValue, hiredTemporary11 = hcDict[10].varValue, firedTemporary1 = fcDict[0].varValue, firedTemporary2 = fcDict[1].varValue, firedTemporary3 = fcDict[2].varValue, firedTemporary4 = fcDict[3].varValue, firedTemporary5 = fcDict[4].varValue, firedTemporary6 = fcDict[5].varValue, firedTemporary7 = fcDict[6].varValue, firedTemporary8 = fcDict[7].varValue, firedTemporary9 = fcDict[8].varValue, firedTemporary10 = fcDict[9].varValue, firedTemporary11 = fcDict[10].varValue, optimalCost = value(model.objective))


def optimizeTwelve(inputPlanName):
    qs = models.TwelveMonthPlan.objects.filter(planName=inputPlanName).values()
    for x in qs:
        inputInventoryInitial = int(x['inventoryInitial'])
        inputInventoryFinal = x['inventoryFinal']
        
        inputDemand1 = int(x['demand1'])
        inputNumPermanent1 = int(x['numPermanent1'])
        inputProdPermanent1 = int(x['prodPermanent1'])
        inputProdTemporary1 = int(x['prodTemporary1'])
        inputCostHiring1 = float(x['costHiring1'])
        inputCostFiring1 = float(x['costFiring1'])
        inputCostHoldingUnit1 = float(x['costHoldingUnit1'])
        
        inputDemand2 = int(x['demand2'])
        inputNumPermanent2 = int(x['numPermanent2'])
        inputProdPermanent2 = int(x['prodPermanent2'])
        inputProdTemporary2 = int(x['prodTemporary2'])
        inputCostHiring2 = float(x['costHiring2'])
        inputCostFiring2 = float(x['costFiring2'])
        inputCostHoldingUnit2 = float(x['costHoldingUnit2'])
        
        inputDemand3 = int(x['demand3'])
        inputNumPermanent3 = int(x['numPermanent3'])
        inputProdPermanent3 = int(x['prodPermanent3'])
        inputProdTemporary3 = int(x['prodTemporary3'])
        inputCostHiring3 = float(x['costHiring3'])
        inputCostFiring3 = float(x['costFiring3'])
        inputCostHoldingUnit3 = float(x['costHoldingUnit3'])
        
        inputDemand4 = int(x['demand4'])
        inputNumPermanent4 = int(x['numPermanent4'])
        inputProdPermanent4 = int(x['prodPermanent4'])
        inputProdTemporary4 = int(x['prodTemporary4'])
        inputCostHiring4 = float(x['costHiring4'])
        inputCostFiring4 = float(x['costFiring4'])
        inputCostHoldingUnit4 = float(x['costHoldingUnit4'])
        
        inputDemand5 = int(x['demand5'])
        inputNumPermanent5 = int(x['numPermanent5'])
        inputProdPermanent5 = int(x['prodPermanent5'])
        inputProdTemporary5 = int(x['prodTemporary5'])
        inputCostHiring5 = float(x['costHiring5'])
        inputCostFiring5 = float(x['costFiring5'])
        inputCostHoldingUnit5 = float(x['costHoldingUnit5'])
        
        inputDemand6 = int(x['demand6'])
        inputNumPermanent6 = int(x['numPermanent6'])
        inputProdPermanent6 = int(x['prodPermanent6'])
        inputProdTemporary6 = int(x['prodTemporary6'])
        inputCostHiring6 = float(x['costHiring6'])
        inputCostFiring6 = float(x['costFiring6'])
        inputCostHoldingUnit6 = float(x['costHoldingUnit6'])
        
        inputDemand7 = int(x['demand7'])
        inputNumPermanent7 = int(x['numPermanent7'])
        inputProdPermanent7 = int(x['prodPermanent7'])
        inputProdTemporary7 = int(x['prodTemporary7'])
        inputCostHiring7 = float(x['costHiring7'])
        inputCostFiring7 = float(x['costFiring7'])
        inputCostHoldingUnit7 = float(x['costHoldingUnit7'])
        
        inputDemand8 = int(x['demand8'])
        inputNumPermanent8 = int(x['numPermanent8'])
        inputProdPermanent8 = int(x['prodPermanent8'])
        inputProdTemporary8 = int(x['prodTemporary8'])
        inputCostHiring8 = float(x['costHiring8'])
        inputCostFiring8 = float(x['costFiring8'])
        inputCostHoldingUnit8 = float(x['costHoldingUnit8'])
        
        inputDemand9 = int(x['demand9'])
        inputNumPermanent9 = int(x['numPermanent9'])
        inputProdPermanent9 = int(x['prodPermanent9'])
        inputProdTemporary9 = int(x['prodTemporary9'])
        inputCostHiring9 = float(x['costHiring9'])
        inputCostFiring9 = float(x['costFiring9'])
        inputCostHoldingUnit9 = float(x['costHoldingUnit9'])
        
        inputDemand10 = int(x['demand10'])
        inputNumPermanent10 = int(x['numPermanent10'])
        inputProdPermanent10 = int(x['prodPermanent10'])
        inputProdTemporary10 = int(x['prodTemporary10'])
        inputCostHiring10 = float(x['costHiring10'])
        inputCostFiring10 = float(x['costFiring10'])
        inputCostHoldingUnit10 = float(x['costHoldingUnit10'])
        
        inputDemand11 = int(x['demand11'])
        inputNumPermanent11 = int(x['numPermanent11'])
        inputProdPermanent11 = int(x['prodPermanent11'])
        inputProdTemporary11 = int(x['prodTemporary11'])
        inputCostHiring11 = float(x['costHiring11'])
        inputCostFiring11 = float(x['costFiring11'])
        inputCostHoldingUnit11 = float(x['costHoldingUnit11'])
        
        inputDemand12 = int(x['demand12'])
        inputNumPermanent12 = int(x['numPermanent12'])
        inputProdPermanent12 = int(x['prodPermanent12'])
        inputProdTemporary12 = int(x['prodTemporary12'])
        inputCostHiring12 = float(x['costHiring12'])
        inputCostFiring12 = float(x['costFiring12'])
        inputCostHoldingUnit12 = float(x['costHoldingUnit12'])
    model = LpProblem("Minimize Cost", LpMinimize)
    month = list(range(12))
    ihcDict = LpVariable.dicts(
        'IHC', month, lowBound=0, cat='Continuous')
    ihcDict[11] = inputInventoryFinal
    hcDict = LpVariable.dicts(
        'HC', month, lowBound=0, cat='Continuous')
    fcDict = LpVariable.dicts(
        'FC', month, lowBound=0, cat='Continuous')
    inputCostHoldingUnitDict = [inputCostHoldingUnit1, inputCostHoldingUnit2, inputCostHoldingUnit3, inputCostHoldingUnit4, inputCostHoldingUnit5, inputCostHoldingUnit6, inputCostHoldingUnit7, inputCostHoldingUnit8, inputCostHoldingUnit9, inputCostHoldingUnit10, inputCostHoldingUnit11, inputCostHoldingUnit12]
    inputCostHiringDict = [inputCostHiring1, inputCostHiring2, inputCostHiring3, inputCostHiring4, inputCostHiring5, inputCostHiring6, inputCostHiring7, inputCostHiring8, inputCostHiring9, inputCostHiring10, inputCostHiring11, inputCostHiring12]
    inputCostFiringDict = [inputCostFiring1, inputCostFiring2, inputCostFiring3, inputCostFiring4, inputCostFiring5, inputCostFiring6, inputCostFiring7, inputCostFiring8, inputCostFiring9, inputCostFiring10, inputCostFiring11, inputCostFiring12]
    model += lpSum([inputCostHoldingUnitDict[i] * ihcDict[i] for i in month]) + lpSum([inputCostHiringDict[i] * hcDict[i] for i in month]) + lpSum([inputCostFiringDict[i] * fcDict[i] for i in month])
    model.addConstraint(inputInventoryInitial + inputProdTemporary1 * hcDict[0] - inputProdTemporary1 * fcDict[0] - ihcDict[0] == inputDemand1 - (inputNumPermanent1 * inputProdPermanent1))
    model.addConstraint(ihcDict[0] + inputProdTemporary2 * hcDict[0] - inputProdTemporary2*fcDict[0] + inputProdTemporary2*hcDict[1] - inputProdTemporary2*fcDict[1] - ihcDict[1] == inputDemand2 - (inputNumPermanent2 * inputProdPermanent2))
    model.addConstraint(ihcDict[1] + inputProdTemporary3 * hcDict[0] - inputProdTemporary3*fcDict[0] + inputProdTemporary3*hcDict[1] - inputProdTemporary3*fcDict[1] + inputProdTemporary3*hcDict[2] - inputProdTemporary3*fcDict[2] - ihcDict[2] == inputDemand3 - (inputNumPermanent3 * inputProdPermanent3))
    model.addConstraint(ihcDict[2] + inputProdTemporary4 * hcDict[0] - inputProdTemporary4*fcDict[0] + inputProdTemporary4*hcDict[1] - inputProdTemporary4*fcDict[1] + inputProdTemporary4*hcDict[2] - inputProdTemporary4*fcDict[2] + inputProdTemporary4*hcDict[3] - inputProdTemporary4*fcDict[3] - ihcDict[3] == inputDemand4 - (inputNumPermanent4 * inputProdPermanent4))
    model.addConstraint(ihcDict[3] + inputProdTemporary5 * hcDict[0] - inputProdTemporary5*fcDict[0] + inputProdTemporary5*hcDict[1] - inputProdTemporary5*fcDict[1] + inputProdTemporary5*hcDict[2] - inputProdTemporary5*fcDict[2] + inputProdTemporary5*hcDict[3] - inputProdTemporary5*fcDict[3] + inputProdTemporary5*hcDict[4] - inputProdTemporary5*fcDict[4] - ihcDict[4] == inputDemand5 - (inputNumPermanent5 * inputProdPermanent5))
    model.addConstraint(ihcDict[4] + inputProdTemporary6 * hcDict[0] - inputProdTemporary6*fcDict[0] + inputProdTemporary6*hcDict[1] - inputProdTemporary6*fcDict[1] + inputProdTemporary6*hcDict[2] - inputProdTemporary6*fcDict[2] + inputProdTemporary6*hcDict[3] - inputProdTemporary6*fcDict[3] + inputProdTemporary6*hcDict[4] - inputProdTemporary6*fcDict[4] + inputProdTemporary6*hcDict[5] - inputProdTemporary6*fcDict[5] - ihcDict[5] == inputDemand6 - (inputNumPermanent6 * inputProdPermanent6))
    model.addConstraint(ihcDict[5] + inputProdTemporary7 * hcDict[0] - inputProdTemporary7*fcDict[0] + inputProdTemporary7*hcDict[1] - inputProdTemporary7*fcDict[1] + inputProdTemporary7*hcDict[2] - inputProdTemporary7*fcDict[2] + inputProdTemporary7*hcDict[3] - inputProdTemporary7*fcDict[3] + inputProdTemporary7*hcDict[4] - inputProdTemporary7*fcDict[4] + inputProdTemporary7*hcDict[5] - inputProdTemporary7*fcDict[5] + inputProdTemporary7*hcDict[6] - inputProdTemporary7*fcDict[6] - ihcDict[6] == inputDemand7 - (inputNumPermanent7 * inputProdPermanent7))
    model.addConstraint(ihcDict[6] + inputProdTemporary8 * hcDict[0] - inputProdTemporary8*fcDict[0] + inputProdTemporary8*hcDict[1] - inputProdTemporary8*fcDict[1] + inputProdTemporary8*hcDict[2] - inputProdTemporary8*fcDict[2] + inputProdTemporary8*hcDict[3] - inputProdTemporary8*fcDict[3] + inputProdTemporary8*hcDict[4] - inputProdTemporary8*fcDict[4] + inputProdTemporary8*hcDict[5] - inputProdTemporary8*fcDict[5] + inputProdTemporary8*hcDict[6] - inputProdTemporary8*fcDict[6] + inputProdTemporary8*hcDict[7] - inputProdTemporary8*fcDict[7] - ihcDict[7] == inputDemand8 - (inputNumPermanent8 * inputProdPermanent8))
    model.addConstraint(ihcDict[7] + inputProdTemporary9 * hcDict[0] - inputProdTemporary9*fcDict[0] + inputProdTemporary9*hcDict[1] - inputProdTemporary9*fcDict[1] + inputProdTemporary9*hcDict[2] - inputProdTemporary9*fcDict[2] + inputProdTemporary9*hcDict[3] - inputProdTemporary9*fcDict[3] + inputProdTemporary9*hcDict[4] - inputProdTemporary9*fcDict[4] + inputProdTemporary9*hcDict[5] - inputProdTemporary9*fcDict[5] + inputProdTemporary9*hcDict[6] - inputProdTemporary9*fcDict[6] + inputProdTemporary9*hcDict[7] - inputProdTemporary9*fcDict[7] + inputProdTemporary9*hcDict[8] - inputProdTemporary9*fcDict[8] - ihcDict[8] == inputDemand9 - (inputNumPermanent9 * inputProdPermanent9))
    model.addConstraint(ihcDict[8] + inputProdTemporary10 * hcDict[0] - inputProdTemporary10*fcDict[0] + inputProdTemporary10*hcDict[1] - inputProdTemporary10*fcDict[1] + inputProdTemporary10*hcDict[2] - inputProdTemporary10*fcDict[2] + inputProdTemporary10*hcDict[3] - inputProdTemporary10*fcDict[3] + inputProdTemporary10*hcDict[4] - inputProdTemporary10*fcDict[4] + inputProdTemporary10*hcDict[5] - inputProdTemporary10*fcDict[5] + inputProdTemporary10*hcDict[6] - inputProdTemporary10*fcDict[6] + inputProdTemporary10*hcDict[7] - inputProdTemporary10*fcDict[7] + inputProdTemporary10*hcDict[8] - inputProdTemporary10*fcDict[8] + inputProdTemporary10*hcDict[9] - inputProdTemporary10*fcDict[9] - ihcDict[9] == inputDemand10 - (inputNumPermanent10 * inputProdPermanent10))
    model.addConstraint(ihcDict[9] + inputProdTemporary11 * hcDict[0] - inputProdTemporary11*fcDict[0] + inputProdTemporary11*hcDict[1] - inputProdTemporary11*fcDict[1] + inputProdTemporary11*hcDict[2] - inputProdTemporary11*fcDict[2] + inputProdTemporary11*hcDict[3] - inputProdTemporary11*fcDict[3] + inputProdTemporary11*hcDict[4] - inputProdTemporary11*fcDict[4] + inputProdTemporary11*hcDict[5] - inputProdTemporary11*fcDict[5] + inputProdTemporary11*hcDict[6] - inputProdTemporary11*fcDict[6] + inputProdTemporary11*hcDict[7] - inputProdTemporary11*fcDict[7] + inputProdTemporary11*hcDict[8] - inputProdTemporary11*fcDict[8] + inputProdTemporary11*hcDict[9] - inputProdTemporary11*fcDict[9] + inputProdTemporary11*hcDict[10] - inputProdTemporary11*fcDict[10] - ihcDict[10] == inputDemand11 - (inputNumPermanent11 * inputProdPermanent11))
    model.addConstraint(ihcDict[10] + inputProdTemporary12 * hcDict[0] - inputProdTemporary12*fcDict[0] + inputProdTemporary12*hcDict[1] - inputProdTemporary12*fcDict[1] + inputProdTemporary12*hcDict[2] - inputProdTemporary12*fcDict[2] + inputProdTemporary12*hcDict[3] - inputProdTemporary12*fcDict[3] + inputProdTemporary12*hcDict[4] - inputProdTemporary12*fcDict[4] + inputProdTemporary12*hcDict[5] - inputProdTemporary12*fcDict[5] + inputProdTemporary12*hcDict[6] - inputProdTemporary12*fcDict[6] + inputProdTemporary12*hcDict[7] - inputProdTemporary12*fcDict[7] + inputProdTemporary12*hcDict[8] - inputProdTemporary12*fcDict[8] + inputProdTemporary12*hcDict[9] - inputProdTemporary12*fcDict[9] + inputProdTemporary12*hcDict[10] - inputProdTemporary12*fcDict[10] + inputProdTemporary12*hcDict[11] - inputProdTemporary12*fcDict[11] - ihcDict[11] == inputDemand12 - (inputNumPermanent12 * inputProdPermanent12))
    model.solve()
    models.TwelveMonthPlan.objects.filter(planName = inputPlanName).update(inventoryInitial = inputInventoryInitial, inventoryFinal = inputInventoryFinal,inventoryMonth1 = ihcDict[0].varValue, inventoryMonth2 = ihcDict[1].varValue, inventoryMonth3 = ihcDict[2].varValue, inventoryMonth4 = ihcDict[3].varValue, inventoryMonth5 = ihcDict[4].varValue, inventoryMonth6 = ihcDict[5].varValue, inventoryMonth7 = ihcDict[6].varValue, inventoryMonth8 = ihcDict[7].varValue, inventoryMonth9 = ihcDict[8].varValue, inventoryMonth10 = ihcDict[9].varValue, inventoryMonth11 = ihcDict[10].varValue, hiredTemporary1 = hcDict[0].varValue, hiredTemporary2 = hcDict[1].varValue, hiredTemporary3 = hcDict[2].varValue, hiredTemporary4 = hcDict[3].varValue, hiredTemporary5 = hcDict[4].varValue, hiredTemporary6 = hcDict[5].varValue, hiredTemporary7 = hcDict[6].varValue, hiredTemporary8 = hcDict[7].varValue, hiredTemporary9 = hcDict[8].varValue, hiredTemporary10 = hcDict[9].varValue, hiredTemporary11 = hcDict[10].varValue, hiredTemporary12 = hcDict[11].varValue, firedTemporary1 = fcDict[0].varValue, firedTemporary2 = fcDict[1].varValue, firedTemporary3 = fcDict[2].varValue, firedTemporary4 = fcDict[3].varValue, firedTemporary5 = fcDict[4].varValue, firedTemporary6 = fcDict[5].varValue, firedTemporary7 = fcDict[6].varValue, firedTemporary8 = fcDict[7].varValue, firedTemporary9 = fcDict[8].varValue, firedTemporary10 = fcDict[9].varValue, firedTemporary11 = fcDict[10].varValue, firedTemporary12 = fcDict[11].varValue, optimalCost = value(model.objective))


def demandFour(request, plan_Name):
    if request.method == "POST":
        inputDemand1 = request.POST.get('demand1')
        inputDemand2 = request.POST.get('demand2')
        inputDemand3 = request.POST.get('demand3')
        inputDemand4 = request.POST.get('demand4')
        models.FourMonthPlan.objects.filter(planName=plan_Name).update(demand1 = inputDemand1, 
                                                                             demand2 = inputDemand2, 
                                                                             demand3 = inputDemand3, 
                                                                             demand4 = inputDemand4
                                                                             )
        return redirect('history')
    else:
        detail = models.FourMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Four/demandFour.html',{'detail' : detail})


def numPermanentFour(request, plan_Name):
    if request.method == "POST":
        inputNumPermanent1 = request.POST.get('numPermanent1')
        inputNumPermanent2 = request.POST.get('numPermanent2')
        inputNumPermanent3 = request.POST.get('numPermanent3')
        inputNumPermanent4 = request.POST.get('numPermanent4')
        models.FourMonthPlan.objects.filter(planName=plan_Name).update(numPermanent1 = inputNumPermanent1, 
                                                                             numPermanent2 = inputNumPermanent2, 
                                                                             numPermanent3 = inputNumPermanent3, 
                                                                             numPermanent4 = inputNumPermanent4
                                                                             )
        return redirect('history')
    else:
        detail = models.FourMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Four/numPermanentFour.html',{'detail' : detail})


def prodPermanentFour(request, plan_Name):
    if request.method == "POST":
        inputProdPermanent1 = request.POST.get('prodPermanent1')
        inputProdPermanent2 = request.POST.get('prodPermanent2')
        inputProdPermanent3 = request.POST.get('prodPermanent3')
        inputProdPermanent4 = request.POST.get('prodPermanent4')
        models.FourMonthPlan.objects.filter(planName=plan_Name).update(prodPermanent1 = inputProdPermanent1, 
                                                                             prodPermanent2 = inputProdPermanent2, 
                                                                             prodPermanent3 = inputProdPermanent3, 
                                                                             prodPermanent4 = inputProdPermanent4
                                                                             )
        return redirect('history')
    else:
        detail = models.FourMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Four/prodPermanentFour.html',{'detail' : detail})


def prodTemporaryFour(request, plan_Name):
    if request.method == "POST":
        inputProdTemporary1 = request.POST.get('prodTemporary1')
        inputProdTemporary2 = request.POST.get('prodTemporary2')
        inputProdTemporary3 = request.POST.get('prodTemporary3')
        inputProdTemporary4 = request.POST.get('prodTemporary4')
        models.FourMonthPlan.objects.filter(planName=plan_Name).update(prodTemporary1 = inputProdTemporary1, 
                                                                             prodTemporary2 = inputProdTemporary2, 
                                                                             prodTemporary3 = inputProdTemporary3, 
                                                                             prodTemporary4 = inputProdTemporary4
                                                                             )
        return redirect('history')
    else:
        detail = models.FourMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Four/prodTemporaryFour.html',{'detail' : detail})


def costHiringFour(request, plan_Name):
    if request.method == "POST":
        inputCostHiring1 = request.POST.get('costHiring1')
        inputCostHiring2 = request.POST.get('costHiring2')
        inputCostHiring3 = request.POST.get('costHiring3')
        inputCostHiring4 = request.POST.get('costHiring4')
        models.FourMonthPlan.objects.filter(planName=plan_Name).update(costHiring1 = inputCostHiring1, 
                                                                             costHiring2 = inputCostHiring2, 
                                                                             costHiring3 = inputCostHiring3, 
                                                                             costHiring4 = inputCostHiring4
                                                                             )
        return redirect('history')
    else:
        detail = models.FourMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Four/costHiringFour.html',{'detail' : detail})


def costFiringFour(request, plan_Name):
    if request.method == "POST":
        inputCostFiring1 = request.POST.get('costFiring1')
        inputCostFiring2 = request.POST.get('costFiring2')
        inputCostFiring3 = request.POST.get('costFiring3')
        inputCostFiring4 = request.POST.get('costFiring4')
        models.FourMonthPlan.objects.filter(planName=plan_Name).update(costFiring1 = inputCostFiring1, 
                                                                             costFiring2 = inputCostFiring2, 
                                                                             costFiring3 = inputCostFiring3, 
                                                                             costFiring4 = inputCostFiring4
                                                                             )
        return redirect('history')
    else:
        detail = models.FourMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Four/costFiringFour.html',{'detail' : detail})


def costHoldingUnitFour(request, plan_Name):
    if request.method == "POST":
        inputCostHoldingUnit1 = request.POST.get('costHoldingUnit1')
        inputCostHoldingUnit2 = request.POST.get('costHoldingUnit2')
        inputCostHoldingUnit3 = request.POST.get('costHoldingUnit3')
        inputCostHoldingUnit4 = request.POST.get('costHoldingUnit4')
        models.FourMonthPlan.objects.filter(planName=plan_Name).update(costHoldingUnit1 = inputCostHoldingUnit1, 
                                                                             costHoldingUnit2 = inputCostHoldingUnit2, 
                                                                             costHoldingUnit3 = inputCostHoldingUnit3, 
                                                                             costHoldingUnit4 = inputCostHoldingUnit4
                                                                             )
        return redirect('history')
    else:
        detail = models.FourMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Four/costHoldingUnitFour.html',{'detail' : detail})


def demandFive(request, plan_Name):
    if request.method == "POST":
        inputDemand1 = request.POST.get('demand1')
        inputDemand2 = request.POST.get('demand2')
        inputDemand3 = request.POST.get('demand3')
        inputDemand4 = request.POST.get('demand4')
        inputDemand5 = request.POST.get('demand5')
        models.FiveMonthPlan.objects.filter(planName=plan_Name).update(demand1 = inputDemand1, 
                                                                             demand2 = inputDemand2, 
                                                                             demand3 = inputDemand3, 
                                                                             demand4 = inputDemand4, 
                                                                             demand5 = inputDemand5
                                                                             )
        return redirect('history')
    else:
        detail = models.FiveMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Five/demandFive.html',{'detail' : detail})


def numPermanentFive(request, plan_Name):
    if request.method == "POST":
        inputNumPermanent1 = request.POST.get('numPermanent1')
        inputNumPermanent2 = request.POST.get('numPermanent2')
        inputNumPermanent3 = request.POST.get('numPermanent3')
        inputNumPermanent4 = request.POST.get('numPermanent4')
        inputNumPermanent5 = request.POST.get('numPermanent5')
        models.FiveMonthPlan.objects.filter(planName=plan_Name).update(numPermanent1 = inputNumPermanent1, 
                                                                             numPermanent2 = inputNumPermanent2, 
                                                                             numPermanent3 = inputNumPermanent3, 
                                                                             numPermanent4 = inputNumPermanent4, 
                                                                             numPermanent5 = inputNumPermanent5
                                                                             )
        return redirect('history')
    else:
        detail = models.FiveMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Five/numPermanentFive.html',{'detail' : detail})


def prodPermanentFive(request, plan_Name):
    if request.method == "POST":
        inputProdPermanent1 = request.POST.get('prodPermanent1')
        inputProdPermanent2 = request.POST.get('prodPermanent2')
        inputProdPermanent3 = request.POST.get('prodPermanent3')
        inputProdPermanent4 = request.POST.get('prodPermanent4')
        inputProdPermanent5 = request.POST.get('prodPermanent5')
        models.FiveMonthPlan.objects.filter(planName=plan_Name).update(prodPermanent1 = inputProdPermanent1, 
                                                                             prodPermanent2 = inputProdPermanent2, 
                                                                             prodPermanent3 = inputProdPermanent3, 
                                                                             prodPermanent4 = inputProdPermanent4, 
                                                                             prodPermanent5 = inputProdPermanent5
                                                                             )
        return redirect('history')
    else:
        detail = models.FiveMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Five/prodPermanentFive.html',{'detail' : detail})


def prodTemporaryFive(request, plan_Name):
    if request.method == "POST":
        inputProdTemporary1 = request.POST.get('prodTemporary1')
        inputProdTemporary2 = request.POST.get('prodTemporary2')
        inputProdTemporary3 = request.POST.get('prodTemporary3')
        inputProdTemporary4 = request.POST.get('prodTemporary4')
        inputProdTemporary5 = request.POST.get('prodTemporary5')
        models.FiveMonthPlan.objects.filter(planName=plan_Name).update(prodTemporary1 = inputProdTemporary1, 
                                                                             prodTemporary2 = inputProdTemporary2, 
                                                                             prodTemporary3 = inputProdTemporary3, 
                                                                             prodTemporary4 = inputProdTemporary4, 
                                                                             prodTemporary5 = inputProdTemporary5
                                                                             )
        return redirect('history')
    else:
        detail = models.FiveMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Five/prodTemporaryFive.html',{'detail' : detail})


def costHiringFive(request, plan_Name):
    if request.method == "POST":
        inputCostHiring1 = request.POST.get('costHiring1')
        inputCostHiring2 = request.POST.get('costHiring2')
        inputCostHiring3 = request.POST.get('costHiring3')
        inputCostHiring4 = request.POST.get('costHiring4')
        inputCostHiring5 = request.POST.get('costHiring5')
        models.FiveMonthPlan.objects.filter(planName=plan_Name).update(costHiring1 = inputCostHiring1, 
                                                                             costHiring2 = inputCostHiring2, 
                                                                             costHiring3 = inputCostHiring3, 
                                                                             costHiring4 = inputCostHiring4, 
                                                                             costHiring5 = inputCostHiring5
                                                                             )
        return redirect('history')
    else:
        detail = models.FiveMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Five/costHiringFive.html',{'detail' : detail})


def costFiringFive(request, plan_Name):
    if request.method == "POST":
        inputCostFiring1 = request.POST.get('costFiring1')
        inputCostFiring2 = request.POST.get('costFiring2')
        inputCostFiring3 = request.POST.get('costFiring3')
        inputCostFiring4 = request.POST.get('costFiring4')
        inputCostFiring5 = request.POST.get('costFiring5')
        models.FiveMonthPlan.objects.filter(planName=plan_Name).update(costFiring1 = inputCostFiring1, 
                                                                             costFiring2 = inputCostFiring2, 
                                                                             costFiring3 = inputCostFiring3, 
                                                                             costFiring4 = inputCostFiring4, 
                                                                             costFiring5 = inputCostFiring5
                                                                             )
        return redirect('history')
    else:
        detail = models.FiveMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Five/costFiringFive.html',{'detail' : detail})


def costHoldingUnitFive(request, plan_Name):
    if request.method == "POST":
        inputCostHoldingUnit1 = request.POST.get('costHoldingUnit1')
        inputCostHoldingUnit2 = request.POST.get('costHoldingUnit2')
        inputCostHoldingUnit3 = request.POST.get('costHoldingUnit3')
        inputCostHoldingUnit4 = request.POST.get('costHoldingUnit4')
        inputCostHoldingUnit5 = request.POST.get('costHoldingUnit5')
        models.FiveMonthPlan.objects.filter(planName=plan_Name).update(costHoldingUnit1 = inputCostHoldingUnit1, 
                                                                             costHoldingUnit2 = inputCostHoldingUnit2, 
                                                                             costHoldingUnit3 = inputCostHoldingUnit3, 
                                                                             costHoldingUnit4 = inputCostHoldingUnit4, 
                                                                             costHoldingUnit5 = inputCostHoldingUnit5
                                                                             )
        return redirect('history')
    else:
        detail = models.FiveMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Five/costHoldingUnitFive.html',{'detail' : detail})


def demandSix(request, plan_Name):
    if request.method == "POST":
        inputDemand1 = request.POST.get('demand1')
        inputDemand2 = request.POST.get('demand2')
        inputDemand3 = request.POST.get('demand3')
        inputDemand4 = request.POST.get('demand4')
        inputDemand5 = request.POST.get('demand5')
        inputDemand6 = request.POST.get('demand6')
        models.SixMonthPlan.objects.filter(planName=plan_Name).update(demand1 = inputDemand1, 
                                                                             demand2 = inputDemand2, 
                                                                             demand3 = inputDemand3, 
                                                                             demand4 = inputDemand4, 
                                                                             demand5 = inputDemand5, 
                                                                             demand6 = inputDemand6
                                                                             )
        return redirect('history')
    else:
        detail = models.SixMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Six/demandSix.html',{'detail' : detail})


def numPermanentSix(request, plan_Name):
    if request.method == "POST":
        inputNumPermanent1 = request.POST.get('numPermanent1')
        inputNumPermanent2 = request.POST.get('numPermanent2')
        inputNumPermanent3 = request.POST.get('numPermanent3')
        inputNumPermanent4 = request.POST.get('numPermanent4')
        inputNumPermanent5 = request.POST.get('numPermanent5')
        inputNumPermanent6 = request.POST.get('numPermanent6')
        models.SixMonthPlan.objects.filter(planName=plan_Name).update(numPermanent1 = inputNumPermanent1, 
                                                                             numPermanent2 = inputNumPermanent2, 
                                                                             numPermanent3 = inputNumPermanent3, 
                                                                             numPermanent4 = inputNumPermanent4, 
                                                                             numPermanent5 = inputNumPermanent5, 
                                                                             numPermanent6 = inputNumPermanent6
                                                                             )
        return redirect('history')
    else:
        detail = models.SixMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Six/numPermanentSix.html',{'detail' : detail})


def prodPermanentSix(request, plan_Name):
    if request.method == "POST":
        inputProdPermanent1 = request.POST.get('prodPermanent1')
        inputProdPermanent2 = request.POST.get('prodPermanent2')
        inputProdPermanent3 = request.POST.get('prodPermanent3')
        inputProdPermanent4 = request.POST.get('prodPermanent4')
        inputProdPermanent5 = request.POST.get('prodPermanent5')
        inputProdPermanent6 = request.POST.get('prodPermanent6')
        models.SixMonthPlan.objects.filter(planName=plan_Name).update(prodPermanent1 = inputProdPermanent1, 
                                                                             prodPermanent2 = inputProdPermanent2, 
                                                                             prodPermanent3 = inputProdPermanent3, 
                                                                             prodPermanent4 = inputProdPermanent4, 
                                                                             prodPermanent5 = inputProdPermanent5, 
                                                                             prodPermanent6 = inputProdPermanent6
                                                                             )
        return redirect('history')
    else:
        detail = models.SixMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Six/prodPermanentSix.html',{'detail' : detail})


def prodTemporarySix(request, plan_Name):
    if request.method == "POST":
        inputProdTemporary1 = request.POST.get('prodTemporary1')
        inputProdTemporary2 = request.POST.get('prodTemporary2')
        inputProdTemporary3 = request.POST.get('prodTemporary3')
        inputProdTemporary4 = request.POST.get('prodTemporary4')
        inputProdTemporary5 = request.POST.get('prodTemporary5')
        inputProdTemporary6 = request.POST.get('prodTemporary6')
        models.SixMonthPlan.objects.filter(planName=plan_Name).update(prodTemporary1 = inputProdTemporary1, 
                                                                             prodTemporary2 = inputProdTemporary2, 
                                                                             prodTemporary3 = inputProdTemporary3, 
                                                                             prodTemporary4 = inputProdTemporary4, 
                                                                             prodTemporary5 = inputProdTemporary5, 
                                                                             prodTemporary6 = inputProdTemporary6
                                                                             )
        return redirect('history')
    else:
        detail = models.SixMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Six/prodTemporarySix.html',{'detail' : detail})


def costHiringSix(request, plan_Name):
    if request.method == "POST":
        inputCostHiring1 = request.POST.get('costHiring1')
        inputCostHiring2 = request.POST.get('costHiring2')
        inputCostHiring3 = request.POST.get('costHiring3')
        inputCostHiring4 = request.POST.get('costHiring4')
        inputCostHiring5 = request.POST.get('costHiring5')
        inputCostHiring6 = request.POST.get('costHiring6')
        models.SixMonthPlan.objects.filter(planName=plan_Name).update(costHiring1 = inputCostHiring1, 
                                                                             costHiring2 = inputCostHiring2, 
                                                                             costHiring3 = inputCostHiring3, 
                                                                             costHiring4 = inputCostHiring4, 
                                                                             costHiring5 = inputCostHiring5, 
                                                                             costHiring6 = inputCostHiring6
                                                                             )
        return redirect('history')
    else:
        detail = models.SixMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Six/costHiringSix.html',{'detail' : detail})


def costFiringSix(request, plan_Name):
    if request.method == "POST":
        inputCostFiring1 = request.POST.get('costFiring1')
        inputCostFiring2 = request.POST.get('costFiring2')
        inputCostFiring3 = request.POST.get('costFiring3')
        inputCostFiring4 = request.POST.get('costFiring4')
        inputCostFiring5 = request.POST.get('costFiring5')
        inputCostFiring6 = request.POST.get('costFiring6')
        models.SixMonthPlan.objects.filter(planName=plan_Name).update(costFiring1 = inputCostFiring1, 
                                                                             costFiring2 = inputCostFiring2, 
                                                                             costFiring3 = inputCostFiring3, 
                                                                             costFiring4 = inputCostFiring4, 
                                                                             costFiring5 = inputCostFiring5, 
                                                                             costFiring6 = inputCostFiring6
                                                                             )
        return redirect('history')
    else:
        detail = models.SixMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Six/costFiringSix.html',{'detail' : detail})


def costHoldingUnitSix(request, plan_Name):
    if request.method == "POST":
        inputCostHoldingUnit1 = request.POST.get('costHoldingUnit1')
        inputCostHoldingUnit2 = request.POST.get('costHoldingUnit2')
        inputCostHoldingUnit3 = request.POST.get('costHoldingUnit3')
        inputCostHoldingUnit4 = request.POST.get('costHoldingUnit4')
        inputCostHoldingUnit5 = request.POST.get('costHoldingUnit5')
        inputCostHoldingUnit6 = request.POST.get('costHoldingUnit6')
        models.SixMonthPlan.objects.filter(planName=plan_Name).update(costHoldingUnit1 = inputCostHoldingUnit1, 
                                                                             costHoldingUnit2 = inputCostHoldingUnit2, 
                                                                             costHoldingUnit3 = inputCostHoldingUnit3, 
                                                                             costHoldingUnit4 = inputCostHoldingUnit4, 
                                                                             costHoldingUnit5 = inputCostHoldingUnit5, 
                                                                             costHoldingUnit6 = inputCostHoldingUnit6
                                                                             )
        return redirect('history')
    else:
        detail = models.SixMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Six/costHoldingUnitSix.html',{'detail' : detail})


def demandSeven(request, plan_Name):
    if request.method == "POST":
        inputDemand1 = request.POST.get('demand1')
        inputDemand2 = request.POST.get('demand2')
        inputDemand3 = request.POST.get('demand3')
        inputDemand4 = request.POST.get('demand4')
        inputDemand5 = request.POST.get('demand5')
        inputDemand6 = request.POST.get('demand6')
        inputDemand7 = request.POST.get('demand7')
        models.SevenMonthPlan.objects.filter(planName=plan_Name).update(demand1 = inputDemand1, 
                                                                             demand2 = inputDemand2, 
                                                                             demand3 = inputDemand3, 
                                                                             demand4 = inputDemand4, 
                                                                             demand5 = inputDemand5, 
                                                                             demand6 = inputDemand6, 
                                                                             demand7 = inputDemand7
                                                                             )
        return redirect('history')
    else:
        detail = models.SevenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Seven/demandSeven.html',{'detail' : detail})


def numPermanentSeven(request, plan_Name):
    if request.method == "POST":
        inputNumPermanent1 = request.POST.get('numPermanent1')
        inputNumPermanent2 = request.POST.get('numPermanent2')
        inputNumPermanent3 = request.POST.get('numPermanent3')
        inputNumPermanent4 = request.POST.get('numPermanent4')
        inputNumPermanent5 = request.POST.get('numPermanent5')
        inputNumPermanent6 = request.POST.get('numPermanent6')
        inputNumPermanent7 = request.POST.get('numPermanent7')
        models.SevenMonthPlan.objects.filter(planName=plan_Name).update(numPermanent1 = inputNumPermanent1, 
                                                                             numPermanent2 = inputNumPermanent2, 
                                                                             numPermanent3 = inputNumPermanent3, 
                                                                             numPermanent4 = inputNumPermanent4, 
                                                                             numPermanent5 = inputNumPermanent5, 
                                                                             numPermanent6 = inputNumPermanent6, 
                                                                             numPermanent7 = inputNumPermanent7
                                                                             )
        return redirect('history')
    else:
        detail = models.SevenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Seven/numPermanentSeven.html',{'detail' : detail})


def prodPermanentSeven(request, plan_Name):
    if request.method == "POST":
        inputProdPermanent1 = request.POST.get('prodPermanent1')
        inputProdPermanent2 = request.POST.get('prodPermanent2')
        inputProdPermanent3 = request.POST.get('prodPermanent3')
        inputProdPermanent4 = request.POST.get('prodPermanent4')
        inputProdPermanent5 = request.POST.get('prodPermanent5')
        inputProdPermanent6 = request.POST.get('prodPermanent6')
        inputProdPermanent7 = request.POST.get('prodPermanent7')
        models.SevenMonthPlan.objects.filter(planName=plan_Name).update(prodPermanent1 = inputProdPermanent1, 
                                                                             prodPermanent2 = inputProdPermanent2, 
                                                                             prodPermanent3 = inputProdPermanent3, 
                                                                             prodPermanent4 = inputProdPermanent4, 
                                                                             prodPermanent5 = inputProdPermanent5, 
                                                                             prodPermanent6 = inputProdPermanent6, 
                                                                             prodPermanent7 = inputProdPermanent7
                                                                             )
        return redirect('history')
    else:
        detail = models.SevenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Seven/prodPermanentSeven.html',{'detail' : detail})


def prodTemporarySeven(request, plan_Name):
    if request.method == "POST":
        inputProdTemporary1 = request.POST.get('prodTemporary1')
        inputProdTemporary2 = request.POST.get('prodTemporary2')
        inputProdTemporary3 = request.POST.get('prodTemporary3')
        inputProdTemporary4 = request.POST.get('prodTemporary4')
        inputProdTemporary5 = request.POST.get('prodTemporary5')
        inputProdTemporary6 = request.POST.get('prodTemporary6')
        inputProdTemporary7 = request.POST.get('prodTemporary7')
        models.SevenMonthPlan.objects.filter(planName=plan_Name).update(prodTemporary1 = inputProdTemporary1, 
                                                                             prodTemporary2 = inputProdTemporary2, 
                                                                             prodTemporary3 = inputProdTemporary3, 
                                                                             prodTemporary4 = inputProdTemporary4, 
                                                                             prodTemporary5 = inputProdTemporary5, 
                                                                             prodTemporary6 = inputProdTemporary6, 
                                                                             prodTemporary7 = inputProdTemporary7
                                                                             )
        return redirect('history')
    else:
        detail = models.SevenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Seven/prodTemporarySeven.html',{'detail' : detail})


def costHiringSeven(request, plan_Name):
    if request.method == "POST":
        inputCostHiring1 = request.POST.get('costHiring1')
        inputCostHiring2 = request.POST.get('costHiring2')
        inputCostHiring3 = request.POST.get('costHiring3')
        inputCostHiring4 = request.POST.get('costHiring4')
        inputCostHiring5 = request.POST.get('costHiring5')
        inputCostHiring6 = request.POST.get('costHiring6')
        inputCostHiring7 = request.POST.get('costHiring7')
        models.SevenMonthPlan.objects.filter(planName=plan_Name).update(costHiring1 = inputCostHiring1, 
                                                                             costHiring2 = inputCostHiring2, 
                                                                             costHiring3 = inputCostHiring3, 
                                                                             costHiring4 = inputCostHiring4, 
                                                                             costHiring5 = inputCostHiring5, 
                                                                             costHiring6 = inputCostHiring6, 
                                                                             costHiring7 = inputCostHiring7
                                                                             )
        return redirect('history')
    else:
        detail = models.SevenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Seven/costHiringSeven.html',{'detail' : detail})


def costFiringSeven(request, plan_Name):
    if request.method == "POST":
        inputCostFiring1 = request.POST.get('costFiring1')
        inputCostFiring2 = request.POST.get('costFiring2')
        inputCostFiring3 = request.POST.get('costFiring3')
        inputCostFiring4 = request.POST.get('costFiring4')
        inputCostFiring5 = request.POST.get('costFiring5')
        inputCostFiring6 = request.POST.get('costFiring6')
        inputCostFiring7 = request.POST.get('costFiring7')
        models.SevenMonthPlan.objects.filter(planName=plan_Name).update(costFiring1 = inputCostFiring1, 
                                                                             costFiring2 = inputCostFiring2, 
                                                                             costFiring3 = inputCostFiring3, 
                                                                             costFiring4 = inputCostFiring4, 
                                                                             costFiring5 = inputCostFiring5, 
                                                                             costFiring6 = inputCostFiring6, 
                                                                             costFiring7 = inputCostFiring7
                                                                             )
        return redirect('history')
    else:
        detail = models.SevenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Seven/costFiringSeven.html',{'detail' : detail})


def costHoldingUnitSeven(request, plan_Name):
    if request.method == "POST":
        inputCostHoldingUnit1 = request.POST.get('costHoldingUnit1')
        inputCostHoldingUnit2 = request.POST.get('costHoldingUnit2')
        inputCostHoldingUnit3 = request.POST.get('costHoldingUnit3')
        inputCostHoldingUnit4 = request.POST.get('costHoldingUnit4')
        inputCostHoldingUnit5 = request.POST.get('costHoldingUnit5')
        inputCostHoldingUnit6 = request.POST.get('costHoldingUnit6')
        inputCostHoldingUnit7 = request.POST.get('costHoldingUnit7')
        models.SevenMonthPlan.objects.filter(planName=plan_Name).update(costHoldingUnit1 = inputCostHoldingUnit1, 
                                                                             costHoldingUnit2 = inputCostHoldingUnit2, 
                                                                             costHoldingUnit3 = inputCostHoldingUnit3, 
                                                                             costHoldingUnit4 = inputCostHoldingUnit4, 
                                                                             costHoldingUnit5 = inputCostHoldingUnit5, 
                                                                             costHoldingUnit6 = inputCostHoldingUnit6, 
                                                                             costHoldingUnit7 = inputCostHoldingUnit7
                                                                             )
        return redirect('history')
    else:
        detail = models.SevenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Seven/costHoldingUnitSeven.html',{'detail' : detail})


def demandEight(request, plan_Name):
    if request.method == "POST":
        inputDemand1 = request.POST.get('demand1')
        inputDemand2 = request.POST.get('demand2')
        inputDemand3 = request.POST.get('demand3')
        inputDemand4 = request.POST.get('demand4')
        inputDemand5 = request.POST.get('demand5')
        inputDemand6 = request.POST.get('demand6')
        inputDemand7 = request.POST.get('demand7')
        inputDemand8 = request.POST.get('demand8')
        models.EightMonthPlan.objects.filter(planName=plan_Name).update(demand1 = inputDemand1, 
                                                                             demand2 = inputDemand2, 
                                                                             demand3 = inputDemand3, 
                                                                             demand4 = inputDemand4, 
                                                                             demand5 = inputDemand5, 
                                                                             demand6 = inputDemand6, 
                                                                             demand7 = inputDemand7, 
                                                                             demand8 = inputDemand8
                                                                             )
        return redirect('history')
    else:
        detail = models.EightMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Eight/demandEight.html',{'detail' : detail})


def numPermanentEight(request, plan_Name):
    if request.method == "POST":
        inputNumPermanent1 = request.POST.get('numPermanent1')
        inputNumPermanent2 = request.POST.get('numPermanent2')
        inputNumPermanent3 = request.POST.get('numPermanent3')
        inputNumPermanent4 = request.POST.get('numPermanent4')
        inputNumPermanent5 = request.POST.get('numPermanent5')
        inputNumPermanent6 = request.POST.get('numPermanent6')
        inputNumPermanent7 = request.POST.get('numPermanent7')
        inputNumPermanent8 = request.POST.get('numPermanent8')
        models.EightMonthPlan.objects.filter(planName=plan_Name).update(numPermanent1 = inputNumPermanent1, 
                                                                             numPermanent2 = inputNumPermanent2, 
                                                                             numPermanent3 = inputNumPermanent3, 
                                                                             numPermanent4 = inputNumPermanent4, 
                                                                             numPermanent5 = inputNumPermanent5, 
                                                                             numPermanent6 = inputNumPermanent6, 
                                                                             numPermanent7 = inputNumPermanent7, 
                                                                             numPermanent8 = inputNumPermanent8
                                                                             )
        return redirect('history')
    else:
        detail = models.EightMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Eight/numPermanentEight.html',{'detail' : detail})


def prodPermanentEight(request, plan_Name):
    if request.method == "POST":
        inputProdPermanent1 = request.POST.get('prodPermanent1')
        inputProdPermanent2 = request.POST.get('prodPermanent2')
        inputProdPermanent3 = request.POST.get('prodPermanent3')
        inputProdPermanent4 = request.POST.get('prodPermanent4')
        inputProdPermanent5 = request.POST.get('prodPermanent5')
        inputProdPermanent6 = request.POST.get('prodPermanent6')
        inputProdPermanent7 = request.POST.get('prodPermanent7')
        inputProdPermanent8 = request.POST.get('prodPermanent8')
        models.EightMonthPlan.objects.filter(planName=plan_Name).update(prodPermanent1 = inputProdPermanent1, 
                                                                             prodPermanent2 = inputProdPermanent2, 
                                                                             prodPermanent3 = inputProdPermanent3, 
                                                                             prodPermanent4 = inputProdPermanent4, 
                                                                             prodPermanent5 = inputProdPermanent5, 
                                                                             prodPermanent6 = inputProdPermanent6, 
                                                                             prodPermanent7 = inputProdPermanent7, 
                                                                             prodPermanent8 = inputProdPermanent8
                                                                             )
        return redirect('history')
    else:
        detail = models.EightMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Eight/prodPermanentEight.html',{'detail' : detail})


def prodTemporaryEight(request, plan_Name):
    if request.method == "POST":
        inputProdTemporary1 = request.POST.get('prodTemporary1')
        inputProdTemporary2 = request.POST.get('prodTemporary2')
        inputProdTemporary3 = request.POST.get('prodTemporary3')
        inputProdTemporary4 = request.POST.get('prodTemporary4')
        inputProdTemporary5 = request.POST.get('prodTemporary5')
        inputProdTemporary6 = request.POST.get('prodTemporary6')
        inputProdTemporary7 = request.POST.get('prodTemporary7')
        inputProdTemporary8 = request.POST.get('prodTemporary8')
        models.EightMonthPlan.objects.filter(planName=plan_Name).update(prodTemporary1 = inputProdTemporary1, 
                                                                             prodTemporary2 = inputProdTemporary2, 
                                                                             prodTemporary3 = inputProdTemporary3, 
                                                                             prodTemporary4 = inputProdTemporary4, 
                                                                             prodTemporary5 = inputProdTemporary5, 
                                                                             prodTemporary6 = inputProdTemporary6, 
                                                                             prodTemporary7 = inputProdTemporary7, 
                                                                             prodTemporary8 = inputProdTemporary8
                                                                             )
        return redirect('history')
    else:
        detail = models.EightMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Eight/prodTemporaryEight.html',{'detail' : detail})


def costHiringEight(request, plan_Name):
    if request.method == "POST":
        inputCostHiring1 = request.POST.get('costHiring1')
        inputCostHiring2 = request.POST.get('costHiring2')
        inputCostHiring3 = request.POST.get('costHiring3')
        inputCostHiring4 = request.POST.get('costHiring4')
        inputCostHiring5 = request.POST.get('costHiring5')
        inputCostHiring6 = request.POST.get('costHiring6')
        inputCostHiring7 = request.POST.get('costHiring7')
        inputCostHiring8 = request.POST.get('costHiring8')
        models.EightMonthPlan.objects.filter(planName=plan_Name).update(costHiring1 = inputCostHiring1, 
                                                                             costHiring2 = inputCostHiring2, 
                                                                             costHiring3 = inputCostHiring3, 
                                                                             costHiring4 = inputCostHiring4, 
                                                                             costHiring5 = inputCostHiring5, 
                                                                             costHiring6 = inputCostHiring6, 
                                                                             costHiring7 = inputCostHiring7, 
                                                                             costHiring8 = inputCostHiring8
                                                                             )
        return redirect('history')
    else:
        detail = models.EightMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Eight/costHiringEight.html',{'detail' : detail})


def costFiringEight(request, plan_Name):
    if request.method == "POST":
        inputCostFiring1 = request.POST.get('costFiring1')
        inputCostFiring2 = request.POST.get('costFiring2')
        inputCostFiring3 = request.POST.get('costFiring3')
        inputCostFiring4 = request.POST.get('costFiring4')
        inputCostFiring5 = request.POST.get('costFiring5')
        inputCostFiring6 = request.POST.get('costFiring6')
        inputCostFiring7 = request.POST.get('costFiring7')
        inputCostFiring8 = request.POST.get('costFiring8')
        models.EightMonthPlan.objects.filter(planName=plan_Name).update(costFiring1 = inputCostFiring1, 
                                                                             costFiring2 = inputCostFiring2, 
                                                                             costFiring3 = inputCostFiring3, 
                                                                             costFiring4 = inputCostFiring4, 
                                                                             costFiring5 = inputCostFiring5, 
                                                                             costFiring6 = inputCostFiring6, 
                                                                             costFiring7 = inputCostFiring7, 
                                                                             costFiring8 = inputCostFiring8
                                                                             )
        return redirect('history')
    else:
        detail = models.EightMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Eight/costFiringEight.html',{'detail' : detail})


def costHoldingUnitEight(request, plan_Name):
    if request.method == "POST":
        inputCostHoldingUnit1 = request.POST.get('costHoldingUnit1')
        inputCostHoldingUnit2 = request.POST.get('costHoldingUnit2')
        inputCostHoldingUnit3 = request.POST.get('costHoldingUnit3')
        inputCostHoldingUnit4 = request.POST.get('costHoldingUnit4')
        inputCostHoldingUnit5 = request.POST.get('costHoldingUnit5')
        inputCostHoldingUnit6 = request.POST.get('costHoldingUnit6')
        inputCostHoldingUnit7 = request.POST.get('costHoldingUnit7')
        inputCostHoldingUnit8 = request.POST.get('costHoldingUnit8')
        models.EightMonthPlan.objects.filter(planName=plan_Name).update(costHoldingUnit1 = inputCostHoldingUnit1, 
                                                                             costHoldingUnit2 = inputCostHoldingUnit2, 
                                                                             costHoldingUnit3 = inputCostHoldingUnit3, 
                                                                             costHoldingUnit4 = inputCostHoldingUnit4, 
                                                                             costHoldingUnit5 = inputCostHoldingUnit5, 
                                                                             costHoldingUnit6 = inputCostHoldingUnit6, 
                                                                             costHoldingUnit7 = inputCostHoldingUnit7, 
                                                                             costHoldingUnit8 = inputCostHoldingUnit8
                                                                             )
        return redirect('history')
    else:
        detail = models.EightMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Eight/costHoldingUnitEight.html',{'detail' : detail})


def demandNine(request, plan_Name):
    if request.method == "POST":
        inputDemand1 = request.POST.get('demand1')
        inputDemand2 = request.POST.get('demand2')
        inputDemand3 = request.POST.get('demand3')
        inputDemand4 = request.POST.get('demand4')
        inputDemand5 = request.POST.get('demand5')
        inputDemand6 = request.POST.get('demand6')
        inputDemand7 = request.POST.get('demand7')
        inputDemand8 = request.POST.get('demand8')
        inputDemand9 = request.POST.get('demand9')
        models.NineMonthPlan.objects.filter(planName=plan_Name).update(demand1 = inputDemand1, 
                                                                             demand2 = inputDemand2, 
                                                                             demand3 = inputDemand3, 
                                                                             demand4 = inputDemand4, 
                                                                             demand5 = inputDemand5, 
                                                                             demand6 = inputDemand6, 
                                                                             demand7 = inputDemand7, 
                                                                             demand8 = inputDemand8, 
                                                                             demand9 = inputDemand9
                                                                             )
        return redirect('history')
    else:
        detail = models.NineMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Nine/demandNine.html',{'detail' : detail})


def numPermanentNine(request, plan_Name):
    if request.method == "POST":
        inputNumPermanent1 = request.POST.get('numPermanent1')
        inputNumPermanent2 = request.POST.get('numPermanent2')
        inputNumPermanent3 = request.POST.get('numPermanent3')
        inputNumPermanent4 = request.POST.get('numPermanent4')
        inputNumPermanent5 = request.POST.get('numPermanent5')
        inputNumPermanent6 = request.POST.get('numPermanent6')
        inputNumPermanent7 = request.POST.get('numPermanent7')
        inputNumPermanent8 = request.POST.get('numPermanent8')
        inputNumPermanent9 = request.POST.get('numPermanent9')
        models.NineMonthPlan.objects.filter(planName=plan_Name).update(numPermanent1 = inputNumPermanent1, 
                                                                             numPermanent2 = inputNumPermanent2, 
                                                                             numPermanent3 = inputNumPermanent3, 
                                                                             numPermanent4 = inputNumPermanent4, 
                                                                             numPermanent5 = inputNumPermanent5, 
                                                                             numPermanent6 = inputNumPermanent6, 
                                                                             numPermanent7 = inputNumPermanent7, 
                                                                             numPermanent8 = inputNumPermanent8, 
                                                                             numPermanent9 = inputNumPermanent9
                                                                             )
        return redirect('history')
    else:
        detail = models.NineMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Nine/numPermanentNine.html',{'detail' : detail})


def prodPermanentNine(request, plan_Name):
    if request.method == "POST":
        inputProdPermanent1 = request.POST.get('prodPermanent1')
        inputProdPermanent2 = request.POST.get('prodPermanent2')
        inputProdPermanent3 = request.POST.get('prodPermanent3')
        inputProdPermanent4 = request.POST.get('prodPermanent4')
        inputProdPermanent5 = request.POST.get('prodPermanent5')
        inputProdPermanent6 = request.POST.get('prodPermanent6')
        inputProdPermanent7 = request.POST.get('prodPermanent7')
        inputProdPermanent8 = request.POST.get('prodPermanent8')
        inputProdPermanent9 = request.POST.get('prodPermanent9')
        models.NineMonthPlan.objects.filter(planName=plan_Name).update(prodPermanent1 = inputProdPermanent1, 
                                                                             prodPermanent2 = inputProdPermanent2, 
                                                                             prodPermanent3 = inputProdPermanent3, 
                                                                             prodPermanent4 = inputProdPermanent4, 
                                                                             prodPermanent5 = inputProdPermanent5, 
                                                                             prodPermanent6 = inputProdPermanent6, 
                                                                             prodPermanent7 = inputProdPermanent7, 
                                                                             prodPermanent8 = inputProdPermanent8, 
                                                                             prodPermanent9 = inputProdPermanent9
                                                                             )
        return redirect('history')
    else:
        detail = models.NineMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Nine/prodPermanentNine.html',{'detail' : detail})


def prodTemporaryNine(request, plan_Name):
    if request.method == "POST":
        inputProdTemporary1 = request.POST.get('prodTemporary1')
        inputProdTemporary2 = request.POST.get('prodTemporary2')
        inputProdTemporary3 = request.POST.get('prodTemporary3')
        inputProdTemporary4 = request.POST.get('prodTemporary4')
        inputProdTemporary5 = request.POST.get('prodTemporary5')
        inputProdTemporary6 = request.POST.get('prodTemporary6')
        inputProdTemporary7 = request.POST.get('prodTemporary7')
        inputProdTemporary8 = request.POST.get('prodTemporary8')
        inputProdTemporary9 = request.POST.get('prodTemporary9')
        models.NineMonthPlan.objects.filter(planName=plan_Name).update(prodTemporary1 = inputProdTemporary1, 
                                                                             prodTemporary2 = inputProdTemporary2, 
                                                                             prodTemporary3 = inputProdTemporary3, 
                                                                             prodTemporary4 = inputProdTemporary4, 
                                                                             prodTemporary5 = inputProdTemporary5, 
                                                                             prodTemporary6 = inputProdTemporary6, 
                                                                             prodTemporary7 = inputProdTemporary7, 
                                                                             prodTemporary8 = inputProdTemporary8, 
                                                                             prodTemporary9 = inputProdTemporary9
                                                                             )
        return redirect('history')
    else:
        detail = models.NineMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Nine/prodTemporaryNine.html',{'detail' : detail})


def costHiringNine(request, plan_Name):
    if request.method == "POST":
        inputCostHiring1 = request.POST.get('costHiring1')
        inputCostHiring2 = request.POST.get('costHiring2')
        inputCostHiring3 = request.POST.get('costHiring3')
        inputCostHiring4 = request.POST.get('costHiring4')
        inputCostHiring5 = request.POST.get('costHiring5')
        inputCostHiring6 = request.POST.get('costHiring6')
        inputCostHiring7 = request.POST.get('costHiring7')
        inputCostHiring8 = request.POST.get('costHiring8')
        inputCostHiring9 = request.POST.get('costHiring9')
        models.NineMonthPlan.objects.filter(planName=plan_Name).update(costHiring1 = inputCostHiring1, 
                                                                             costHiring2 = inputCostHiring2, 
                                                                             costHiring3 = inputCostHiring3, 
                                                                             costHiring4 = inputCostHiring4, 
                                                                             costHiring5 = inputCostHiring5, 
                                                                             costHiring6 = inputCostHiring6, 
                                                                             costHiring7 = inputCostHiring7, 
                                                                             costHiring8 = inputCostHiring8, 
                                                                             costHiring9 = inputCostHiring9
                                                                             )
        return redirect('history')
    else:
        detail = models.NineMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Nine/costHiringNine.html',{'detail' : detail})


def costFiringNine(request, plan_Name):
    if request.method == "POST":
        inputCostFiring1 = request.POST.get('costFiring1')
        inputCostFiring2 = request.POST.get('costFiring2')
        inputCostFiring3 = request.POST.get('costFiring3')
        inputCostFiring4 = request.POST.get('costFiring4')
        inputCostFiring5 = request.POST.get('costFiring5')
        inputCostFiring6 = request.POST.get('costFiring6')
        inputCostFiring7 = request.POST.get('costFiring7')
        inputCostFiring8 = request.POST.get('costFiring8')
        inputCostFiring9 = request.POST.get('costFiring9')
        models.NineMonthPlan.objects.filter(planName=plan_Name).update(costFiring1 = inputCostFiring1, 
                                                                             costFiring2 = inputCostFiring2, 
                                                                             costFiring3 = inputCostFiring3, 
                                                                             costFiring4 = inputCostFiring4, 
                                                                             costFiring5 = inputCostFiring5, 
                                                                             costFiring6 = inputCostFiring6, 
                                                                             costFiring7 = inputCostFiring7, 
                                                                             costFiring8 = inputCostFiring8, 
                                                                             costFiring9 = inputCostFiring9
                                                                             )
        return redirect('history')
    else:
        detail = models.NineMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Nine/costFiringNine.html',{'detail' : detail})


def costHoldingUnitNine(request, plan_Name):
    if request.method == "POST":
        inputCostHoldingUnit1 = request.POST.get('costHoldingUnit1')
        inputCostHoldingUnit2 = request.POST.get('costHoldingUnit2')
        inputCostHoldingUnit3 = request.POST.get('costHoldingUnit3')
        inputCostHoldingUnit4 = request.POST.get('costHoldingUnit4')
        inputCostHoldingUnit5 = request.POST.get('costHoldingUnit5')
        inputCostHoldingUnit6 = request.POST.get('costHoldingUnit6')
        inputCostHoldingUnit7 = request.POST.get('costHoldingUnit7')
        inputCostHoldingUnit8 = request.POST.get('costHoldingUnit8')
        inputCostHoldingUnit9 = request.POST.get('costHoldingUnit9')
        models.NineMonthPlan.objects.filter(planName=plan_Name).update(costHoldingUnit1 = inputCostHoldingUnit1, 
                                                                             costHoldingUnit2 = inputCostHoldingUnit2, 
                                                                             costHoldingUnit3 = inputCostHoldingUnit3, 
                                                                             costHoldingUnit4 = inputCostHoldingUnit4, 
                                                                             costHoldingUnit5 = inputCostHoldingUnit5, 
                                                                             costHoldingUnit6 = inputCostHoldingUnit6, 
                                                                             costHoldingUnit7 = inputCostHoldingUnit7, 
                                                                             costHoldingUnit8 = inputCostHoldingUnit8, 
                                                                             costHoldingUnit9 = inputCostHoldingUnit9
                                                                             )
        return redirect('history')
    else:
        detail = models.NineMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Nine/costHoldingUnitNine.html',{'detail' : detail})


def demandTen(request, plan_Name):
    if request.method == "POST":
        inputDemand1 = request.POST.get('demand1')
        inputDemand2 = request.POST.get('demand2')
        inputDemand3 = request.POST.get('demand3')
        inputDemand4 = request.POST.get('demand4')
        inputDemand5 = request.POST.get('demand5')
        inputDemand6 = request.POST.get('demand6')
        inputDemand7 = request.POST.get('demand7')
        inputDemand8 = request.POST.get('demand8')
        inputDemand9 = request.POST.get('demand9')
        inputDemand10 = request.POST.get('demand10')
        models.TenMonthPlan.objects.filter(planName=plan_Name).update(demand1 = inputDemand1, 
                                                                             demand2 = inputDemand2, 
                                                                             demand3 = inputDemand3, 
                                                                             demand4 = inputDemand4, 
                                                                             demand5 = inputDemand5, 
                                                                             demand6 = inputDemand6, 
                                                                             demand7 = inputDemand7, 
                                                                             demand8 = inputDemand8, 
                                                                             demand9 = inputDemand9, 
                                                                             demand10 = inputDemand10
                                                                             )
        return redirect('history')
    else:
        detail = models.TenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Ten/demandTen.html',{'detail' : detail})


def numPermanentTen(request, plan_Name):
    if request.method == "POST":
        inputNumPermanent1 = request.POST.get('numPermanent1')
        inputNumPermanent2 = request.POST.get('numPermanent2')
        inputNumPermanent3 = request.POST.get('numPermanent3')
        inputNumPermanent4 = request.POST.get('numPermanent4')
        inputNumPermanent5 = request.POST.get('numPermanent5')
        inputNumPermanent6 = request.POST.get('numPermanent6')
        inputNumPermanent7 = request.POST.get('numPermanent7')
        inputNumPermanent8 = request.POST.get('numPermanent8')
        inputNumPermanent9 = request.POST.get('numPermanent9')
        inputNumPermanent10 = request.POST.get('numPermanent10')
        models.TenMonthPlan.objects.filter(planName=plan_Name).update(numPermanent1 = inputNumPermanent1, 
                                                                             numPermanent2 = inputNumPermanent2, 
                                                                             numPermanent3 = inputNumPermanent3, 
                                                                             numPermanent4 = inputNumPermanent4, 
                                                                             numPermanent5 = inputNumPermanent5, 
                                                                             numPermanent6 = inputNumPermanent6, 
                                                                             numPermanent7 = inputNumPermanent7, 
                                                                             numPermanent8 = inputNumPermanent8, 
                                                                             numPermanent9 = inputNumPermanent9, 
                                                                             numPermanent10 = inputNumPermanent10
                                                                             )
        return redirect('history')
    else:
        detail = models.TenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Ten/numPermanentTen.html',{'detail' : detail})


def prodPermanentTen(request, plan_Name):
    if request.method == "POST":
        inputProdPermanent1 = request.POST.get('prodPermanent1')
        inputProdPermanent2 = request.POST.get('prodPermanent2')
        inputProdPermanent3 = request.POST.get('prodPermanent3')
        inputProdPermanent4 = request.POST.get('prodPermanent4')
        inputProdPermanent5 = request.POST.get('prodPermanent5')
        inputProdPermanent6 = request.POST.get('prodPermanent6')
        inputProdPermanent7 = request.POST.get('prodPermanent7')
        inputProdPermanent8 = request.POST.get('prodPermanent8')
        inputProdPermanent9 = request.POST.get('prodPermanent9')
        inputProdPermanent10 = request.POST.get('prodPermanent10')
        models.TenMonthPlan.objects.filter(planName=plan_Name).update(prodPermanent1 = inputProdPermanent1, 
                                                                             prodPermanent2 = inputProdPermanent2, 
                                                                             prodPermanent3 = inputProdPermanent3, 
                                                                             prodPermanent4 = inputProdPermanent4, 
                                                                             prodPermanent5 = inputProdPermanent5, 
                                                                             prodPermanent6 = inputProdPermanent6, 
                                                                             prodPermanent7 = inputProdPermanent7, 
                                                                             prodPermanent8 = inputProdPermanent8, 
                                                                             prodPermanent9 = inputProdPermanent9, 
                                                                             prodPermanent10 = inputProdPermanent10
                                                                             )
        return redirect('history')
    else:
        detail = models.TenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Ten/prodPermanentTen.html',{'detail' : detail})


def prodTemporaryTen(request, plan_Name):
    if request.method == "POST":
        inputProdTemporary1 = request.POST.get('prodTemporary1')
        inputProdTemporary2 = request.POST.get('prodTemporary2')
        inputProdTemporary3 = request.POST.get('prodTemporary3')
        inputProdTemporary4 = request.POST.get('prodTemporary4')
        inputProdTemporary5 = request.POST.get('prodTemporary5')
        inputProdTemporary6 = request.POST.get('prodTemporary6')
        inputProdTemporary7 = request.POST.get('prodTemporary7')
        inputProdTemporary8 = request.POST.get('prodTemporary8')
        inputProdTemporary9 = request.POST.get('prodTemporary9')
        inputProdTemporary10 = request.POST.get('prodTemporary10')
        models.TenMonthPlan.objects.filter(planName=plan_Name).update(prodTemporary1 = inputProdTemporary1, 
                                                                             prodTemporary2 = inputProdTemporary2, 
                                                                             prodTemporary3 = inputProdTemporary3, 
                                                                             prodTemporary4 = inputProdTemporary4, 
                                                                             prodTemporary5 = inputProdTemporary5, 
                                                                             prodTemporary6 = inputProdTemporary6, 
                                                                             prodTemporary7 = inputProdTemporary7, 
                                                                             prodTemporary8 = inputProdTemporary8, 
                                                                             prodTemporary9 = inputProdTemporary9, 
                                                                             prodTemporary10 = inputProdTemporary10
                                                                             )
        return redirect('history')
    else:
        detail = models.TenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Ten/prodTemporaryTen.html',{'detail' : detail})


def costHiringTen(request, plan_Name):
    if request.method == "POST":
        inputCostHiring1 = request.POST.get('costHiring1')
        inputCostHiring2 = request.POST.get('costHiring2')
        inputCostHiring3 = request.POST.get('costHiring3')
        inputCostHiring4 = request.POST.get('costHiring4')
        inputCostHiring5 = request.POST.get('costHiring5')
        inputCostHiring6 = request.POST.get('costHiring6')
        inputCostHiring7 = request.POST.get('costHiring7')
        inputCostHiring8 = request.POST.get('costHiring8')
        inputCostHiring9 = request.POST.get('costHiring9')
        inputCostHiring10 = request.POST.get('costHiring10')
        models.TenMonthPlan.objects.filter(planName=plan_Name).update(costHiring1 = inputCostHiring1, 
                                                                             costHiring2 = inputCostHiring2, 
                                                                             costHiring3 = inputCostHiring3, 
                                                                             costHiring4 = inputCostHiring4, 
                                                                             costHiring5 = inputCostHiring5, 
                                                                             costHiring6 = inputCostHiring6, 
                                                                             costHiring7 = inputCostHiring7, 
                                                                             costHiring8 = inputCostHiring8, 
                                                                             costHiring9 = inputCostHiring9, 
                                                                             costHiring10 = inputCostHiring10
                                                                             )
        return redirect('history')
    else:
        detail = models.TenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Ten/costHiringTen.html',{'detail' : detail})


def costFiringTen(request, plan_Name):
    if request.method == "POST":
        inputCostFiring1 = request.POST.get('costFiring1')
        inputCostFiring2 = request.POST.get('costFiring2')
        inputCostFiring3 = request.POST.get('costFiring3')
        inputCostFiring4 = request.POST.get('costFiring4')
        inputCostFiring5 = request.POST.get('costFiring5')
        inputCostFiring6 = request.POST.get('costFiring6')
        inputCostFiring7 = request.POST.get('costFiring7')
        inputCostFiring8 = request.POST.get('costFiring8')
        inputCostFiring9 = request.POST.get('costFiring9')
        inputCostFiring10 = request.POST.get('costFiring10')
        models.TenMonthPlan.objects.filter(planName=plan_Name).update(costFiring1 = inputCostFiring1, 
                                                                             costFiring2 = inputCostFiring2, 
                                                                             costFiring3 = inputCostFiring3, 
                                                                             costFiring4 = inputCostFiring4, 
                                                                             costFiring5 = inputCostFiring5, 
                                                                             costFiring6 = inputCostFiring6, 
                                                                             costFiring7 = inputCostFiring7, 
                                                                             costFiring8 = inputCostFiring8, 
                                                                             costFiring9 = inputCostFiring9, 
                                                                             costFiring10 = inputCostFiring10
                                                                             )
        return redirect('history')
    else:
        detail = models.TenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Ten/costFiringTen.html',{'detail' : detail})


def costHoldingUnitTen(request, plan_Name):
    if request.method == "POST":
        inputCostHoldingUnit1 = request.POST.get('costHoldingUnit1')
        inputCostHoldingUnit2 = request.POST.get('costHoldingUnit2')
        inputCostHoldingUnit3 = request.POST.get('costHoldingUnit3')
        inputCostHoldingUnit4 = request.POST.get('costHoldingUnit4')
        inputCostHoldingUnit5 = request.POST.get('costHoldingUnit5')
        inputCostHoldingUnit6 = request.POST.get('costHoldingUnit6')
        inputCostHoldingUnit7 = request.POST.get('costHoldingUnit7')
        inputCostHoldingUnit8 = request.POST.get('costHoldingUnit8')
        inputCostHoldingUnit9 = request.POST.get('costHoldingUnit9')
        inputCostHoldingUnit10 = request.POST.get('costHoldingUnit10')
        models.TenMonthPlan.objects.filter(planName=plan_Name).update(costHoldingUnit1 = inputCostHoldingUnit1, 
                                                                             costHoldingUnit2 = inputCostHoldingUnit2, 
                                                                             costHoldingUnit3 = inputCostHoldingUnit3, 
                                                                             costHoldingUnit4 = inputCostHoldingUnit4, 
                                                                             costHoldingUnit5 = inputCostHoldingUnit5, 
                                                                             costHoldingUnit6 = inputCostHoldingUnit6, 
                                                                             costHoldingUnit7 = inputCostHoldingUnit7, 
                                                                             costHoldingUnit8 = inputCostHoldingUnit8, 
                                                                             costHoldingUnit9 = inputCostHoldingUnit9, 
                                                                             costHoldingUnit10 = inputCostHoldingUnit10
                                                                             )
        return redirect('history')
    else:
        detail = models.TenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Ten/costHoldingUnitTen.html',{'detail' : detail})


def demandEleven(request, plan_Name):
    if request.method == "POST":
        inputDemand1 = request.POST.get('demand1')
        inputDemand2 = request.POST.get('demand2')
        inputDemand3 = request.POST.get('demand3')
        inputDemand4 = request.POST.get('demand4')
        inputDemand5 = request.POST.get('demand5')
        inputDemand6 = request.POST.get('demand6')
        inputDemand7 = request.POST.get('demand7')
        inputDemand8 = request.POST.get('demand8')
        inputDemand9 = request.POST.get('demand9')
        inputDemand10 = request.POST.get('demand10')
        inputDemand11 = request.POST.get('demand11')
        models.ElevenMonthPlan.objects.filter(planName=plan_Name).update(demand1 = inputDemand1, 
                                                                             demand2 = inputDemand2, 
                                                                             demand3 = inputDemand3, 
                                                                             demand4 = inputDemand4, 
                                                                             demand5 = inputDemand5, 
                                                                             demand6 = inputDemand6, 
                                                                             demand7 = inputDemand7, 
                                                                             demand8 = inputDemand8, 
                                                                             demand9 = inputDemand9, 
                                                                             demand10 = inputDemand10, 
                                                                             demand11 = inputDemand11
                                                                             )
        return redirect('history')
    else:
        detail = models.ElevenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Eleven/demandEleven.html',{'detail' : detail})


def numPermanentEleven(request, plan_Name):
    if request.method == "POST":
        inputNumPermanent1 = request.POST.get('numPermanent1')
        inputNumPermanent2 = request.POST.get('numPermanent2')
        inputNumPermanent3 = request.POST.get('numPermanent3')
        inputNumPermanent4 = request.POST.get('numPermanent4')
        inputNumPermanent5 = request.POST.get('numPermanent5')
        inputNumPermanent6 = request.POST.get('numPermanent6')
        inputNumPermanent7 = request.POST.get('numPermanent7')
        inputNumPermanent8 = request.POST.get('numPermanent8')
        inputNumPermanent9 = request.POST.get('numPermanent9')
        inputNumPermanent10 = request.POST.get('numPermanent10')
        inputNumPermanent11 = request.POST.get('numPermanent11')
        models.ElevenMonthPlan.objects.filter(planName=plan_Name).update(numPermanent1 = inputNumPermanent1, 
                                                                             numPermanent2 = inputNumPermanent2, 
                                                                             numPermanent3 = inputNumPermanent3, 
                                                                             numPermanent4 = inputNumPermanent4, 
                                                                             numPermanent5 = inputNumPermanent5, 
                                                                             numPermanent6 = inputNumPermanent6, 
                                                                             numPermanent7 = inputNumPermanent7, 
                                                                             numPermanent8 = inputNumPermanent8, 
                                                                             numPermanent9 = inputNumPermanent9, 
                                                                             numPermanent10 = inputNumPermanent10, 
                                                                             numPermanent11 = inputNumPermanent11
                                                                             )
        return redirect('history')
    else:
        detail = models.ElevenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Eleven/numPermanentEleven.html',{'detail' : detail})


def prodPermanentEleven(request, plan_Name):
    if request.method == "POST":
        inputProdPermanent1 = request.POST.get('prodPermanent1')
        inputProdPermanent2 = request.POST.get('prodPermanent2')
        inputProdPermanent3 = request.POST.get('prodPermanent3')
        inputProdPermanent4 = request.POST.get('prodPermanent4')
        inputProdPermanent5 = request.POST.get('prodPermanent5')
        inputProdPermanent6 = request.POST.get('prodPermanent6')
        inputProdPermanent7 = request.POST.get('prodPermanent7')
        inputProdPermanent8 = request.POST.get('prodPermanent8')
        inputProdPermanent9 = request.POST.get('prodPermanent9')
        inputProdPermanent10 = request.POST.get('prodPermanent10')
        inputProdPermanent11 = request.POST.get('prodPermanent11')
        models.ElevenMonthPlan.objects.filter(planName=plan_Name).update(prodPermanent1 = inputProdPermanent1, 
                                                                             prodPermanent2 = inputProdPermanent2, 
                                                                             prodPermanent3 = inputProdPermanent3, 
                                                                             prodPermanent4 = inputProdPermanent4, 
                                                                             prodPermanent5 = inputProdPermanent5, 
                                                                             prodPermanent6 = inputProdPermanent6, 
                                                                             prodPermanent7 = inputProdPermanent7, 
                                                                             prodPermanent8 = inputProdPermanent8, 
                                                                             prodPermanent9 = inputProdPermanent9, 
                                                                             prodPermanent10 = inputProdPermanent10, 
                                                                             prodPermanent11 = inputProdPermanent11
                                                                             )
        return redirect('history')
    else:
        detail = models.ElevenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Eleven/prodPermanentEleven.html',{'detail' : detail})


def prodTemporaryEleven(request, plan_Name):
    if request.method == "POST":
        inputProdTemporary1 = request.POST.get('prodTemporary1')
        inputProdTemporary2 = request.POST.get('prodTemporary2')
        inputProdTemporary3 = request.POST.get('prodTemporary3')
        inputProdTemporary4 = request.POST.get('prodTemporary4')
        inputProdTemporary5 = request.POST.get('prodTemporary5')
        inputProdTemporary6 = request.POST.get('prodTemporary6')
        inputProdTemporary7 = request.POST.get('prodTemporary7')
        inputProdTemporary8 = request.POST.get('prodTemporary8')
        inputProdTemporary9 = request.POST.get('prodTemporary9')
        inputProdTemporary10 = request.POST.get('prodTemporary10')
        inputProdTemporary11 = request.POST.get('prodTemporary11')
        models.ElevenMonthPlan.objects.filter(planName=plan_Name).update(prodTemporary1 = inputProdTemporary1, 
                                                                             prodTemporary2 = inputProdTemporary2, 
                                                                             prodTemporary3 = inputProdTemporary3, 
                                                                             prodTemporary4 = inputProdTemporary4, 
                                                                             prodTemporary5 = inputProdTemporary5, 
                                                                             prodTemporary6 = inputProdTemporary6, 
                                                                             prodTemporary7 = inputProdTemporary7, 
                                                                             prodTemporary8 = inputProdTemporary8, 
                                                                             prodTemporary9 = inputProdTemporary9, 
                                                                             prodTemporary10 = inputProdTemporary10, 
                                                                             prodTemporary11 = inputProdTemporary11
                                                                             )
        return redirect('history')
    else:
        detail = models.ElevenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Eleven/prodTemporaryEleven.html',{'detail' : detail})


def costHiringEleven(request, plan_Name):
    if request.method == "POST":
        inputCostHiring1 = request.POST.get('costHiring1')
        inputCostHiring2 = request.POST.get('costHiring2')
        inputCostHiring3 = request.POST.get('costHiring3')
        inputCostHiring4 = request.POST.get('costHiring4')
        inputCostHiring5 = request.POST.get('costHiring5')
        inputCostHiring6 = request.POST.get('costHiring6')
        inputCostHiring7 = request.POST.get('costHiring7')
        inputCostHiring8 = request.POST.get('costHiring8')
        inputCostHiring9 = request.POST.get('costHiring9')
        inputCostHiring10 = request.POST.get('costHiring10')
        inputCostHiring11 = request.POST.get('costHiring11')
        models.ElevenMonthPlan.objects.filter(planName=plan_Name).update(costHiring1 = inputCostHiring1, 
                                                                             costHiring2 = inputCostHiring2, 
                                                                             costHiring3 = inputCostHiring3, 
                                                                             costHiring4 = inputCostHiring4, 
                                                                             costHiring5 = inputCostHiring5, 
                                                                             costHiring6 = inputCostHiring6, 
                                                                             costHiring7 = inputCostHiring7, 
                                                                             costHiring8 = inputCostHiring8, 
                                                                             costHiring9 = inputCostHiring9, 
                                                                             costHiring10 = inputCostHiring10, 
                                                                             costHiring11 = inputCostHiring11
                                                                             )
        return redirect('history')
    else:
        detail = models.ElevenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Eleven/costHiringEleven.html',{'detail' : detail})


def costFiringEleven(request, plan_Name):
    if request.method == "POST":
        inputCostFiring1 = request.POST.get('costFiring1')
        inputCostFiring2 = request.POST.get('costFiring2')
        inputCostFiring3 = request.POST.get('costFiring3')
        inputCostFiring4 = request.POST.get('costFiring4')
        inputCostFiring5 = request.POST.get('costFiring5')
        inputCostFiring6 = request.POST.get('costFiring6')
        inputCostFiring7 = request.POST.get('costFiring7')
        inputCostFiring8 = request.POST.get('costFiring8')
        inputCostFiring9 = request.POST.get('costFiring9')
        inputCostFiring10 = request.POST.get('costFiring10')
        inputCostFiring11 = request.POST.get('costFiring11')
        models.ElevenMonthPlan.objects.filter(planName=plan_Name).update(costFiring1 = inputCostFiring1, 
                                                                             costFiring2 = inputCostFiring2, 
                                                                             costFiring3 = inputCostFiring3, 
                                                                             costFiring4 = inputCostFiring4, 
                                                                             costFiring5 = inputCostFiring5, 
                                                                             costFiring6 = inputCostFiring6, 
                                                                             costFiring7 = inputCostFiring7, 
                                                                             costFiring8 = inputCostFiring8, 
                                                                             costFiring9 = inputCostFiring9, 
                                                                             costFiring10 = inputCostFiring10, 
                                                                             costFiring11 = inputCostFiring11
                                                                             )
        return redirect('history')
    else:
        detail = models.ElevenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Eleven/costFiringEleven.html',{'detail' : detail})


def costHoldingUnitEleven(request, plan_Name):
    if request.method == "POST":
        inputCostHoldingUnit1 = request.POST.get('costHoldingUnit1')
        inputCostHoldingUnit2 = request.POST.get('costHoldingUnit2')
        inputCostHoldingUnit3 = request.POST.get('costHoldingUnit3')
        inputCostHoldingUnit4 = request.POST.get('costHoldingUnit4')
        inputCostHoldingUnit5 = request.POST.get('costHoldingUnit5')
        inputCostHoldingUnit6 = request.POST.get('costHoldingUnit6')
        inputCostHoldingUnit7 = request.POST.get('costHoldingUnit7')
        inputCostHoldingUnit8 = request.POST.get('costHoldingUnit8')
        inputCostHoldingUnit9 = request.POST.get('costHoldingUnit9')
        inputCostHoldingUnit10 = request.POST.get('costHoldingUnit10')
        inputCostHoldingUnit11 = request.POST.get('costHoldingUnit11')
        models.ElevenMonthPlan.objects.filter(planName=plan_Name).update(costHoldingUnit1 = inputCostHoldingUnit1, 
                                                                             costHoldingUnit2 = inputCostHoldingUnit2, 
                                                                             costHoldingUnit3 = inputCostHoldingUnit3, 
                                                                             costHoldingUnit4 = inputCostHoldingUnit4, 
                                                                             costHoldingUnit5 = inputCostHoldingUnit5, 
                                                                             costHoldingUnit6 = inputCostHoldingUnit6, 
                                                                             costHoldingUnit7 = inputCostHoldingUnit7, 
                                                                             costHoldingUnit8 = inputCostHoldingUnit8, 
                                                                             costHoldingUnit9 = inputCostHoldingUnit9, 
                                                                             costHoldingUnit10 = inputCostHoldingUnit10, 
                                                                             costHoldingUnit11 = inputCostHoldingUnit11 
                                                                             )
        return redirect('history')
    else:
        detail = models.ElevenMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Eleven/costHoldingUnitEleven.html',{'detail' : detail})


def demandTwelve(request, plan_Name):
    if request.method == "POST":
        inputDemand1 = request.POST.get('demand1')
        inputDemand2 = request.POST.get('demand2')
        inputDemand3 = request.POST.get('demand3')
        inputDemand4 = request.POST.get('demand4')
        inputDemand5 = request.POST.get('demand5')
        inputDemand6 = request.POST.get('demand6')
        inputDemand7 = request.POST.get('demand7')
        inputDemand8 = request.POST.get('demand8')
        inputDemand9 = request.POST.get('demand9')
        inputDemand10 = request.POST.get('demand10')
        inputDemand11 = request.POST.get('demand11')
        inputDemand12 = request.POST.get('demand12')
        models.TwelveMonthPlan.objects.filter(planName=plan_Name).update(demand1 = inputDemand1, 
                                                                             demand2 = inputDemand2, 
                                                                             demand3 = inputDemand3, 
                                                                             demand4 = inputDemand4, 
                                                                             demand5 = inputDemand5, 
                                                                             demand6 = inputDemand6, 
                                                                             demand7 = inputDemand7, 
                                                                             demand8 = inputDemand8, 
                                                                             demand9 = inputDemand9, 
                                                                             demand10 = inputDemand10, 
                                                                             demand11 = inputDemand11, 
                                                                             demand12 = inputDemand12
                                                                             )
        return redirect('history')
    else:
        detail = models.TwelveMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Twelve/demandTwelve.html',{'detail' : detail})


def numPermanentTwelve(request, plan_Name):
    if request.method == "POST":
        inputNumPermanent1 = request.POST.get('numPermanent1')
        inputNumPermanent2 = request.POST.get('numPermanent2')
        inputNumPermanent3 = request.POST.get('numPermanent3')
        inputNumPermanent4 = request.POST.get('numPermanent4')
        inputNumPermanent5 = request.POST.get('numPermanent5')
        inputNumPermanent6 = request.POST.get('numPermanent6')
        inputNumPermanent7 = request.POST.get('numPermanent7')
        inputNumPermanent8 = request.POST.get('numPermanent8')
        inputNumPermanent9 = request.POST.get('numPermanent9')
        inputNumPermanent10 = request.POST.get('numPermanent10')
        inputNumPermanent11 = request.POST.get('numPermanent11')
        inputNumPermanent12 = request.POST.get('numPermanent12')
        models.TwelveMonthPlan.objects.filter(planName=plan_Name).update(numPermanent1 = inputNumPermanent1, 
                                                                             numPermanent2 = inputNumPermanent2, 
                                                                             numPermanent3 = inputNumPermanent3, 
                                                                             numPermanent4 = inputNumPermanent4, 
                                                                             numPermanent5 = inputNumPermanent5, 
                                                                             numPermanent6 = inputNumPermanent6, 
                                                                             numPermanent7 = inputNumPermanent7, 
                                                                             numPermanent8 = inputNumPermanent8, 
                                                                             numPermanent9 = inputNumPermanent9, 
                                                                             numPermanent10 = inputNumPermanent10, 
                                                                             numPermanent11 = inputNumPermanent11, 
                                                                             numPermanent12 = inputNumPermanent12
                                                                             )
        return redirect('history')
    else:
        detail = models.TwelveMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Twelve/numPermanentTwelve.html',{'detail' : detail})


def prodPermanentTwelve(request, plan_Name):
    if request.method == "POST":
        inputProdPermanent1 = request.POST.get('prodPermanent1')
        inputProdPermanent2 = request.POST.get('prodPermanent2')
        inputProdPermanent3 = request.POST.get('prodPermanent3')
        inputProdPermanent4 = request.POST.get('prodPermanent4')
        inputProdPermanent5 = request.POST.get('prodPermanent5')
        inputProdPermanent6 = request.POST.get('prodPermanent6')
        inputProdPermanent7 = request.POST.get('prodPermanent7')
        inputProdPermanent8 = request.POST.get('prodPermanent8')
        inputProdPermanent9 = request.POST.get('prodPermanent9')
        inputProdPermanent10 = request.POST.get('prodPermanent10')
        inputProdPermanent11 = request.POST.get('prodPermanent11')
        inputProdPermanent12 = request.POST.get('prodPermanent12')
        models.TwelveMonthPlan.objects.filter(planName=plan_Name).update(prodPermanent1 = inputProdPermanent1, 
                                                                             prodPermanent2 = inputProdPermanent2, 
                                                                             prodPermanent3 = inputProdPermanent3, 
                                                                             prodPermanent4 = inputProdPermanent4, 
                                                                             prodPermanent5 = inputProdPermanent5, 
                                                                             prodPermanent6 = inputProdPermanent6, 
                                                                             prodPermanent7 = inputProdPermanent7, 
                                                                             prodPermanent8 = inputProdPermanent8, 
                                                                             prodPermanent9 = inputProdPermanent9, 
                                                                             prodPermanent10 = inputProdPermanent10, 
                                                                             prodPermanent11 = inputProdPermanent11, 
                                                                             prodPermanent12 = inputProdPermanent12
                                                                             )
        return redirect('history')
    else:
        detail = models.TwelveMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Twelve/prodPermanentTwelve.html',{'detail' : detail})


def prodTemporaryTwelve(request, plan_Name):
    if request.method == "POST":
        inputProdTemporary1 = request.POST.get('prodTemporary1')
        inputProdTemporary2 = request.POST.get('prodTemporary2')
        inputProdTemporary3 = request.POST.get('prodTemporary3')
        inputProdTemporary4 = request.POST.get('prodTemporary4')
        inputProdTemporary5 = request.POST.get('prodTemporary5')
        inputProdTemporary6 = request.POST.get('prodTemporary6')
        inputProdTemporary7 = request.POST.get('prodTemporary7')
        inputProdTemporary8 = request.POST.get('prodTemporary8')
        inputProdTemporary9 = request.POST.get('prodTemporary9')
        inputProdTemporary10 = request.POST.get('prodTemporary10')
        inputProdTemporary11 = request.POST.get('prodTemporary11')
        inputProdTemporary12 = request.POST.get('prodTemporary12')
        models.TwelveMonthPlan.objects.filter(planName=plan_Name).update(prodTemporary1 = inputProdTemporary1, 
                                                                             prodTemporary2 = inputProdTemporary2, 
                                                                             prodTemporary3 = inputProdTemporary3, 
                                                                             prodTemporary4 = inputProdTemporary4, 
                                                                             prodTemporary5 = inputProdTemporary5, 
                                                                             prodTemporary6 = inputProdTemporary6, 
                                                                             prodTemporary7 = inputProdTemporary7, 
                                                                             prodTemporary8 = inputProdTemporary8, 
                                                                             prodTemporary9 = inputProdTemporary9, 
                                                                             prodTemporary10 = inputProdTemporary10, 
                                                                             prodTemporary11 = inputProdTemporary11, 
                                                                             prodTemporary12 = inputProdTemporary12
                                                                             )
        return redirect('history')
    else:
        detail = models.TwelveMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Twelve/prodTemporaryTwelve.html',{'detail' : detail})


def costHiringTwelve(request, plan_Name):
    if request.method == "POST":
        inputCostHiring1 = request.POST.get('costHiring1')
        inputCostHiring2 = request.POST.get('costHiring2')
        inputCostHiring3 = request.POST.get('costHiring3')
        inputCostHiring4 = request.POST.get('costHiring4')
        inputCostHiring5 = request.POST.get('costHiring5')
        inputCostHiring6 = request.POST.get('costHiring6')
        inputCostHiring7 = request.POST.get('costHiring7')
        inputCostHiring8 = request.POST.get('costHiring8')
        inputCostHiring9 = request.POST.get('costHiring9')
        inputCostHiring10 = request.POST.get('costHiring10')
        inputCostHiring11 = request.POST.get('costHiring11')
        inputCostHiring12 = request.POST.get('costHiring12')
        models.TwelveMonthPlan.objects.filter(planName=plan_Name).update(costHiring1 = inputCostHiring1, 
                                                                             costHiring2 = inputCostHiring2, 
                                                                             costHiring3 = inputCostHiring3, 
                                                                             costHiring4 = inputCostHiring4, 
                                                                             costHiring5 = inputCostHiring5, 
                                                                             costHiring6 = inputCostHiring6, 
                                                                             costHiring7 = inputCostHiring7, 
                                                                             costHiring8 = inputCostHiring8, 
                                                                             costHiring9 = inputCostHiring9, 
                                                                             costHiring10 = inputCostHiring10, 
                                                                             costHiring11 = inputCostHiring11, 
                                                                             costHiring12 = inputCostHiring12
                                                                             )
        return redirect('history')
    else:
        detail = models.TwelveMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Twelve/costHiringTwelve.html',{'detail' : detail})


def costFiringTwelve(request, plan_Name):
    if request.method == "POST":
        inputCostFiring1 = request.POST.get('costFiring1')
        inputCostFiring2 = request.POST.get('costFiring2')
        inputCostFiring3 = request.POST.get('costFiring3')
        inputCostFiring4 = request.POST.get('costFiring4')
        inputCostFiring5 = request.POST.get('costFiring5')
        inputCostFiring6 = request.POST.get('costFiring6')
        inputCostFiring7 = request.POST.get('costFiring7')
        inputCostFiring8 = request.POST.get('costFiring8')
        inputCostFiring9 = request.POST.get('costFiring9')
        inputCostFiring10 = request.POST.get('costFiring10')
        inputCostFiring11 = request.POST.get('costFiring11')
        inputCostFiring12 = request.POST.get('costFiring12')
        models.TwelveMonthPlan.objects.filter(planName=plan_Name).update(costFiring1 = inputCostFiring1, 
                                                                             costFiring2 = inputCostFiring2, 
                                                                             costFiring3 = inputCostFiring3, 
                                                                             costFiring4 = inputCostFiring4, 
                                                                             costFiring5 = inputCostFiring5, 
                                                                             costFiring6 = inputCostFiring6, 
                                                                             costFiring7 = inputCostFiring7, 
                                                                             costFiring8 = inputCostFiring8, 
                                                                             costFiring9 = inputCostFiring9, 
                                                                             costFiring10 = inputCostFiring10, 
                                                                             costFiring11 = inputCostFiring11, 
                                                                             costFiring12 = inputCostFiring12
                                                                             )
        return redirect('history')
    else:
        detail = models.TwelveMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Twelve/costFiringTwelve.html',{'detail' : detail})


def costHoldingUnitTwelve(request, plan_Name):
    if request.method == "POST":
        inputCostHoldingUnit1 = request.POST.get('costHoldingUnit1')
        inputCostHoldingUnit2 = request.POST.get('costHoldingUnit2')
        inputCostHoldingUnit3 = request.POST.get('costHoldingUnit3')
        inputCostHoldingUnit4 = request.POST.get('costHoldingUnit4')
        inputCostHoldingUnit5 = request.POST.get('costHoldingUnit5')
        inputCostHoldingUnit6 = request.POST.get('costHoldingUnit6')
        inputCostHoldingUnit7 = request.POST.get('costHoldingUnit7')
        inputCostHoldingUnit8 = request.POST.get('costHoldingUnit8')
        inputCostHoldingUnit9 = request.POST.get('costHoldingUnit9')
        inputCostHoldingUnit10 = request.POST.get('costHoldingUnit10')
        inputCostHoldingUnit11 = request.POST.get('costHoldingUnit11')
        inputCostHoldingUnit12 = request.POST.get('costHoldingUnit12')
        models.TwelveMonthPlan.objects.filter(planName=plan_Name).update(costHoldingUnit1 = inputCostHoldingUnit1, 
                                                                             costHoldingUnit2 = inputCostHoldingUnit2, 
                                                                             costHoldingUnit3 = inputCostHoldingUnit3, 
                                                                             costHoldingUnit4 = inputCostHoldingUnit4, 
                                                                             costHoldingUnit5 = inputCostHoldingUnit5, 
                                                                             costHoldingUnit6 = inputCostHoldingUnit6, 
                                                                             costHoldingUnit7 = inputCostHoldingUnit7, 
                                                                             costHoldingUnit8 = inputCostHoldingUnit8, 
                                                                             costHoldingUnit9 = inputCostHoldingUnit9, 
                                                                             costHoldingUnit10 = inputCostHoldingUnit10, 
                                                                             costHoldingUnit11 = inputCostHoldingUnit11, 
                                                                             costHoldingUnit12 = inputCostHoldingUnit12
                                                                             )
        return redirect('history')
    else:
        detail = models.TwelveMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/Twelve/costHoldingUnitTwelve.html',{'detail' : detail})

def inventoryInitialFinal(request, month, plan_Name):
    if request.method == "POST":
        inputInventoryInitial = request.POST.get('inventoryInitial')
        inputInventoryFinal = request.POST.get('inventoryFinal')
        if month == "Four":
            models.FourMonthPlan.objects.filter(planName = plan_Name).update(inventoryInitial= inputInventoryInitial, inventoryFinal= inputInventoryFinal)
        elif month == "Five":
            models.FiveMonthPlan.objects.filter(planName = plan_Name).update(inventoryInitial= inputInventoryInitial, inventoryFinal= inputInventoryFinal)
        elif month == "Six":
            models.SixMonthPlan.objects.filter(planName = plan_Name).update(inventoryInitial= inputInventoryInitial, inventoryFinal= inputInventoryFinal)
        elif month == "Seven":
            models.SevenMonthPlan.objects.filter(planName = plan_Name).update(inventoryInitial= inputInventoryInitial, inventoryFinal= inputInventoryFinal)
        elif month == "Eight":
            models.EightMonthPlan.objects.filter(planName = plan_Name).update(inventoryInitial= inputInventoryInitial, inventoryFinal= inputInventoryFinal)
        elif month == "Nine":
            models.NineMonthPlan.objects.filter(planName = plan_Name).update(inventoryInitial= inputInventoryInitial, inventoryFinal= inputInventoryFinal)
        elif month == "Ten":
            models.TenMonthPlan.objects.filter(planName = plan_Name).update(inventoryInitial= inputInventoryInitial, inventoryFinal= inputInventoryFinal)
        elif month == "Eleven":
            models.ElevenMonthPlan.objects.filter(planName = plan_Name).update(inventoryInitial= inputInventoryInitial, inventoryFinal= inputInventoryFinal)
        elif month == "Twelve":
            models.TwelveMonthPlan.objects.filter(planName = plan_Name).update(inventoryInitial= inputInventoryInitial, inventoryFinal= inputInventoryFinal)
        return redirect('history')
    else:
        if month == "Four":
            detail = models.FourMonthPlan.objects.filter(planName = plan_Name).values()
        elif month == "Five":
            detail = models.FiveMonthPlan.objects.filter(planName = plan_Name).values()
        elif month == "Six":
            detail = models.SixMonthPlan.objects.filter(planName = plan_Name).values()
        elif month == "Seven":
            detail = models.SevenMonthPlan.objects.filter(planName = plan_Name).values()
        elif month == "Eight":
            detail = models.EightMonthPlan.objects.filter(planName = plan_Name).values()
        elif month == "Nine":
            detail = models.NineMonthPlan.objects.filter(planName = plan_Name).values()
        elif month == "Ten":
            detail = models.TenMonthPlan.objects.filter(planName = plan_Name).values()
        elif month == "Eleven":
            detail = models.ElevenMonthPlan.objects.filter(planName = plan_Name).values()
        elif month == "Twelve":
            detail = models.TwelveMonthPlan.objects.filter(planName = plan_Name).values()
    return render(request, 'main/inventoryInitialFinal.html',{'detail' : detail})

style_head_row = xlwt.easyxf("""    
        align:
        wrap off,
        vert center,
        horiz center;
        borders:
        left THIN,
        right THIN,
        top THIN,
        bottom THIN;
        font:
        name Arial,
        colour_index white,
        bold on,
        height 0xA0;
        pattern:
        pattern solid,
        fore-colour 0x19;
        """
    )

    # Define worksheet data row style. 
style_data_row = xlwt.easyxf("""
        align:
        wrap on,
        vert center,
        horiz left;
        font:
        name Arial,
        bold off,
        height 0XA0;
        borders:
        left THIN,
        right THIN,
        top THIN,
        bottom THIN;
        """
    )


# Define a green color style.
style_green = xlwt.easyxf(" pattern: fore-colour 0x11, pattern solid;")

# Define a red color style.
style_red = xlwt.easyxf(" pattern: fore-colour 0x0A, pattern solid;")

def downloadFour(request,plan_Name):
    response = HttpResponse(content_type='application/vnd.ms-excel') 
    response['Content-Disposition'] = 'attachment;filename=viewFour.xls'
    work_book = xlwt.Workbook(encoding = 'utf-8') 
    work_sheet = work_book.add_sheet(u'plan details')

    
    
    plan = models.FourMonthPlan.objects.filter(planName=plan_Name).values()
    for x in plan:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        thC = hC1 + hC2 + hC3 + hC4
        tfC = fC1 + fC2 + fC3 + fC4
        tihC = ihc1 + ihc2 + ihc3 + ihc4
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryFinal']
        optimalCost= x['optimalCost']
    work_sheet.write(0,0, 'MONTH', style_head_row) 
    work_sheet.write(0,1, 'REMAINING DEMAND', style_head_row) 
    work_sheet.write(0,2, 'ENDING INVENTORY UNIT(S)', style_head_row) 
    work_sheet.write(0,3, 'NUMBER OF TEMPORARY WORKER HIRED', style_head_row) 
    work_sheet.write(0,4, 'NUMBER OF TEMPORARY WORKER FIRED', style_head_row) 
    work_sheet.write(0,5, 'NUMBER OF TEMPORARY WORKER(S)', style_head_row) 
    work_sheet.write(0,6, 'HIRING COST', style_head_row) 
    work_sheet.write(0,7, 'FIRING COST', style_head_row) 
    work_sheet.write(0,8, 'INVENTORY HOLDING COST', style_head_row)

    work_sheet.write(1,0, 'MONTH 1', style_data_row) 
    work_sheet.write(1,1, rd1, style_data_row) 
    work_sheet.write(1,2, ei1, style_data_row) 
    work_sheet.write(1,3, ntwH1, style_data_row) 
    work_sheet.write(1,4, ntwF1, style_data_row) 
    work_sheet.write(1,5,ntw1, style_data_row) 
    work_sheet.write(1,6, hC1, style_data_row) 
    work_sheet.write(1,7, fC1, style_data_row) 
    work_sheet.write(1,8, ihc1, style_data_row)

    work_sheet.write(2,0, 'MONTH 2', style_data_row) 
    work_sheet.write(2,1, rd2, style_data_row) 
    work_sheet.write(2,2, ei2, style_data_row) 
    work_sheet.write(2,3, ntwH2, style_data_row) 
    work_sheet.write(2,4, ntwF2, style_data_row) 
    work_sheet.write(2,5,ntw2, style_data_row) 
    work_sheet.write(2,6, hC2, style_data_row) 
    work_sheet.write(2,7, fC2, style_data_row) 
    work_sheet.write(2,8, ihc2, style_data_row)

    work_sheet.write(3,0, 'MONTH 3', style_data_row) 
    work_sheet.write(3,1, rd3, style_data_row) 
    work_sheet.write(3,2, ei3, style_data_row) 
    work_sheet.write(3,3, ntwH3, style_data_row) 
    work_sheet.write(3,4, ntwF3, style_data_row) 
    work_sheet.write(3,5,ntw3, style_data_row) 
    work_sheet.write(3,6, hC3, style_data_row) 
    work_sheet.write(3,7, fC3, style_data_row) 
    work_sheet.write(3,8, ihc3, style_data_row)

    work_sheet.write(4,0, 'MONTH 4', style_data_row) 
    work_sheet.write(4,1, rd4, style_data_row) 
    work_sheet.write(4,2, ei4, style_data_row) 
    work_sheet.write(4,3, ntwH4, style_data_row) 
    work_sheet.write(4,4, ntwF4, style_data_row) 
    work_sheet.write(4,5, ntw4, style_data_row) 
    work_sheet.write(4,6, hC4, style_data_row) 
    work_sheet.write(4,7, fC4, style_data_row) 
    work_sheet.write(4,8, ihc4, style_data_row)

    work_sheet.write(5,0,'TOTAL INDIVIDUAL COSTS',style_data_row)
    work_sheet.write(5,6,thC,style_data_row)
    work_sheet.write(5,7,tfC,style_data_row)
    work_sheet.write(5,8,tihC,style_data_row)

    work_sheet.write(6,0,"OPTIMIZED FINAL COST FOR MULTI-PERIOD PLANNING",style_data_row)
    work_sheet.write(6,7,optimalCost,style_data_row)

    output = BytesIO()
    work_book.save(output)
    output.seek(0)
    response.write(output.getvalue()) 

    return response

def downloadFive(request,plan_Name):
    response = HttpResponse(content_type='application/vnd.ms-excel') 
    response['Content-Disposition'] = 'attachment;filename=viewFive.xls'
    work_book = xlwt.Workbook(encoding = 'utf-8') 
    work_sheet = work_book.add_sheet(u'plan details')

    
     
    plan = models.FiveMonthPlan.objects.filter(planName=plan_Name).values()
    for x in plan:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        ntwH5 = x['hiredTemporary5']
        ntwF5 = x['firedTemporary5']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryMonth4']
        rd5 = x['demand5'] - (x['numPermanent5'] * x['prodPermanent5'])
        if rd5 < 0:
            rd5 = 0
        hC5 = ntwH5 * x['costHiring5']
        fC5 = ntwF5 * x['costFiring5']
        ihc5 = x['costHoldingUnit5'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        ntw5 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5
        thC = hC1 + hC2 + hC3 + hC4 + hC5
        tfC = fC1 + fC2 + fC3 + fC4 + fC5
        tihC = ihc1 + ihc2 + ihc3 + ihc4 + ihc5
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryMonth4']
        ei5 = x['inventoryFinal']
        optimalCost= x['optimalCost']
    work_sheet.write(0,0, 'MONTH', style_head_row) 
    work_sheet.write(0,1, 'REMAINING DEMAND', style_head_row) 
    work_sheet.write(0,2, 'ENDING INVENTORY UNIT(S)', style_head_row) 
    work_sheet.write(0,3, 'NUMBER OF TEMPORARY WORKER HIRED', style_head_row) 
    work_sheet.write(0,4, 'NUMBER OF TEMPORARY WORKER FIRED', style_head_row) 
    work_sheet.write(0,5, 'NUMBER OF TEMPORARY WORKER(S)', style_head_row) 
    work_sheet.write(0,6, 'HIRING COST', style_head_row) 
    work_sheet.write(0,7, 'FIRING COST', style_head_row) 
    work_sheet.write(0,8, 'INVENTORY HOLDING COST', style_head_row)

    work_sheet.write(1,0, 'MONTH 1', style_data_row) 
    work_sheet.write(1,1, rd1, style_data_row) 
    work_sheet.write(1,2, ei1, style_data_row) 
    work_sheet.write(1,3, ntwH1, style_data_row) 
    work_sheet.write(1,4, ntwF1, style_data_row) 
    work_sheet.write(1,5,ntw1, style_data_row) 
    work_sheet.write(1,6, hC1, style_data_row) 
    work_sheet.write(1,7, fC1, style_data_row) 
    work_sheet.write(1,8, ihc1, style_data_row)

    work_sheet.write(2,0, 'MONTH 2', style_data_row) 
    work_sheet.write(2,1, rd2, style_data_row) 
    work_sheet.write(2,2, ei2, style_data_row) 
    work_sheet.write(2,3, ntwH2, style_data_row) 
    work_sheet.write(2,4, ntwF2, style_data_row) 
    work_sheet.write(2,5,ntw2, style_data_row) 
    work_sheet.write(2,6, hC2, style_data_row) 
    work_sheet.write(2,7, fC2, style_data_row) 
    work_sheet.write(2,8, ihc2, style_data_row)

    work_sheet.write(3,0, 'MONTH 3', style_data_row) 
    work_sheet.write(3,1, rd3, style_data_row) 
    work_sheet.write(3,2, ei3, style_data_row) 
    work_sheet.write(3,3, ntwH3, style_data_row) 
    work_sheet.write(3,4, ntwF3, style_data_row) 
    work_sheet.write(3,5,ntw3, style_data_row) 
    work_sheet.write(3,6, hC3, style_data_row) 
    work_sheet.write(3,7, fC3, style_data_row) 
    work_sheet.write(3,8, ihc3, style_data_row)

    work_sheet.write(4,0, 'MONTH 4', style_data_row) 
    work_sheet.write(4,1, rd4, style_data_row) 
    work_sheet.write(4,2, ei4, style_data_row) 
    work_sheet.write(4,3, ntwH4, style_data_row) 
    work_sheet.write(4,4, ntwF4, style_data_row) 
    work_sheet.write(4,5, ntw4, style_data_row) 
    work_sheet.write(4,6, hC4, style_data_row) 
    work_sheet.write(4,7, fC4, style_data_row) 
    work_sheet.write(4,8, ihc4, style_data_row)

    work_sheet.write(5,0, 'MONTH 5', style_data_row) 
    work_sheet.write(5,1, rd5, style_data_row) 
    work_sheet.write(5,2, ei5, style_data_row) 
    work_sheet.write(5,3, ntwH5, style_data_row) 
    work_sheet.write(5,4, ntwF5, style_data_row) 
    work_sheet.write(5,5, ntw5, style_data_row) 
    work_sheet.write(5,6, hC5, style_data_row) 
    work_sheet.write(5,7, fC5, style_data_row) 
    work_sheet.write(5,8, ihc5, style_data_row)
    work_sheet.write(6,0,'TOTAL INDIVIDUAL COSTS',style_data_row)
    work_sheet.write(6,6,thC,style_data_row)
    work_sheet.write(6,7,tfC,style_data_row)
    work_sheet.write(6,8,tihC,style_data_row)

    work_sheet.write(7,0,"OPTIMIZED FINAL COST FOR MULTI-PERIOD PLANNING",style_data_row)
    work_sheet.write(7,7,optimalCost,style_data_row)

    output = BytesIO()
    work_book.save(output)
    output.seek(0)
    response.write(output.getvalue()) 

    return response


def downloadSix(request,plan_Name):
    response = HttpResponse(content_type='application/vnd.ms-excel') 
    response['Content-Disposition'] = 'attachment;filename=viewSix.xls'
    work_book = xlwt.Workbook(encoding = 'utf-8') 
    work_sheet = work_book.add_sheet(u'plan details')

    
     
    plan = models.SixMonthPlan.objects.filter(planName=plan_Name).values()
    for x in plan:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        ntwH5 = x['hiredTemporary5']
        ntwF5 = x['firedTemporary5']
        ntwH6 = x['hiredTemporary6']
        ntwF6 = x['firedTemporary6']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryMonth4']
        rd5 = x['demand5'] - (x['numPermanent5'] * x['prodPermanent5'])
        if rd5 < 0:
            rd5 = 0
        hC5 = ntwH5 * x['costHiring5']
        fC5 = ntwF5 * x['costFiring5']
        ihc5 = x['costHoldingUnit5'] * x['inventoryMonth5']
        rd6 = x['demand6'] - (x['numPermanent6'] * x['prodPermanent6'])
        if rd6 < 0:
            rd6 = 0
        hC6 = ntwH6 * x['costHiring6']
        fC6 = ntwF6 * x['costFiring6']
        ihc6 = x['costHoldingUnit6'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        ntw5 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5
        ntw6 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6
        thC = hC1 + hC2 + hC3 + hC4 + hC5 + hC6
        tfC = fC1 + fC2 + fC3 + fC4 + fC5 + fC6
        tihC = ihc1 + ihc2 + ihc3 + ihc4 + ihc5 + ihc6
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryMonth4']
        ei5 = x['inventoryMonth5']
        ei6 = x['inventoryFinal']
        optimalCost= x['optimalCost']
    work_sheet.write(0,0, 'MONTH', style_head_row) 
    work_sheet.write(0,1, 'REMAINING DEMAND', style_head_row) 
    work_sheet.write(0,2, 'ENDING INVENTORY UNIT(S)', style_head_row) 
    work_sheet.write(0,3, 'NUMBER OF TEMPORARY WORKER HIRED', style_head_row) 
    work_sheet.write(0,4, 'NUMBER OF TEMPORARY WORKER FIRED', style_head_row) 
    work_sheet.write(0,5, 'NUMBER OF TEMPORARY WORKER(S)', style_head_row) 
    work_sheet.write(0,6, 'HIRING COST', style_head_row) 
    work_sheet.write(0,7, 'FIRING COST', style_head_row) 
    work_sheet.write(0,8, 'INVENTORY HOLDING COST', style_head_row)

    work_sheet.write(1,0, 'MONTH 1', style_data_row) 
    work_sheet.write(1,1, rd1, style_data_row) 
    work_sheet.write(1,2, ei1, style_data_row) 
    work_sheet.write(1,3, ntwH1, style_data_row) 
    work_sheet.write(1,4, ntwF1, style_data_row) 
    work_sheet.write(1,5,ntw1, style_data_row) 
    work_sheet.write(1,6, hC1, style_data_row) 
    work_sheet.write(1,7, fC1, style_data_row) 
    work_sheet.write(1,8, ihc1, style_data_row)

    work_sheet.write(2,0, 'MONTH 2', style_data_row) 
    work_sheet.write(2,1, rd2, style_data_row) 
    work_sheet.write(2,2, ei2, style_data_row) 
    work_sheet.write(2,3, ntwH2, style_data_row) 
    work_sheet.write(2,4, ntwF2, style_data_row) 
    work_sheet.write(2,5,ntw2, style_data_row) 
    work_sheet.write(2,6, hC2, style_data_row) 
    work_sheet.write(2,7, fC2, style_data_row) 
    work_sheet.write(2,8, ihc2, style_data_row)

    work_sheet.write(3,0, 'MONTH 3', style_data_row) 
    work_sheet.write(3,1, rd3, style_data_row) 
    work_sheet.write(3,2, ei3, style_data_row) 
    work_sheet.write(3,3, ntwH3, style_data_row) 
    work_sheet.write(3,4, ntwF3, style_data_row) 
    work_sheet.write(3,5,ntw3, style_data_row) 
    work_sheet.write(3,6, hC3, style_data_row) 
    work_sheet.write(3,7, fC3, style_data_row) 
    work_sheet.write(3,8, ihc3, style_data_row)

    work_sheet.write(4,0, 'MONTH 4', style_data_row) 
    work_sheet.write(4,1, rd4, style_data_row) 
    work_sheet.write(4,2, ei4, style_data_row) 
    work_sheet.write(4,3, ntwH4, style_data_row) 
    work_sheet.write(4,4, ntwF4, style_data_row) 
    work_sheet.write(4,5, ntw4, style_data_row) 
    work_sheet.write(4,6, hC4, style_data_row) 
    work_sheet.write(4,7, fC4, style_data_row) 
    work_sheet.write(4,8, ihc4, style_data_row)

    work_sheet.write(5,0, 'MONTH 5', style_data_row) 
    work_sheet.write(5,1, rd5, style_data_row) 
    work_sheet.write(5,2, ei5, style_data_row) 
    work_sheet.write(5,3, ntwH5, style_data_row) 
    work_sheet.write(5,4, ntwF5, style_data_row) 
    work_sheet.write(5,5, ntw5, style_data_row) 
    work_sheet.write(5,6, hC5, style_data_row) 
    work_sheet.write(5,7, fC5, style_data_row) 
    work_sheet.write(5,8, ihc5, style_data_row)

    work_sheet.write(6,0, 'MONTH 6', style_data_row) 
    work_sheet.write(6,1, rd6, style_data_row) 
    work_sheet.write(6,2, ei6, style_data_row) 
    work_sheet.write(6,3, ntwH6, style_data_row) 
    work_sheet.write(6,4, ntwF6, style_data_row) 
    work_sheet.write(6,5, ntw6, style_data_row) 
    work_sheet.write(6,6, hC6, style_data_row) 
    work_sheet.write(6,7, fC6, style_data_row) 
    work_sheet.write(6,8, ihc6, style_data_row)

    work_sheet.write(7,0,'TOTAL INDIVIDUAL COSTS',style_data_row)
    work_sheet.write(7,6,thC,style_data_row)
    work_sheet.write(7,7,tfC,style_data_row)
    work_sheet.write(7,8,tihC,style_data_row)

    work_sheet.write(8,0,"OPTIMIZED FINAL COST FOR MULTI-PERIOD PLANNING",style_data_row)
    work_sheet.write(8,7,optimalCost,style_data_row)

    output = BytesIO()
    work_book.save(output)
    output.seek(0)
    response.write(output.getvalue()) 

    return response

def downloadSeven(request,plan_Name):
    response = HttpResponse(content_type='application/vnd.ms-excel') 
    response['Content-Disposition'] = 'attachment;filename=viewSeven.xls'
    work_book = xlwt.Workbook(encoding = 'utf-8') 
    work_sheet = work_book.add_sheet(u'plan details')

    
     
    plan = models.SevenMonthPlan.objects.filter(planName=plan_Name).values()
    for x in plan:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        ntwH5 = x['hiredTemporary5']
        ntwF5 = x['firedTemporary5']
        ntwH6 = x['hiredTemporary6']
        ntwF6 = x['firedTemporary6']
        ntwH7 = x['hiredTemporary7']
        ntwF7 = x['firedTemporary7']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryMonth4']
        rd5 = x['demand5'] - (x['numPermanent5'] * x['prodPermanent5'])
        if rd5 < 0:
            rd5 = 0
        hC5 = ntwH5 * x['costHiring5']
        fC5 = ntwF5 * x['costFiring5']
        ihc5 = x['costHoldingUnit5'] * x['inventoryMonth5']
        rd6 = x['demand6'] - (x['numPermanent6'] * x['prodPermanent6'])
        if rd6 < 0:
            rd6 = 0
        hC6 = ntwH6 * x['costHiring6']
        fC6 = ntwF6 * x['costFiring6']
        ihc6 = x['costHoldingUnit6'] * x['inventoryMonth6']
        rd7 = x['demand7'] - (x['numPermanent7'] * x['prodPermanent7'])
        if rd7 < 0:
            rd7 = 0
        hC7 = ntwH7 * x['costHiring7']
        fC7 = ntwF7 * x['costFiring7']
        ihc7 = x['costHoldingUnit7'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        ntw5 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5
        ntw6 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6
        ntw7 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7
        thC = hC1 + hC2 + hC3 + hC4 + hC5 + hC6 + hC7
        tfC = fC1 + fC2 + fC3 + fC4 + fC5 + fC6 + fC7
        tihC = ihc1 + ihc2 + ihc3 + ihc4 + ihc5 + ihc6 + ihc7
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryMonth4']
        ei5 = x['inventoryMonth5']
        ei6 = x['inventoryMonth6']
        ei7 = x['inventoryFinal']
        optimalCost= x['optimalCost']

    work_sheet.write(0,0, 'MONTH', style_head_row) 
    work_sheet.write(0,1, 'REMAINING DEMAND', style_head_row) 
    work_sheet.write(0,2, 'ENDING INVENTORY UNIT(S)', style_head_row) 
    work_sheet.write(0,3, 'NUMBER OF TEMPORARY WORKER HIRED', style_head_row) 
    work_sheet.write(0,4, 'NUMBER OF TEMPORARY WORKER FIRED', style_head_row) 
    work_sheet.write(0,5, 'NUMBER OF TEMPORARY WORKER(S)', style_head_row) 
    work_sheet.write(0,6, 'HIRING COST', style_head_row) 
    work_sheet.write(0,7, 'FIRING COST', style_head_row) 
    work_sheet.write(0,8, 'INVENTORY HOLDING COST', style_head_row)

    work_sheet.write(1,0, 'MONTH 1', style_data_row) 
    work_sheet.write(1,1, rd1, style_data_row) 
    work_sheet.write(1,2, ei1, style_data_row) 
    work_sheet.write(1,3, ntwH1, style_data_row) 
    work_sheet.write(1,4, ntwF1, style_data_row) 
    work_sheet.write(1,5,ntw1, style_data_row) 
    work_sheet.write(1,6, hC1, style_data_row) 
    work_sheet.write(1,7, fC1, style_data_row) 
    work_sheet.write(1,8, ihc1, style_data_row)

    work_sheet.write(2,0, 'MONTH 2', style_data_row) 
    work_sheet.write(2,1, rd2, style_data_row) 
    work_sheet.write(2,2, ei2, style_data_row) 
    work_sheet.write(2,3, ntwH2, style_data_row) 
    work_sheet.write(2,4, ntwF2, style_data_row) 
    work_sheet.write(2,5,ntw2, style_data_row) 
    work_sheet.write(2,6, hC2, style_data_row) 
    work_sheet.write(2,7, fC2, style_data_row) 
    work_sheet.write(2,8, ihc2, style_data_row)

    work_sheet.write(3,0, 'MONTH 3', style_data_row) 
    work_sheet.write(3,1, rd3, style_data_row) 
    work_sheet.write(3,2, ei3, style_data_row) 
    work_sheet.write(3,3, ntwH3, style_data_row) 
    work_sheet.write(3,4, ntwF3, style_data_row) 
    work_sheet.write(3,5,ntw3, style_data_row) 
    work_sheet.write(3,6, hC3, style_data_row) 
    work_sheet.write(3,7, fC3, style_data_row) 
    work_sheet.write(3,8, ihc3, style_data_row)

    work_sheet.write(4,0, 'MONTH 4', style_data_row) 
    work_sheet.write(4,1, rd4, style_data_row) 
    work_sheet.write(4,2, ei4, style_data_row) 
    work_sheet.write(4,3, ntwH4, style_data_row) 
    work_sheet.write(4,4, ntwF4, style_data_row) 
    work_sheet.write(4,5, ntw4, style_data_row) 
    work_sheet.write(4,6, hC4, style_data_row) 
    work_sheet.write(4,7, fC4, style_data_row) 
    work_sheet.write(4,8, ihc4, style_data_row)

    work_sheet.write(5,0, 'MONTH 5', style_data_row) 
    work_sheet.write(5,1, rd5, style_data_row) 
    work_sheet.write(5,2, ei5, style_data_row) 
    work_sheet.write(5,3, ntwH5, style_data_row) 
    work_sheet.write(5,4, ntwF5, style_data_row) 
    work_sheet.write(5,5, ntw5, style_data_row) 
    work_sheet.write(5,6, hC5, style_data_row) 
    work_sheet.write(5,7, fC5, style_data_row) 
    work_sheet.write(5,8, ihc5, style_data_row)

    work_sheet.write(6,0, 'MONTH 6', style_data_row) 
    work_sheet.write(6,1, rd6, style_data_row) 
    work_sheet.write(6,2, ei6, style_data_row) 
    work_sheet.write(6,3, ntwH6, style_data_row) 
    work_sheet.write(6,4, ntwF6, style_data_row) 
    work_sheet.write(6,5, ntw6, style_data_row) 
    work_sheet.write(6,6, hC6, style_data_row) 
    work_sheet.write(6,7, fC6, style_data_row) 
    work_sheet.write(6,8, ihc6, style_data_row)

    work_sheet.write(7,0, 'MONTH 7', style_data_row) 
    work_sheet.write(7,1, rd7, style_data_row) 
    work_sheet.write(7,2, ei7, style_data_row) 
    work_sheet.write(7,3, ntwH7, style_data_row) 
    work_sheet.write(7,4, ntwF7, style_data_row) 
    work_sheet.write(7,5, ntw7, style_data_row) 
    work_sheet.write(7,6, hC7, style_data_row) 
    work_sheet.write(7,7, fC7, style_data_row) 
    work_sheet.write(7,8, ihc7, style_data_row)

    work_sheet.write(8,0,'TOTAL INDIVIDUAL COSTS',style_data_row)
    work_sheet.write(8,6,thC,style_data_row)
    work_sheet.write(8,7,tfC,style_data_row)
    work_sheet.write(8,8,tihC,style_data_row)

    work_sheet.write(9,0,"OPTIMIZED FINAL COST FOR MULTI-PERIOD PLANNING",style_data_row)
    work_sheet.write(9,7,optimalCost,style_data_row)

    output = BytesIO()
    work_book.save(output)
    output.seek(0)
    response.write(output.getvalue()) 

    return response

def downloadEight(request,plan_Name):
    response = HttpResponse(content_type='application/vnd.ms-excel') 
    response['Content-Disposition'] = 'attachment;filename=viewEight.xls'
    work_book = xlwt.Workbook(encoding = 'utf-8') 
    work_sheet = work_book.add_sheet(u'plan details')

    
     
    plan = models.EightMonthPlan.objects.filter(planName=plan_Name).values()
    for x in plan:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        ntwH5 = x['hiredTemporary5']
        ntwF5 = x['firedTemporary5']
        ntwH6 = x['hiredTemporary6']
        ntwF6 = x['firedTemporary6']
        ntwH7 = x['hiredTemporary7']
        ntwF7 = x['firedTemporary7']
        ntwH8 = x['hiredTemporary8']
        ntwF8 = x['firedTemporary8']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryMonth4']
        rd5 = x['demand5'] - (x['numPermanent5'] * x['prodPermanent5'])
        if rd5 < 0:
            rd5 = 0
        hC5 = ntwH5 * x['costHiring5']
        fC5 = ntwF5 * x['costFiring5']
        ihc5 = x['costHoldingUnit5'] * x['inventoryMonth5']
        rd6 = x['demand6'] - (x['numPermanent6'] * x['prodPermanent6'])
        if rd6 < 0:
            rd6 = 0
        hC6 = ntwH6 * x['costHiring6']
        fC6 = ntwF6 * x['costFiring6']
        ihc6 = x['costHoldingUnit6'] * x['inventoryMonth6']
        rd7 = x['demand7'] - (x['numPermanent7'] * x['prodPermanent7'])
        if rd7 < 0:
            rd7 = 0
        hC7 = ntwH7 * x['costHiring7']
        fC7 = ntwF7 * x['costFiring7']
        ihc7 = x['costHoldingUnit7'] * x['inventoryMonth7']
        rd8 = x['demand8'] - (x['numPermanent8'] * x['prodPermanent8'])
        if rd8 < 0:
            rd8 = 0
        hC8 = ntwH8 * x['costHiring8']
        fC8 = ntwF8 * x['costFiring8']
        ihc8 = x['costHoldingUnit8'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        ntw5 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5
        ntw6 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6
        ntw7 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7
        ntw8 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8
        thC = hC1 + hC2 + hC3 + hC4 + hC5 + hC6 + hC7 + hC8
        tfC = fC1 + fC2 + fC3 + fC4 + fC5 + fC6 + fC7 + fC8
        tihC = ihc1 + ihc2 + ihc3 + ihc4 + ihc5 + ihc6 + ihc7 + ihc8
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryMonth4']
        ei5 = x['inventoryMonth5']
        ei6 = x['inventoryMonth6']
        ei7 = x['inventoryMonth7']
        ei8 = x['inventoryFinal']
        optimalCost= x['optimalCost']

    work_sheet.write(0,0, 'MONTH', style_head_row) 
    work_sheet.write(0,1, 'REMAINING DEMAND', style_head_row) 
    work_sheet.write(0,2, 'ENDING INVENTORY UNIT(S)', style_head_row) 
    work_sheet.write(0,3, 'NUMBER OF TEMPORARY WORKER HIRED', style_head_row) 
    work_sheet.write(0,4, 'NUMBER OF TEMPORARY WORKER FIRED', style_head_row) 
    work_sheet.write(0,5, 'NUMBER OF TEMPORARY WORKER(S)', style_head_row) 
    work_sheet.write(0,6, 'HIRING COST', style_head_row) 
    work_sheet.write(0,7, 'FIRING COST', style_head_row) 
    work_sheet.write(0,8, 'INVENTORY HOLDING COST', style_head_row)

    work_sheet.write(1,0, 'MONTH 1', style_data_row) 
    work_sheet.write(1,1, rd1, style_data_row) 
    work_sheet.write(1,2, ei1, style_data_row) 
    work_sheet.write(1,3, ntwH1, style_data_row) 
    work_sheet.write(1,4, ntwF1, style_data_row) 
    work_sheet.write(1,5,ntw1, style_data_row) 
    work_sheet.write(1,6, hC1, style_data_row) 
    work_sheet.write(1,7, fC1, style_data_row) 
    work_sheet.write(1,8, ihc1, style_data_row)

    work_sheet.write(2,0, 'MONTH 2', style_data_row) 
    work_sheet.write(2,1, rd2, style_data_row) 
    work_sheet.write(2,2, ei2, style_data_row) 
    work_sheet.write(2,3, ntwH2, style_data_row) 
    work_sheet.write(2,4, ntwF2, style_data_row) 
    work_sheet.write(2,5,ntw2, style_data_row) 
    work_sheet.write(2,6, hC2, style_data_row) 
    work_sheet.write(2,7, fC2, style_data_row) 
    work_sheet.write(2,8, ihc2, style_data_row)

    work_sheet.write(3,0, 'MONTH 3', style_data_row) 
    work_sheet.write(3,1, rd3, style_data_row) 
    work_sheet.write(3,2, ei3, style_data_row) 
    work_sheet.write(3,3, ntwH3, style_data_row) 
    work_sheet.write(3,4, ntwF3, style_data_row) 
    work_sheet.write(3,5,ntw3, style_data_row) 
    work_sheet.write(3,6, hC3, style_data_row) 
    work_sheet.write(3,7, fC3, style_data_row) 
    work_sheet.write(3,8, ihc3, style_data_row)

    work_sheet.write(4,0, 'MONTH 4', style_data_row) 
    work_sheet.write(4,1, rd4, style_data_row) 
    work_sheet.write(4,2, ei4, style_data_row) 
    work_sheet.write(4,3, ntwH4, style_data_row) 
    work_sheet.write(4,4, ntwF4, style_data_row) 
    work_sheet.write(4,5, ntw4, style_data_row) 
    work_sheet.write(4,6, hC4, style_data_row) 
    work_sheet.write(4,7, fC4, style_data_row) 
    work_sheet.write(4,8, ihc4, style_data_row)

    work_sheet.write(5,0, 'MONTH 5', style_data_row) 
    work_sheet.write(5,1, rd5, style_data_row) 
    work_sheet.write(5,2, ei5, style_data_row) 
    work_sheet.write(5,3, ntwH5, style_data_row) 
    work_sheet.write(5,4, ntwF5, style_data_row) 
    work_sheet.write(5,5, ntw5, style_data_row) 
    work_sheet.write(5,6, hC5, style_data_row) 
    work_sheet.write(5,7, fC5, style_data_row) 
    work_sheet.write(5,8, ihc5, style_data_row)

    work_sheet.write(6,0, 'MONTH 6', style_data_row) 
    work_sheet.write(6,1, rd6, style_data_row) 
    work_sheet.write(6,2, ei6, style_data_row) 
    work_sheet.write(6,3, ntwH6, style_data_row) 
    work_sheet.write(6,4, ntwF6, style_data_row) 
    work_sheet.write(6,5, ntw6, style_data_row) 
    work_sheet.write(6,6, hC6, style_data_row) 
    work_sheet.write(6,7, fC6, style_data_row) 
    work_sheet.write(6,8, ihc6, style_data_row)

    work_sheet.write(7,0, 'MONTH 7', style_data_row) 
    work_sheet.write(7,1, rd7, style_data_row) 
    work_sheet.write(7,2, ei7, style_data_row) 
    work_sheet.write(7,3, ntwH7, style_data_row) 
    work_sheet.write(7,4, ntwF7, style_data_row) 
    work_sheet.write(7,5, ntw7, style_data_row) 
    work_sheet.write(7,6, hC7, style_data_row) 
    work_sheet.write(7,7, fC7, style_data_row) 
    work_sheet.write(7,8, ihc7, style_data_row)

    work_sheet.write(8,0, 'MONTH 8', style_data_row) 
    work_sheet.write(8,1, rd8, style_data_row) 
    work_sheet.write(8,2, ei8, style_data_row) 
    work_sheet.write(8,3, ntwH8, style_data_row) 
    work_sheet.write(8,4, ntwF8, style_data_row) 
    work_sheet.write(8,5, ntw8, style_data_row) 
    work_sheet.write(8,6, hC8, style_data_row) 
    work_sheet.write(8,7, fC8, style_data_row) 
    work_sheet.write(8,8, ihc8, style_data_row)

    work_sheet.write(9,0,'TOTAL INDIVIDUAL COSTS',style_data_row)
    work_sheet.write(9,6,thC,style_data_row)
    work_sheet.write(9,7,tfC,style_data_row)
    work_sheet.write(9,8,tihC,style_data_row)

    work_sheet.write(10,0,"OPTIMIZED FINAL COST FOR MULTI-PERIOD PLANNING",style_data_row)
    work_sheet.write(10,7,optimalCost,style_data_row)

    output = BytesIO()
    work_book.save(output)
    output.seek(0)
    response.write(output.getvalue()) 

    return response

def downloadNine(request,plan_Name):
    response = HttpResponse(content_type='application/vnd.ms-excel') 
    response['Content-Disposition'] = 'attachment;filename=viewNine.xls'
    work_book = xlwt.Workbook(encoding = 'utf-8') 
    work_sheet = work_book.add_sheet(u'plan details')

    
     
    plan = models.NineMonthPlan.objects.filter(planName=plan_Name).values()
    for x in plan:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        ntwH5 = x['hiredTemporary5']
        ntwF5 = x['firedTemporary5']
        ntwH6 = x['hiredTemporary6']
        ntwF6 = x['firedTemporary6']
        ntwH7 = x['hiredTemporary7']
        ntwF7 = x['firedTemporary7']
        ntwH8 = x['hiredTemporary8']
        ntwF8 = x['firedTemporary8']
        ntwH9 = x['hiredTemporary9']
        ntwF9 = x['firedTemporary9']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryMonth4']
        rd5 = x['demand5'] - (x['numPermanent5'] * x['prodPermanent5'])
        if rd5 < 0:
            rd5 = 0
        hC5 = ntwH5 * x['costHiring5']
        fC5 = ntwF5 * x['costFiring5']
        ihc5 = x['costHoldingUnit5'] * x['inventoryMonth5']
        rd6 = x['demand6'] - (x['numPermanent6'] * x['prodPermanent6'])
        if rd6 < 0:
            rd6 = 0
        hC6 = ntwH6 * x['costHiring6']
        fC6 = ntwF6 * x['costFiring6']
        ihc6 = x['costHoldingUnit6'] * x['inventoryMonth6']
        rd7 = x['demand7'] - (x['numPermanent7'] * x['prodPermanent7'])
        if rd7 < 0:
            rd7 = 0
        hC7 = ntwH7 * x['costHiring7']
        fC7 = ntwF7 * x['costFiring7']
        ihc7 = x['costHoldingUnit7'] * x['inventoryMonth7']
        rd8 = x['demand8'] - (x['numPermanent8'] * x['prodPermanent8'])
        if rd8 < 0:
            rd8 = 0
        hC8 = ntwH8 * x['costHiring8']
        fC8 = ntwF8 * x['costFiring8']
        ihc8 = x['costHoldingUnit8'] * x['inventoryMonth8']
        rd9 = x['demand9'] - (x['numPermanent9'] * x['prodPermanent9'])
        if rd9 < 0:
            rd9 = 0
        hC9 = ntwH9 * x['costHiring9']
        fC9 = ntwF9 * x['costFiring9']
        ihc9 = x['costHoldingUnit9'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        ntw5 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5
        ntw6 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6
        ntw7 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7
        ntw8 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8
        ntw9 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9
        thC = hC1 + hC2 + hC3 + hC4 + hC5 + hC6 + hC7 + hC8 + hC9
        tfC = fC1 + fC2 + fC3 + fC4 + fC5 + fC6 + fC7 + fC8 + fC9
        tihC = ihc1 + ihc2 + ihc3 + ihc4 + ihc5 + ihc6 + ihc7 + ihc8 + ihc9
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryMonth4']
        ei5 = x['inventoryMonth5']
        ei6 = x['inventoryMonth6']
        ei7 = x['inventoryMonth7']
        ei8 = x['inventoryMonth8']
        ei9 = x['inventoryFinal']
        optimalCost= x['optimalCost']

    work_sheet.write(0,0, 'MONTH', style_head_row) 
    work_sheet.write(0,1, 'REMAINING DEMAND', style_head_row) 
    work_sheet.write(0,2, 'ENDING INVENTORY UNIT(S)', style_head_row) 
    work_sheet.write(0,3, 'NUMBER OF TEMPORARY WORKER HIRED', style_head_row) 
    work_sheet.write(0,4, 'NUMBER OF TEMPORARY WORKER FIRED', style_head_row) 
    work_sheet.write(0,5, 'NUMBER OF TEMPORARY WORKER(S)', style_head_row) 
    work_sheet.write(0,6, 'HIRING COST', style_head_row) 
    work_sheet.write(0,7, 'FIRING COST', style_head_row) 
    work_sheet.write(0,8, 'INVENTORY HOLDING COST', style_head_row)

    work_sheet.write(1,0, 'MONTH 1', style_data_row) 
    work_sheet.write(1,1, rd1, style_data_row) 
    work_sheet.write(1,2, ei1, style_data_row) 
    work_sheet.write(1,3, ntwH1, style_data_row) 
    work_sheet.write(1,4, ntwF1, style_data_row) 
    work_sheet.write(1,5,ntw1, style_data_row) 
    work_sheet.write(1,6, hC1, style_data_row) 
    work_sheet.write(1,7, fC1, style_data_row) 
    work_sheet.write(1,8, ihc1, style_data_row)

    work_sheet.write(2,0, 'MONTH 2', style_data_row) 
    work_sheet.write(2,1, rd2, style_data_row) 
    work_sheet.write(2,2, ei2, style_data_row) 
    work_sheet.write(2,3, ntwH2, style_data_row) 
    work_sheet.write(2,4, ntwF2, style_data_row) 
    work_sheet.write(2,5,ntw2, style_data_row) 
    work_sheet.write(2,6, hC2, style_data_row) 
    work_sheet.write(2,7, fC2, style_data_row) 
    work_sheet.write(2,8, ihc2, style_data_row)

    work_sheet.write(3,0, 'MONTH 3', style_data_row) 
    work_sheet.write(3,1, rd3, style_data_row) 
    work_sheet.write(3,2, ei3, style_data_row) 
    work_sheet.write(3,3, ntwH3, style_data_row) 
    work_sheet.write(3,4, ntwF3, style_data_row) 
    work_sheet.write(3,5,ntw3, style_data_row) 
    work_sheet.write(3,6, hC3, style_data_row) 
    work_sheet.write(3,7, fC3, style_data_row) 
    work_sheet.write(3,8, ihc3, style_data_row)

    work_sheet.write(4,0, 'MONTH 4', style_data_row) 
    work_sheet.write(4,1, rd4, style_data_row) 
    work_sheet.write(4,2, ei4, style_data_row) 
    work_sheet.write(4,3, ntwH4, style_data_row) 
    work_sheet.write(4,4, ntwF4, style_data_row) 
    work_sheet.write(4,5, ntw4, style_data_row) 
    work_sheet.write(4,6, hC4, style_data_row) 
    work_sheet.write(4,7, fC4, style_data_row) 
    work_sheet.write(4,8, ihc4, style_data_row)

    work_sheet.write(5,0, 'MONTH 5', style_data_row) 
    work_sheet.write(5,1, rd5, style_data_row) 
    work_sheet.write(5,2, ei5, style_data_row) 
    work_sheet.write(5,3, ntwH5, style_data_row) 
    work_sheet.write(5,4, ntwF5, style_data_row) 
    work_sheet.write(5,5, ntw5, style_data_row) 
    work_sheet.write(5,6, hC5, style_data_row) 
    work_sheet.write(5,7, fC5, style_data_row) 
    work_sheet.write(5,8, ihc5, style_data_row)

    work_sheet.write(6,0, 'MONTH 6', style_data_row) 
    work_sheet.write(6,1, rd6, style_data_row) 
    work_sheet.write(6,2, ei6, style_data_row) 
    work_sheet.write(6,3, ntwH6, style_data_row) 
    work_sheet.write(6,4, ntwF6, style_data_row) 
    work_sheet.write(6,5, ntw6, style_data_row) 
    work_sheet.write(6,6, hC6, style_data_row) 
    work_sheet.write(6,7, fC6, style_data_row) 
    work_sheet.write(6,8, ihc6, style_data_row)

    work_sheet.write(7,0, 'MONTH 7', style_data_row) 
    work_sheet.write(7,1, rd7, style_data_row) 
    work_sheet.write(7,2, ei7, style_data_row) 
    work_sheet.write(7,3, ntwH7, style_data_row) 
    work_sheet.write(7,4, ntwF7, style_data_row) 
    work_sheet.write(7,5, ntw7, style_data_row) 
    work_sheet.write(7,6, hC7, style_data_row) 
    work_sheet.write(7,7, fC7, style_data_row) 
    work_sheet.write(7,8, ihc7, style_data_row)

    work_sheet.write(8,0, 'MONTH 8', style_data_row) 
    work_sheet.write(8,1, rd8, style_data_row) 
    work_sheet.write(8,2, ei8, style_data_row) 
    work_sheet.write(8,3, ntwH8, style_data_row) 
    work_sheet.write(8,4, ntwF8, style_data_row) 
    work_sheet.write(8,5, ntw8, style_data_row) 
    work_sheet.write(8,6, hC8, style_data_row) 
    work_sheet.write(8,7, fC8, style_data_row) 
    work_sheet.write(8,8, ihc8, style_data_row)

    work_sheet.write(9,0, 'MONTH 9', style_data_row) 
    work_sheet.write(9,1, rd9, style_data_row) 
    work_sheet.write(9,2, ei9, style_data_row) 
    work_sheet.write(9,3, ntwH9, style_data_row) 
    work_sheet.write(9,4, ntwF9, style_data_row) 
    work_sheet.write(9,5, ntw9, style_data_row) 
    work_sheet.write(9,6, hC9, style_data_row) 
    work_sheet.write(9,7, fC9, style_data_row) 
    work_sheet.write(9,8, ihc9, style_data_row)

    work_sheet.write(10,0,'TOTAL INDIVIDUAL COSTS',style_data_row)
    work_sheet.write(10,6,thC,style_data_row)
    work_sheet.write(10,7,tfC,style_data_row)
    work_sheet.write(10,8,tihC,style_data_row)

    work_sheet.write(11,0,"OPTIMIZED FINAL COST FOR MULTI-PERIOD PLANNING",style_data_row)
    work_sheet.write(11,7,optimalCost,style_data_row)

    output = BytesIO()
    work_book.save(output)
    output.seek(0)
    response.write(output.getvalue()) 

    return response

def downloadTen(request,plan_Name):
    response = HttpResponse(content_type='application/vnd.ms-excel') 
    response['Content-Disposition'] = 'attachment;filename=viewTen.xls'
    work_book = xlwt.Workbook(encoding = 'utf-8') 
    work_sheet = work_book.add_sheet(u'plan details')

    
     
    plan = models.TenMonthPlan.objects.filter(planName=plan_Name).values()
    for x in plan:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        ntwH5 = x['hiredTemporary5']
        ntwF5 = x['firedTemporary5']
        ntwH6 = x['hiredTemporary6']
        ntwF6 = x['firedTemporary6']
        ntwH7 = x['hiredTemporary7']
        ntwF7 = x['firedTemporary7']
        ntwH8 = x['hiredTemporary8']
        ntwF8 = x['firedTemporary8']
        ntwH9 = x['hiredTemporary9']
        ntwF9 = x['firedTemporary9']
        ntwH10 = x['hiredTemporary10']
        ntwF10 = x['firedTemporary10']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryMonth4']
        rd5 = x['demand5'] - (x['numPermanent5'] * x['prodPermanent5'])
        if rd5 < 0:
            rd5 = 0
        hC5 = ntwH5 * x['costHiring5']
        fC5 = ntwF5 * x['costFiring5']
        ihc5 = x['costHoldingUnit5'] * x['inventoryMonth5']
        rd6 = x['demand6'] - (x['numPermanent6'] * x['prodPermanent6'])
        if rd6 < 0:
            rd6 = 0
        hC6 = ntwH6 * x['costHiring6']
        fC6 = ntwF6 * x['costFiring6']
        ihc6 = x['costHoldingUnit6'] * x['inventoryMonth6']
        rd7 = x['demand7'] - (x['numPermanent7'] * x['prodPermanent7'])
        if rd7 < 0:
            rd7 = 0
        hC7 = ntwH7 * x['costHiring7']
        fC7 = ntwF7 * x['costFiring7']
        ihc7 = x['costHoldingUnit7'] * x['inventoryMonth7']
        rd8 = x['demand8'] - (x['numPermanent8'] * x['prodPermanent8'])
        if rd8 < 0:
            rd8 = 0
        hC8 = ntwH8 * x['costHiring8']
        fC8 = ntwF8 * x['costFiring8']
        ihc8 = x['costHoldingUnit8'] * x['inventoryMonth8']
        rd9 = x['demand9'] - (x['numPermanent9'] * x['prodPermanent9'])
        if rd9 < 0:
            rd9 = 0
        hC9 = ntwH9 * x['costHiring9']
        fC9 = ntwF9 * x['costFiring9']
        ihc9 = x['costHoldingUnit9'] * x['inventoryMonth9']
        rd10 = x['demand10'] - (x['numPermanent10'] * x['prodPermanent10'])
        if rd10 < 0:
            rd10 = 0
        hC10 = ntwH10 * x['costHiring10']
        fC10 = ntwF10 * x['costFiring10']
        ihc10 = x['costHoldingUnit10'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        ntw5 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5
        ntw6 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6
        ntw7 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7
        ntw8 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8
        ntw9 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9
        ntw10 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9 + ntwH10 - ntwF10
        thC = hC1 + hC2 + hC3 + hC4 + hC5 + hC6 + hC7 + hC8 + hC9 + hC10
        tfC = fC1 + fC2 + fC3 + fC4 + fC5 + fC6 + fC7 + fC8 + fC9 + fC10
        tihC = ihc1 + ihc2 + ihc3 + ihc4 + ihc5 + ihc6 + ihc7 + ihc8 + ihc9 + ihc10
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryMonth4']
        ei5 = x['inventoryMonth5']
        ei6 = x['inventoryMonth6']
        ei7 = x['inventoryMonth7']
        ei8 = x['inventoryMonth8']
        ei9 = x['inventoryMonth9']
        ei10 = x['inventoryFinal']
        optimalCost= x['optimalCost']

    work_sheet.write(0,0, 'MONTH', style_head_row) 
    work_sheet.write(0,1, 'REMAINING DEMAND', style_head_row) 
    work_sheet.write(0,2, 'ENDING INVENTORY UNIT(S)', style_head_row) 
    work_sheet.write(0,3, 'NUMBER OF TEMPORARY WORKER HIRED', style_head_row) 
    work_sheet.write(0,4, 'NUMBER OF TEMPORARY WORKER FIRED', style_head_row) 
    work_sheet.write(0,5, 'NUMBER OF TEMPORARY WORKER(S)', style_head_row) 
    work_sheet.write(0,6, 'HIRING COST', style_head_row) 
    work_sheet.write(0,7, 'FIRING COST', style_head_row) 
    work_sheet.write(0,8, 'INVENTORY HOLDING COST', style_head_row)

    work_sheet.write(1,0, 'MONTH 1', style_data_row) 
    work_sheet.write(1,1, rd1, style_data_row) 
    work_sheet.write(1,2, ei1, style_data_row) 
    work_sheet.write(1,3, ntwH1, style_data_row) 
    work_sheet.write(1,4, ntwF1, style_data_row) 
    work_sheet.write(1,5,ntw1, style_data_row) 
    work_sheet.write(1,6, hC1, style_data_row) 
    work_sheet.write(1,7, fC1, style_data_row) 
    work_sheet.write(1,8, ihc1, style_data_row)

    work_sheet.write(2,0, 'MONTH 2', style_data_row) 
    work_sheet.write(2,1, rd2, style_data_row) 
    work_sheet.write(2,2, ei2, style_data_row) 
    work_sheet.write(2,3, ntwH2, style_data_row) 
    work_sheet.write(2,4, ntwF2, style_data_row) 
    work_sheet.write(2,5,ntw2, style_data_row) 
    work_sheet.write(2,6, hC2, style_data_row) 
    work_sheet.write(2,7, fC2, style_data_row) 
    work_sheet.write(2,8, ihc2, style_data_row)

    work_sheet.write(3,0, 'MONTH 3', style_data_row) 
    work_sheet.write(3,1, rd3, style_data_row) 
    work_sheet.write(3,2, ei3, style_data_row) 
    work_sheet.write(3,3, ntwH3, style_data_row) 
    work_sheet.write(3,4, ntwF3, style_data_row) 
    work_sheet.write(3,5,ntw3, style_data_row) 
    work_sheet.write(3,6, hC3, style_data_row) 
    work_sheet.write(3,7, fC3, style_data_row) 
    work_sheet.write(3,8, ihc3, style_data_row)

    work_sheet.write(4,0, 'MONTH 4', style_data_row) 
    work_sheet.write(4,1, rd4, style_data_row) 
    work_sheet.write(4,2, ei4, style_data_row) 
    work_sheet.write(4,3, ntwH4, style_data_row) 
    work_sheet.write(4,4, ntwF4, style_data_row) 
    work_sheet.write(4,5, ntw4, style_data_row) 
    work_sheet.write(4,6, hC4, style_data_row) 
    work_sheet.write(4,7, fC4, style_data_row) 
    work_sheet.write(4,8, ihc4, style_data_row)

    work_sheet.write(5,0, 'MONTH 5', style_data_row) 
    work_sheet.write(5,1, rd5, style_data_row) 
    work_sheet.write(5,2, ei5, style_data_row) 
    work_sheet.write(5,3, ntwH5, style_data_row) 
    work_sheet.write(5,4, ntwF5, style_data_row) 
    work_sheet.write(5,5, ntw5, style_data_row) 
    work_sheet.write(5,6, hC5, style_data_row) 
    work_sheet.write(5,7, fC5, style_data_row) 
    work_sheet.write(5,8, ihc5, style_data_row)

    work_sheet.write(6,0, 'MONTH 6', style_data_row) 
    work_sheet.write(6,1, rd6, style_data_row) 
    work_sheet.write(6,2, ei6, style_data_row) 
    work_sheet.write(6,3, ntwH6, style_data_row) 
    work_sheet.write(6,4, ntwF6, style_data_row) 
    work_sheet.write(6,5, ntw6, style_data_row) 
    work_sheet.write(6,6, hC6, style_data_row) 
    work_sheet.write(6,7, fC6, style_data_row) 
    work_sheet.write(6,8, ihc6, style_data_row)

    work_sheet.write(7,0, 'MONTH 7', style_data_row) 
    work_sheet.write(7,1, rd7, style_data_row) 
    work_sheet.write(7,2, ei7, style_data_row) 
    work_sheet.write(7,3, ntwH7, style_data_row) 
    work_sheet.write(7,4, ntwF7, style_data_row) 
    work_sheet.write(7,5, ntw7, style_data_row) 
    work_sheet.write(7,6, hC7, style_data_row) 
    work_sheet.write(7,7, fC7, style_data_row) 
    work_sheet.write(7,8, ihc7, style_data_row)

    work_sheet.write(8,0, 'MONTH 8', style_data_row) 
    work_sheet.write(8,1, rd8, style_data_row) 
    work_sheet.write(8,2, ei8, style_data_row) 
    work_sheet.write(8,3, ntwH8, style_data_row) 
    work_sheet.write(8,4, ntwF8, style_data_row) 
    work_sheet.write(8,5, ntw8, style_data_row) 
    work_sheet.write(8,6, hC8, style_data_row) 
    work_sheet.write(8,7, fC8, style_data_row) 
    work_sheet.write(8,8, ihc8, style_data_row)

    work_sheet.write(9,0, 'MONTH 9', style_data_row) 
    work_sheet.write(9,1, rd9, style_data_row) 
    work_sheet.write(9,2, ei9, style_data_row) 
    work_sheet.write(9,3, ntwH9, style_data_row) 
    work_sheet.write(9,4, ntwF9, style_data_row) 
    work_sheet.write(9,5, ntw9, style_data_row) 
    work_sheet.write(9,6, hC9, style_data_row) 
    work_sheet.write(9,7, fC9, style_data_row) 
    work_sheet.write(9,8, ihc9, style_data_row)

    work_sheet.write(10,0, 'MONTH 10', style_data_row) 
    work_sheet.write(10,1, rd10, style_data_row) 
    work_sheet.write(10,2, ei10, style_data_row) 
    work_sheet.write(10,3, ntwH10, style_data_row) 
    work_sheet.write(10,4, ntwF10, style_data_row) 
    work_sheet.write(10,5, ntw10, style_data_row) 
    work_sheet.write(10,6, hC10, style_data_row) 
    work_sheet.write(10,7, fC10, style_data_row) 
    work_sheet.write(10,8, ihc10, style_data_row)

    work_sheet.write(11,0,'TOTAL INDIVIDUAL COSTS',style_data_row)
    work_sheet.write(11,6,thC,style_data_row)
    work_sheet.write(11,7,tfC,style_data_row)
    work_sheet.write(11,8,tihC,style_data_row)

    work_sheet.write(12,0,"OPTIMIZED FINAL COST FOR MULTI-PERIOD PLANNING",style_data_row)
    work_sheet.write(12,7,optimalCost,style_data_row)

    output = BytesIO()
    work_book.save(output)
    output.seek(0)
    response.write(output.getvalue()) 

    return response

def downloadEleven(request,plan_Name):
    response = HttpResponse(content_type='application/vnd.ms-excel') 
    response['Content-Disposition'] = 'attachment;filename=viewEleven.xls'
    work_book = xlwt.Workbook(encoding = 'utf-8') 
    work_sheet = work_book.add_sheet(u'plan details')

    
     
    plan = models.ElevenMonthPlan.objects.filter(planName=plan_Name).values()
    for x in plan:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        ntwH5 = x['hiredTemporary5']
        ntwF5 = x['firedTemporary5']
        ntwH6 = x['hiredTemporary6']
        ntwF6 = x['firedTemporary6']
        ntwH7 = x['hiredTemporary7']
        ntwF7 = x['firedTemporary7']
        ntwH8 = x['hiredTemporary8']
        ntwF8 = x['firedTemporary8']
        ntwH9 = x['hiredTemporary9']
        ntwF9 = x['firedTemporary9']
        ntwH10 = x['hiredTemporary10']
        ntwF10 = x['firedTemporary10']
        ntwH11 = x['hiredTemporary11']
        ntwF11 = x['firedTemporary11']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryMonth4']
        rd5 = x['demand5'] - (x['numPermanent5'] * x['prodPermanent5'])
        if rd5 < 0:
            rd5 = 0
        hC5 = ntwH5 * x['costHiring5']
        fC5 = ntwF5 * x['costFiring5']
        ihc5 = x['costHoldingUnit5'] * x['inventoryMonth5']
        rd6 = x['demand6'] - (x['numPermanent6'] * x['prodPermanent6'])
        if rd6 < 0:
            rd6 = 0
        hC6 = ntwH6 * x['costHiring6']
        fC6 = ntwF6 * x['costFiring6']
        ihc6 = x['costHoldingUnit6'] * x['inventoryMonth6']
        rd7 = x['demand7'] - (x['numPermanent7'] * x['prodPermanent7'])
        if rd7 < 0:
            rd7 = 0
        hC7 = ntwH7 * x['costHiring7']
        fC7 = ntwF7 * x['costFiring7']
        ihc7 = x['costHoldingUnit7'] * x['inventoryMonth7']
        rd8 = x['demand8'] - (x['numPermanent8'] * x['prodPermanent8'])
        if rd8 < 0:
            rd8 = 0
        hC8 = ntwH8 * x['costHiring8']
        fC8 = ntwF8 * x['costFiring8']
        ihc8 = x['costHoldingUnit8'] * x['inventoryMonth8']
        rd9 = x['demand9'] - (x['numPermanent9'] * x['prodPermanent9'])
        if rd9 < 0:
            rd9 = 0
        hC9 = ntwH9 * x['costHiring9']
        fC9 = ntwF9 * x['costFiring9']
        ihc9 = x['costHoldingUnit9'] * x['inventoryMonth9']
        rd10 = x['demand10'] - (x['numPermanent10'] * x['prodPermanent10'])
        if rd10 < 0:
            rd10 = 0
        hC10 = ntwH10 * x['costHiring10']
        fC10 = ntwF10 * x['costFiring10']
        ihc10 = x['costHoldingUnit10'] * x['inventoryMonth10']
        rd11 = x['demand11'] - (x['numPermanent11'] * x['prodPermanent11'])
        if rd11 < 0:
            rd11 = 0
        hC11 = ntwH11 * x['costHiring11']
        fC11 = ntwF11 * x['costFiring11']
        ihc11 = x['costHoldingUnit11'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        ntw5 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5
        ntw6 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6
        ntw7 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7
        ntw8 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8
        ntw9 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9
        ntw10 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9 + ntwH10 - ntwF10
        ntw11 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9 + ntwH10 - ntwF10 + ntwH11 - ntwF11
        thC = hC1 + hC2 + hC3 + hC4 + hC5 + hC6 + hC7 + hC8 + hC9 + hC10 + hC11
        tfC = fC1 + fC2 + fC3 + fC4 + fC5 + fC6 + fC7 + fC8 + fC9 + fC10 + fC11
        tihC = ihc1 + ihc2 + ihc3 + ihc4 + ihc5 + ihc6 + ihc7 + ihc8 + ihc9 + ihc10 + ihc11
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryMonth4']
        ei5 = x['inventoryMonth5']
        ei6 = x['inventoryMonth6']
        ei7 = x['inventoryMonth7']
        ei8 = x['inventoryMonth8']
        ei9 = x['inventoryMonth9']
        ei10 = x['inventoryMonth10']
        ei11 = x['inventoryFinal']
        optimalCost= x['optimalCost']

    work_sheet.write(0,0, 'MONTH', style_head_row) 
    work_sheet.write(0,1, 'REMAINING DEMAND', style_head_row) 
    work_sheet.write(0,2, 'ENDING INVENTORY UNIT(S)', style_head_row) 
    work_sheet.write(0,3, 'NUMBER OF TEMPORARY WORKER HIRED', style_head_row) 
    work_sheet.write(0,4, 'NUMBER OF TEMPORARY WORKER FIRED', style_head_row) 
    work_sheet.write(0,5, 'NUMBER OF TEMPORARY WORKER(S)', style_head_row) 
    work_sheet.write(0,6, 'HIRING COST', style_head_row) 
    work_sheet.write(0,7, 'FIRING COST', style_head_row) 
    work_sheet.write(0,8, 'INVENTORY HOLDING COST', style_head_row)

    work_sheet.write(1,0, 'MONTH 1', style_data_row) 
    work_sheet.write(1,1, rd1, style_data_row) 
    work_sheet.write(1,2, ei1, style_data_row) 
    work_sheet.write(1,3, ntwH1, style_data_row) 
    work_sheet.write(1,4, ntwF1, style_data_row) 
    work_sheet.write(1,5,ntw1, style_data_row) 
    work_sheet.write(1,6, hC1, style_data_row) 
    work_sheet.write(1,7, fC1, style_data_row) 
    work_sheet.write(1,8, ihc1, style_data_row)

    work_sheet.write(2,0, 'MONTH 2', style_data_row) 
    work_sheet.write(2,1, rd2, style_data_row) 
    work_sheet.write(2,2, ei2, style_data_row) 
    work_sheet.write(2,3, ntwH2, style_data_row) 
    work_sheet.write(2,4, ntwF2, style_data_row) 
    work_sheet.write(2,5,ntw2, style_data_row) 
    work_sheet.write(2,6, hC2, style_data_row) 
    work_sheet.write(2,7, fC2, style_data_row) 
    work_sheet.write(2,8, ihc2, style_data_row)

    work_sheet.write(3,0, 'MONTH 3', style_data_row) 
    work_sheet.write(3,1, rd3, style_data_row) 
    work_sheet.write(3,2, ei3, style_data_row) 
    work_sheet.write(3,3, ntwH3, style_data_row) 
    work_sheet.write(3,4, ntwF3, style_data_row) 
    work_sheet.write(3,5,ntw3, style_data_row) 
    work_sheet.write(3,6, hC3, style_data_row) 
    work_sheet.write(3,7, fC3, style_data_row) 
    work_sheet.write(3,8, ihc3, style_data_row)

    work_sheet.write(4,0, 'MONTH 4', style_data_row) 
    work_sheet.write(4,1, rd4, style_data_row) 
    work_sheet.write(4,2, ei4, style_data_row) 
    work_sheet.write(4,3, ntwH4, style_data_row) 
    work_sheet.write(4,4, ntwF4, style_data_row) 
    work_sheet.write(4,5, ntw4, style_data_row) 
    work_sheet.write(4,6, hC4, style_data_row) 
    work_sheet.write(4,7, fC4, style_data_row) 
    work_sheet.write(4,8, ihc4, style_data_row)

    work_sheet.write(5,0, 'MONTH 5', style_data_row) 
    work_sheet.write(5,1, rd5, style_data_row) 
    work_sheet.write(5,2, ei5, style_data_row) 
    work_sheet.write(5,3, ntwH5, style_data_row) 
    work_sheet.write(5,4, ntwF5, style_data_row) 
    work_sheet.write(5,5, ntw5, style_data_row) 
    work_sheet.write(5,6, hC5, style_data_row) 
    work_sheet.write(5,7, fC5, style_data_row) 
    work_sheet.write(5,8, ihc5, style_data_row)

    work_sheet.write(6,0, 'MONTH 6', style_data_row) 
    work_sheet.write(6,1, rd6, style_data_row) 
    work_sheet.write(6,2, ei6, style_data_row) 
    work_sheet.write(6,3, ntwH6, style_data_row) 
    work_sheet.write(6,4, ntwF6, style_data_row) 
    work_sheet.write(6,5, ntw6, style_data_row) 
    work_sheet.write(6,6, hC6, style_data_row) 
    work_sheet.write(6,7, fC6, style_data_row) 
    work_sheet.write(6,8, ihc6, style_data_row)

    work_sheet.write(7,0, 'MONTH 7', style_data_row) 
    work_sheet.write(7,1, rd7, style_data_row) 
    work_sheet.write(7,2, ei7, style_data_row) 
    work_sheet.write(7,3, ntwH7, style_data_row) 
    work_sheet.write(7,4, ntwF7, style_data_row) 
    work_sheet.write(7,5, ntw7, style_data_row) 
    work_sheet.write(7,6, hC7, style_data_row) 
    work_sheet.write(7,7, fC7, style_data_row) 
    work_sheet.write(7,8, ihc7, style_data_row)

    work_sheet.write(8,0, 'MONTH 8', style_data_row) 
    work_sheet.write(8,1, rd8, style_data_row) 
    work_sheet.write(8,2, ei8, style_data_row) 
    work_sheet.write(8,3, ntwH8, style_data_row) 
    work_sheet.write(8,4, ntwF8, style_data_row) 
    work_sheet.write(8,5, ntw8, style_data_row) 
    work_sheet.write(8,6, hC8, style_data_row) 
    work_sheet.write(8,7, fC8, style_data_row) 
    work_sheet.write(8,8, ihc8, style_data_row)

    work_sheet.write(9,0, 'MONTH 9', style_data_row) 
    work_sheet.write(9,1, rd9, style_data_row) 
    work_sheet.write(9,2, ei9, style_data_row) 
    work_sheet.write(9,3, ntwH9, style_data_row) 
    work_sheet.write(9,4, ntwF9, style_data_row) 
    work_sheet.write(9,5, ntw9, style_data_row) 
    work_sheet.write(9,6, hC9, style_data_row) 
    work_sheet.write(9,7, fC9, style_data_row) 
    work_sheet.write(9,8, ihc9, style_data_row)

    work_sheet.write(10,0, 'MONTH 10', style_data_row) 
    work_sheet.write(10,1, rd10, style_data_row) 
    work_sheet.write(10,2, ei10, style_data_row) 
    work_sheet.write(10,3, ntwH10, style_data_row) 
    work_sheet.write(10,4, ntwF10, style_data_row) 
    work_sheet.write(10,5, ntw10, style_data_row) 
    work_sheet.write(10,6, hC10, style_data_row) 
    work_sheet.write(10,7, fC10, style_data_row) 
    work_sheet.write(10,8, ihc10, style_data_row)

    work_sheet.write(11,0, 'MONTH 11', style_data_row) 
    work_sheet.write(11,1, rd11, style_data_row) 
    work_sheet.write(11,2, ei11, style_data_row) 
    work_sheet.write(11,3, ntwH11, style_data_row) 
    work_sheet.write(11,4, ntwF11, style_data_row) 
    work_sheet.write(11,5, ntw11, style_data_row) 
    work_sheet.write(11,6, hC11, style_data_row) 
    work_sheet.write(11,7, fC11, style_data_row) 
    work_sheet.write(11,8, ihc11, style_data_row)

    work_sheet.write(12,0,'TOTAL INDIVIDUAL COSTS',style_data_row)
    work_sheet.write(12,6,thC,style_data_row)
    work_sheet.write(12,7,tfC,style_data_row)
    work_sheet.write(12,8,tihC,style_data_row)

    work_sheet.write(13,0,"OPTIMIZED FINAL COST FOR MULTI-PERIOD PLANNING",style_data_row)
    work_sheet.write(13,7,optimalCost,style_data_row)

    output = BytesIO()
    work_book.save(output)
    output.seek(0)
    response.write(output.getvalue()) 

    return response

def downloadTwelve(request,plan_Name):
    response = HttpResponse(content_type='application/vnd.ms-excel') 
    response['Content-Disposition'] = 'attachment;filename=viewTwelve.xls'
    work_book = xlwt.Workbook(encoding = 'utf-8') 
    work_sheet = work_book.add_sheet(u'plan details')

    
     
    plan = models.TwelveMonthPlan.objects.filter(planName=plan_Name).values()
    for x in plan:
        ntwH1 = x['hiredTemporary1']
        ntwF1 = x['firedTemporary1']
        ntwH2 = x['hiredTemporary2']
        ntwF2 = x['firedTemporary2']
        ntwH3 = x['hiredTemporary3']
        ntwF3 = x['firedTemporary3']
        ntwH4 = x['hiredTemporary4']
        ntwF4 = x['firedTemporary4']
        ntwH5 = x['hiredTemporary5']
        ntwF5 = x['firedTemporary5']
        ntwH6 = x['hiredTemporary6']
        ntwF6 = x['firedTemporary6']
        ntwH7 = x['hiredTemporary7']
        ntwF7 = x['firedTemporary7']
        ntwH8 = x['hiredTemporary8']
        ntwF8 = x['firedTemporary8']
        ntwH9 = x['hiredTemporary9']
        ntwF9 = x['firedTemporary9']
        ntwH10 = x['hiredTemporary10']
        ntwF10 = x['firedTemporary10']
        ntwH11 = x['hiredTemporary11']
        ntwF11 = x['firedTemporary11']
        ntwH12 = x['hiredTemporary12']
        ntwF12 = x['firedTemporary12']
        rd1 = x['demand1'] - (x['numPermanent1'] * x['prodPermanent1'])
        if rd1 < 0:
            rd1 = 0
        hC1 = ntwH1 * x['costHiring1']
        fC1 = ntwF1 * x['costFiring1']
        ihc1 = x['costHoldingUnit1'] * x['inventoryMonth1']
        rd2 = x['demand2'] - (x['numPermanent2'] * x['prodPermanent2'])
        if rd2 < 0:
            rd2 = 0
        hC2 = ntwH2 * x['costHiring2']
        fC2 = ntwF2 * x['costFiring2']
        ihc2 = x['costHoldingUnit2'] * x['inventoryMonth2']
        rd3 = x['demand3'] - (x['numPermanent3'] * x['prodPermanent3'])
        if rd3 < 0:
            rd3 = 0
        hC3 = ntwH3 * x['costHiring3']
        fC3 = ntwF3 * x['costFiring3']
        ihc3 = x['costHoldingUnit3'] * x['inventoryMonth3']
        rd4 = x['demand4'] - (x['numPermanent4'] * x['prodPermanent4'])
        if rd4 < 0:
            rd4 = 0
        hC4 = ntwH4 * x['costHiring4']
        fC4 = ntwF4 * x['costFiring4']
        ihc4 = x['costHoldingUnit4'] * x['inventoryMonth4']
        rd5 = x['demand5'] - (x['numPermanent5'] * x['prodPermanent5'])
        if rd5 < 0:
            rd5 = 0
        hC5 = ntwH5 * x['costHiring5']
        fC5 = ntwF5 * x['costFiring5']
        ihc5 = x['costHoldingUnit5'] * x['inventoryMonth5']
        rd6 = x['demand6'] - (x['numPermanent6'] * x['prodPermanent6'])
        if rd6 < 0:
            rd6 = 0
        hC6 = ntwH6 * x['costHiring6']
        fC6 = ntwF6 * x['costFiring6']
        ihc6 = x['costHoldingUnit6'] * x['inventoryMonth6']
        rd7 = x['demand7'] - (x['numPermanent7'] * x['prodPermanent7'])
        if rd7 < 0:
            rd7 = 0
        hC7 = ntwH7 * x['costHiring7']
        fC7 = ntwF7 * x['costFiring7']
        ihc7 = x['costHoldingUnit7'] * x['inventoryMonth7']
        rd8 = x['demand8'] - (x['numPermanent8'] * x['prodPermanent8'])
        if rd8 < 0:
            rd8 = 0
        hC8 = ntwH8 * x['costHiring8']
        fC8 = ntwF8 * x['costFiring8']
        ihc8 = x['costHoldingUnit8'] * x['inventoryMonth8']
        rd9 = x['demand9'] - (x['numPermanent9'] * x['prodPermanent9'])
        if rd9 < 0:
            rd9 = 0
        hC9 = ntwH9 * x['costHiring9']
        fC9 = ntwF9 * x['costFiring9']
        ihc9 = x['costHoldingUnit9'] * x['inventoryMonth9']
        rd10 = x['demand10'] - (x['numPermanent10'] * x['prodPermanent10'])
        if rd10 < 0:
            rd10 = 0
        hC10 = ntwH10 * x['costHiring10']
        fC10 = ntwF10 * x['costFiring10']
        ihc10 = x['costHoldingUnit10'] * x['inventoryMonth10']
        rd11 = x['demand11'] - (x['numPermanent11'] * x['prodPermanent11'])
        if rd11 < 0:
            rd11 = 0
        hC11 = ntwH11 * x['costHiring11']
        fC11 = ntwF11 * x['costFiring11']
        ihc11 = x['costHoldingUnit11'] * x['inventoryMonth11']
        rd12 = x['demand12'] - (x['numPermanent12'] * x['prodPermanent12'])
        if rd12 < 0:
            rd12 = 0
        hC12 = ntwH12 * x['costHiring12']
        fC12 = ntwF12 * x['costFiring12']
        ihc12 = x['costHoldingUnit12'] * x['inventoryFinal']
        ntw1 = ntwH1 - ntwF1 
        ntw2 = ntwH1 - ntwF1 + ntwH2 - ntwF2 
        ntw3 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 
        ntw4 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4
        ntw5 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5
        ntw6 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6
        ntw7 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7
        ntw8 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8
        ntw9 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9
        ntw10 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9 + ntwH10 - ntwF10
        ntw11 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9 + ntwH10 - ntwF10 + ntwH11 - ntwF11
        ntw12 = ntwH1 - ntwF1 + ntwH2 - ntwF2 + ntwH3 - ntwF3 + ntwH4 - ntwF4 + ntwH5 - ntwF5 + ntwH6 - ntwF6 + ntwH7 - ntwF7 + ntwH8 - ntwF8 + ntwH9 - ntwF9 + ntwH10 - ntwF10 + ntwH11 - ntwF11 + ntwH12 - ntwF12
        thC = hC1 + hC2 + hC3 + hC4 + hC5 + hC6 + hC7 + hC8 + hC9 + hC10 + hC11 + hC12
        tfC = fC1 + fC2 + fC3 + fC4 + fC5 + fC6 + fC7 + fC8 + fC9 + fC10 + fC11 + fC12
        tihC = ihc1 + ihc2 + ihc3 + ihc4 + ihc5 + ihc6 + ihc7 + ihc8 + ihc9 + ihc10 + ihc11 + ihc12
        ei1 = x['inventoryMonth1']
        ei2 = x['inventoryMonth2']
        ei3 = x['inventoryMonth3']
        ei4 = x['inventoryMonth4']
        ei5 = x['inventoryMonth5']
        ei6 = x['inventoryMonth6']
        ei7 = x['inventoryMonth7']
        ei8 = x['inventoryMonth8']
        ei9 = x['inventoryMonth9']
        ei10 = x['inventoryMonth10']
        ei11 = x['inventoryMonth11']
        ei12 = x['inventoryFinal']
        optimalCost= x['optimalCost']

    work_sheet.write(0,0, 'MONTH', style_head_row) 
    work_sheet.write(0,1, 'REMAINING DEMAND', style_head_row) 
    work_sheet.write(0,2, 'ENDING INVENTORY UNIT(S)', style_head_row) 
    work_sheet.write(0,3, 'NUMBER OF TEMPORARY WORKER HIRED', style_head_row) 
    work_sheet.write(0,4, 'NUMBER OF TEMPORARY WORKER FIRED', style_head_row) 
    work_sheet.write(0,5, 'NUMBER OF TEMPORARY WORKER(S)', style_head_row) 
    work_sheet.write(0,6, 'HIRING COST', style_head_row) 
    work_sheet.write(0,7, 'FIRING COST', style_head_row) 
    work_sheet.write(0,8, 'INVENTORY HOLDING COST', style_head_row)

    work_sheet.write(1,0, 'MONTH 1', style_data_row) 
    work_sheet.write(1,1, rd1, style_data_row) 
    work_sheet.write(1,2, ei1, style_data_row) 
    work_sheet.write(1,3, ntwH1, style_data_row) 
    work_sheet.write(1,4, ntwF1, style_data_row) 
    work_sheet.write(1,5,ntw1, style_data_row) 
    work_sheet.write(1,6, hC1, style_data_row) 
    work_sheet.write(1,7, fC1, style_data_row) 
    work_sheet.write(1,8, ihc1, style_data_row)

    work_sheet.write(2,0, 'MONTH 2', style_data_row) 
    work_sheet.write(2,1, rd2, style_data_row) 
    work_sheet.write(2,2, ei2, style_data_row) 
    work_sheet.write(2,3, ntwH2, style_data_row) 
    work_sheet.write(2,4, ntwF2, style_data_row) 
    work_sheet.write(2,5,ntw2, style_data_row) 
    work_sheet.write(2,6, hC2, style_data_row) 
    work_sheet.write(2,7, fC2, style_data_row) 
    work_sheet.write(2,8, ihc2, style_data_row)

    work_sheet.write(3,0, 'MONTH 3', style_data_row) 
    work_sheet.write(3,1, rd3, style_data_row) 
    work_sheet.write(3,2, ei3, style_data_row) 
    work_sheet.write(3,3, ntwH3, style_data_row) 
    work_sheet.write(3,4, ntwF3, style_data_row) 
    work_sheet.write(3,5,ntw3, style_data_row) 
    work_sheet.write(3,6, hC3, style_data_row) 
    work_sheet.write(3,7, fC3, style_data_row) 
    work_sheet.write(3,8, ihc3, style_data_row)

    work_sheet.write(4,0, 'MONTH 4', style_data_row) 
    work_sheet.write(4,1, rd4, style_data_row) 
    work_sheet.write(4,2, ei4, style_data_row) 
    work_sheet.write(4,3, ntwH4, style_data_row) 
    work_sheet.write(4,4, ntwF4, style_data_row) 
    work_sheet.write(4,5, ntw4, style_data_row) 
    work_sheet.write(4,6, hC4, style_data_row) 
    work_sheet.write(4,7, fC4, style_data_row) 
    work_sheet.write(4,8, ihc4, style_data_row)

    work_sheet.write(5,0, 'MONTH 5', style_data_row) 
    work_sheet.write(5,1, rd5, style_data_row) 
    work_sheet.write(5,2, ei5, style_data_row) 
    work_sheet.write(5,3, ntwH5, style_data_row) 
    work_sheet.write(5,4, ntwF5, style_data_row) 
    work_sheet.write(5,5, ntw5, style_data_row) 
    work_sheet.write(5,6, hC5, style_data_row) 
    work_sheet.write(5,7, fC5, style_data_row) 
    work_sheet.write(5,8, ihc5, style_data_row)

    work_sheet.write(6,0, 'MONTH 6', style_data_row) 
    work_sheet.write(6,1, rd6, style_data_row) 
    work_sheet.write(6,2, ei6, style_data_row) 
    work_sheet.write(6,3, ntwH6, style_data_row) 
    work_sheet.write(6,4, ntwF6, style_data_row) 
    work_sheet.write(6,5, ntw6, style_data_row) 
    work_sheet.write(6,6, hC6, style_data_row) 
    work_sheet.write(6,7, fC6, style_data_row) 
    work_sheet.write(6,8, ihc6, style_data_row)

    work_sheet.write(7,0, 'MONTH 7', style_data_row) 
    work_sheet.write(7,1, rd7, style_data_row) 
    work_sheet.write(7,2, ei7, style_data_row) 
    work_sheet.write(7,3, ntwH7, style_data_row) 
    work_sheet.write(7,4, ntwF7, style_data_row) 
    work_sheet.write(7,5, ntw7, style_data_row) 
    work_sheet.write(7,6, hC7, style_data_row) 
    work_sheet.write(7,7, fC7, style_data_row) 
    work_sheet.write(7,8, ihc7, style_data_row)

    work_sheet.write(8,0, 'MONTH 8', style_data_row) 
    work_sheet.write(8,1, rd8, style_data_row) 
    work_sheet.write(8,2, ei8, style_data_row) 
    work_sheet.write(8,3, ntwH8, style_data_row) 
    work_sheet.write(8,4, ntwF8, style_data_row) 
    work_sheet.write(8,5, ntw8, style_data_row) 
    work_sheet.write(8,6, hC8, style_data_row) 
    work_sheet.write(8,7, fC8, style_data_row) 
    work_sheet.write(8,8, ihc8, style_data_row)

    work_sheet.write(9,0, 'MONTH 9', style_data_row) 
    work_sheet.write(9,1, rd9, style_data_row) 
    work_sheet.write(9,2, ei9, style_data_row) 
    work_sheet.write(9,3, ntwH9, style_data_row) 
    work_sheet.write(9,4, ntwF9, style_data_row) 
    work_sheet.write(9,5, ntw9, style_data_row) 
    work_sheet.write(9,6, hC9, style_data_row) 
    work_sheet.write(9,7, fC9, style_data_row) 
    work_sheet.write(9,8, ihc9, style_data_row)

    work_sheet.write(10,0, 'MONTH 10', style_data_row) 
    work_sheet.write(10,1, rd10, style_data_row) 
    work_sheet.write(10,2, ei10, style_data_row) 
    work_sheet.write(10,3, ntwH10, style_data_row) 
    work_sheet.write(10,4, ntwF10, style_data_row) 
    work_sheet.write(10,5, ntw10, style_data_row) 
    work_sheet.write(10,6, hC10, style_data_row) 
    work_sheet.write(10,7, fC10, style_data_row) 
    work_sheet.write(10,8, ihc10, style_data_row)

    work_sheet.write(11,0, 'MONTH 11', style_data_row) 
    work_sheet.write(11,1, rd11, style_data_row) 
    work_sheet.write(11,2, ei11, style_data_row) 
    work_sheet.write(11,3, ntwH11, style_data_row) 
    work_sheet.write(11,4, ntwF11, style_data_row) 
    work_sheet.write(11,5, ntw11, style_data_row) 
    work_sheet.write(11,6, hC11, style_data_row) 
    work_sheet.write(11,7, fC11, style_data_row) 
    work_sheet.write(11,8, ihc11, style_data_row)
    
    work_sheet.write(12,0, 'MONTH 12', style_data_row) 
    work_sheet.write(12,1, rd12, style_data_row) 
    work_sheet.write(12,2, ei12, style_data_row) 
    work_sheet.write(12,3, ntwH12, style_data_row) 
    work_sheet.write(12,4, ntwF12, style_data_row) 
    work_sheet.write(12,5, ntw12, style_data_row) 
    work_sheet.write(12,6, hC12, style_data_row) 
    work_sheet.write(12,7, fC12, style_data_row) 
    work_sheet.write(12,8, ihc12, style_data_row)

    work_sheet.write(13,0,'TOTAL INDIVIDUAL COSTS',style_data_row)
    work_sheet.write(13,6,thC,style_data_row)
    work_sheet.write(13,7,tfC,style_data_row)
    work_sheet.write(13,8,tihC,style_data_row)

    work_sheet.write(14,0,"OPTIMIZED FINAL COST FOR MULTI-PERIOD PLANNING",style_data_row)
    work_sheet.write(14,7,optimalCost,style_data_row)

    output = BytesIO()
    work_book.save(output)
    output.seek(0)
    response.write(output.getvalue()) 

    return response


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject=form.cleaned_data['subject']
            email=form.cleaned_data['email']
            content=form.cleaned_data['content']
            send_mail(subject=subject, message=content,from_email=settings.EMAIL_HOST_USER,recipient_list=[settings.RECIPIENT_ADDRESS])
            return redirect ("home")
    form = ContactForm()
    context = {'form': form}
    return render(request, 'main/contact.html', context)

def create_user(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = models.User.objects.create(
            first_name=first_name, last_name=last_name, username=username, email=email, password=password
        )
        return redirect("read")
    return render(request, "main/users/create.html")

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = models.User.objects.create(
            first_name=first_name, last_name=last_name, username=username, email=email, password=password
        )
        return redirect("login")
    return render(request, "main/signup.html")

@login_required(login_url='login/')
def read_user(request):
    # pk = request.user.id
    # user = models.User.objects.get(id=pk)
    userData = models.User.objects.all().values
    return render(request, 'main/users/read.html', {'userData': userData})

def update_user(request, id):
    # pk = request.user.id
    userData = models.User.objects.get(id=id)
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        is_active = request.POST.get("is_active")
        is_staff = request.POST.get("is_staff")
        is_superuser = request.POST.get("is_superuser")
        userData.first_name = first_name
        userData.last_name = last_name
        userData.email = email
        userData.is_active = (is_active == 'on')
        userData.is_staff = (is_staff == 'on')
        userData.is_superuser = (is_superuser == 'on')
        userData.save()
        return redirect("read")
    return render(request, "main/users/update.html", {"userData": userData})

def editprofile(request, id):
    # pk = request.user.id
    userData = models.User.objects.get(id=id)
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        userData.first_name = first_name
        userData.last_name = last_name
        userData.save()
        return redirect("/")
    return render(request, "main/editprofile.html", {"userData": userData})

def delete_user(request, id):
    # pk = request.user.id
    userData = models.User.objects.get(id=id)
    if request.method == "POST":
        userData.delete()
        return redirect("read")
    return render(request, "main/users/delete.html", {"userData": userData})