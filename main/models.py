from django.db import models
from django.contrib.auth.models import User


class BossExtra(models.Model):
  user= models.OneToOneField(User,on_delete=models.CASCADE)
  joindate=models.DateField(auto_now_add=True)
  mobile=models.CharField(max_length=40)
  address=models.CharField(max_length=200)
  def __str__(self):
        return self.user.first_name
  @property
  def get_id(self):
      return self.user.id
  @property
  def get_name(self):
      return self.user.first_name+" "+self.user.last_name

class WorkerExtra(models.Model):
  user= models.OneToOneField(User,on_delete=models.CASCADE)
  joindate=models.DateField(auto_now_add=True)
  mobile=models.CharField(max_length=40)
  address=models.CharField(max_length=200)
  def __str__(self):
        return self.user.first_name
  @property
  def get_id(self):
      return self.user.id
  @property
  def get_name(self):
      return self.user.first_name+" "+self.user.last_name


class IHCDatabase(models.Model):
  #calculate inventory holding cost monthly
  month = models.IntegerField()
  holdingCostPerUnit = models.DecimalField(max_digits=19, decimal_places=2) 
  unitsOfEndingInventory = models.IntegerField() 
  inventoryHoldingCost=models.DecimalField(max_digits=19, decimal_places=2, null=True)
  
class FHCDatabase(models.Model):
  #calculate firing and hiring cost
  month = models.IntegerField()
  tempWorkerHiringCost = models.DecimalField(max_digits=19, decimal_places=2) 
  tempWorkerFiringCost= models.DecimalField(max_digits=19, decimal_places=2) 
  tempWorkerHired=models.IntegerField() 
  tempWorkerFired=models.IntegerField() 
  hiringCost= models.DecimalField(max_digits=19, decimal_places=2, null=True)
  firingCost= models.DecimalField(max_digits=19, decimal_places=2, null=True)
  
class FCDatabase(models.Model):
  # Final Cost
  finalCost= models.DecimalField(max_digits=19, decimal_places=2, default=0)

class NTWDatabase(models.Model):
  # # Calculate Number of Temporary Workers Monthly
  tempWorkerMonthly = models.IntegerField(default=0) 

class RDDatabase(models.Model):
  # Calculate Remaining Demand Monthly
  month = models.IntegerField()
  demand=models.IntegerField() 
  productionPermanentWorker=models.IntegerField() 
  numPermanentWorker= models.IntegerField() 
  remainingDemand=models.IntegerField(null=True)

class ICDatabase(models.Model):
  # # Calculate Monthly Inventory Constraints
  month = models.IntegerField()
  productionTempWorker=models.IntegerField() 
  monthlyInventoryConstraints=models.IntegerField(null=True)



  
  