from django import forms
from .import models
from django.contrib.auth.models import User


class BossUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class BossExtraForm(forms.ModelForm):
    class Meta:
        model = models.BossExtra
        fields = ['mobile', 'address']

class ContactForm(forms.Form):
    email=forms.EmailField()
    subject=forms.CharField(max_length=255)
    content=forms.CharField(widget=forms.Textarea)
    
# class WorkerUserForm(forms.ModelForm):
#   class Meta:
#     model=User
#     fields=['first_name','last_name','username','email', 'password']
# class WorkerExtraForm(forms.ModelForm):
#   class Meta:
#     model=models.WorkerExtra
#     fields=['mobile','address']


# class IHCForm(forms.ModelForm):
#   class Meta:
#     model =  models.IHCDatabase
#     fields=['month', 'holdingCostPerUnit', 'unitsOfEndingInventory']
#     labels = {'month': "Month", "holdingCostPerUnit": "Holding cost per unit", "unitsOfEndingInventory": "Ending inventory unit(s)"}

# class FHCForm(forms.ModelForm):
#   class Meta:
#     model =  models.FHCDatabase
#     fields=['month', 'tempWorkerHiringCost', 'tempWorkerFiringCost','tempWorkerHired','tempWorkerFired']
#     labels = {"month": "Month",
#               "tempWorkerHiringCost": "Temporary Worker Hiring Cost",
#               "tempWorkerFiringCost": "Temporary Worker Firing Cost",
#               "tempWorkerHired": "Number of Hired Temporary Worker",
#               "tempWorkerFired": "Number of Fired Temporary Worker"}

# class FCForm(forms.ModelForm):
#   class Meta:
#     model =  models.FCDatabase
#     fields = ['finalCost']
#     labels = {"finalCost": "Final Cost"}

# class RDForm(forms.ModelForm):
#   class Meta:
#     model =  models.RDDatabase
#     fields=['month', 'demand', 'productionPermanentWorker','numPermanentWorker']
#     labels = {"month": "Month",
#               "demand": "Demand",
#               "productionPermanentWorker": "Production Rate of A Permanent Worker",
#               "numPermanentWorker": "Number of Permanent Worker"}

# class NTWForm(forms.ModelForm):
#   class Meta:
#     model =  models.NTWDatabase
#     fields = ['month', 'tempWorkerMonthly']
#     labels = {"month": "Month","tempWorkerMonthly": "Number of Temporary Worker"}

# class ICForm(forms.ModelForm):
#   class Meta:
#     model =  models.ICDatabase
#     fields=['month','productionTempWorker']
#     labels = {"month": "Month",
#               "productionTempWorker": "Production of Temporary Worker"}