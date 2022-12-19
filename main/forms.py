from django import forms
from .import models
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class BossUserForm(forms.ModelForm):
  class Meta:
    model=User
    fields=['first_name','last_name','username','email', 'password']
class BossExtraForm(forms.ModelForm):
  class Meta:
    model=models.BossExtra
    fields=['mobile','address']

class WorkerUserForm(forms.ModelForm):
  class Meta:
    model=User
    fields=['first_name','last_name','username','email', 'password']
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
        Row(
            Column('first_name', css_class='pb-2 text-2xl  text-center bg-clip-text text-transparent bg-gradient-to-r from-slate-900 to-blue-500 font-bold'),
            Column('last_name', css_class='pb-2 text-2xl  text-center bg-clip-text text-transparent bg-gradient-to-r from-slate-900 to-blue-500 font-bold'),

        ),
        #  Row(
        #     Column('username', css_class='pb-2 text-2xl  text-center bg-clip-text text-transparent bg-gradient-to-r from-slate-900 to-blue-500 font-bold'),
            
        # ),
         Row(
            'email', css_class='pb-2 text-2xl block text-center bg-clip-text text-transparent bg-gradient-to-r from-slate-900 to-blue-500 font-bold'
            
        ),
         Row(
           'password', css_class='pb-2 text-2xl block text-center bg-clip-text text-transparent bg-gradient-to-r from-slate-900 to-blue-500 font-bold'
            
        ),
        Submit('submit', 'Submit',css_class='bg-indigo-600 text-white py-2 w-full rounded-md drop-shadow-lg transition duration-300 ease-in-out hover:-translate-y-1 hover:scale-110 hover:bg-blue-500 hover:text-white font-bold')
    )
class WorkerExtraForm(forms.ModelForm):
  class Meta:
    model=models.WorkerExtra
    fields=['mobile','address']



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
    
class NTWForm(forms.ModelForm):
  class Meta:
    model =  models.NTWDatabase
    fields = ['month']
    labels = {"month": "Month"}
    
class ICForm(forms.ModelForm):
  class Meta:
    model =  models.ICDatabase
    fields=['month','productionTempWorker']
    labels = {"month": "Month",
              "productionTempWorker": "Production of Temporary Worker"}