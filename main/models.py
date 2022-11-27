from django.db import models
from django.contrib.auth.models import AbstractUser
from month.models import MonthField
# Create your models here.

class User(AbstractUser):
  is_manager=models.BooleanField(default=False)
  is_worker=models.BooleanField(default=False)
  email=models.EmailField(blank=True, null=True)
  phone = models.CharField(max_length=60, blank=True, null=True)

  def get_full_name(self):
    full_name = self.username
    if self.first_name and self.last_name:
        full_name = self.first_name + " " + self.last_name
    return full_name


class Manager(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE)
  id_number = models.CharField(max_length=20, unique=True)

  def __str__(self):
    return self.id_number

class Worker(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE)
  id_number = models.CharField(max_length=20, unique=True)

  def __str__(self):
    return self.id_number


class DataInput(models.Model):
  month = MonthField()
  
  #calculate inventory holding cost monthly
  holdingCostPerUnit = models.DecimalField() 
  unitsOfEndingInventory = models.IntegerField() 
  inventoryHoldingCost=models.DecimalField()
  
  #calculate firing and hiring cost
  tempWorkerHiringCost = models.DecimalField() 
  tempWorkerFiringCost= models.DecimalField() 
  tempWorkerHired=models.IntegerField() 
  tempWorkerFired=models.IntegerField() 
  firingCost= models.DecimalField()
  hiringCost= models.DecimalField()
  
  # Final Cost
  finalCost= models.DecimalField()

  # Calculate Number of Temporary Workers Monthly
  tempWorkerMonthly = models.DecimalField() 

  # Calculate Remaining Demand Monthly
  demand=models.IntegerField() 
  productionPermanentWorker=models.IntegerField() 
  numPermanentWorker= models.IntegerField() 
  remainingDemand=models.IntegerField()

  # Calculate Monthly Inventory Constraints
  productionTempWorker=models.IntegerField() 
  monthlyInventoryConstraints=models.IntegerField()


  

  
  