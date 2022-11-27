from django.shortcuts import render
from django.http import HttpResponse
from main import models,forms
# Create your views here.
def index(response):
  return render(response,"main/index.html",{})


def login(response):
  return render(response,'main/login.html',{})

def signup(response): 
  return render(response,'main/signup.html',{})

def calculateInventoryHoldingCost(request):
  form=forms.IHCForm()
  if request.method== "POST":
    form=forms.IHCForm(request.POST)
    #if form.is_valid():
      # 

  return render(request,"main/calculate_inventory_holding_cost.html",{'form':form})

def calculateFinalCost(response):
  return render(response,"main/calculate_final_cost.html",{})

def calculateFiringHiringCost(response):
  return render(response,"main/calculate_firing_hiring_cost.html",{})

def calculateInventoryConstraints(response):
  return render(response,"main/calculate_inventory_constraints.html",{})

def calculateNumOfTempWorkers(response):
  return render(response,"main/calculate_num_of_temp_workers.html",{})

def calculateRemainingDemand(response):
  return render(response,"main/calculate_remaining_demand.html",{})