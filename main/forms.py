from django import forms
from .import models
from django.contrib.auth.models import User
from django.forms import ValidationError

class IHCForm(forms.ModelForm):
  class Meta:
    model =  models.IHCDatabase
    fields=['month', 'holdingCostPerUnit', 'unitsOfEndingInventory']
    labels = {'month': "Month", "holdingCostPerUnit": "Holding cost per unit", "unitsOfEndingInventory": "Ending inventory unit(s)"}

class FHCForm(forms.ModelForm):
  class Meta:
    model =  models.FHCDatabase
    fields=['month', 'tempWorkerHiringCost', 'tempWorkerFiringCost','tempWorkerHired','tempWorkerFired']
    labels = {"month": "Month", 
              "tempWorkerHiringCost": "Temporary Worker Hiring Cost", 
              "tempWorkerFiringCost": "Temporary Worker Firing Cost", 
              "tempWorkerHired": "Number of Hired Temporary Worker", 
              "tempWorkerFired": "Number of Fired Temporary Worker"}

class FCForm(forms.ModelForm):
  class Meta:
    model =  models.FCDatabase
    fields = ['finalCost']
    labels = {"finalCost": "Final Cost"}
    
class RDForm(forms.ModelForm):
  class Meta:
    model =  models.RDDatabase
    fields=['month', 'demand', 'productionPermanentWorker','numPermanentWorker']
    labels = {"month": "Month", 
              "demand": "Demand", 
              "productionPermanentWorker": "Production Rate of A Permanent Worker", 
              "numPermanentWorker": "Number of Permanent Worker"}