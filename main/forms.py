from django import forms
from .import models
from django.contrib.auth.models import User
from django.forms import ValidationError

class IHCForm(forms.ModelForm):
  class Meta:
    model=  models.DataInput()
    fields=['month', 'holdingCostPerUnit', 'unitsOfEndingInventory','inventoryHoldingCost']
    

      