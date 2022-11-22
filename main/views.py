from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def calculate(response):
  return render(response,"main/calculate_final_cost.html",{})