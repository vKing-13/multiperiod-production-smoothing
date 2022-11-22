from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def calculateFinalCost(response):
  return render(response,"main/calculate_final_cost.html",{})

def calculateFiringHiringCost(response):
  return render(response,"main/calculate_firing_hiring_cost.html",{})

def calculateInventoryConstraints(response):
  return render(response,"main/calculate_inventory_constraints.html",{})

def calculateInventoryHoldingCost(response):
  return render(response,"main/calculate_inventory_holding_cost.html",{})

def calculateNumOfTempWorkers(response):
  return render(response,"main/calculate_num_of_temp_workers.html",{})

def calculateRemainingDemand(response):
  return render(response,"main/calculate_remaining_demand.html",{})