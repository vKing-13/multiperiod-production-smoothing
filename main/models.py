from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# class User(AbstractUser):
#   is_manager=models.BooleanField(default=False)
#   is_worker=models.BooleanField(default=False)
#   email=models.EmailField(blank=True, null=True)
#   phone = models.CharField(max_length=60, blank=True, null=True)

#   def get_full_name(self):
#     full_name = self.username
#     if self.first_name and self.last_name:
#         full_name = self.first_name + " " + self.last_name
#     return full_name


# class Manager(models.Model):
#   user=models.OneToOneField(User,on_delete=models.CASCADE)
#   id_number = models.CharField(max_length=20, unique=True)

#   def __str__(self):
#     return self.id_number

# class Worker(models.Model):
#   user=models.OneToOneField(User,on_delete=models.CASCADE)
#   id_number = models.CharField(max_length=20, unique=True)

#   def __str__(self):
#     return self.id_number


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

  # # Calculate Number of Temporary Workers Monthly
  # tempWorkerMonthly = models.DecimalField(decimal_places=2,max_digits=5) 

class RDDatabase(models.Model):
  # Calculate Remaining Demand Monthly
  month = models.IntegerField()
  demand=models.IntegerField() 
  productionPermanentWorker=models.IntegerField() 
  numPermanentWorker= models.IntegerField() 
  remainingDemand=models.IntegerField(null=True)

  # # Calculate Monthly Inventory Constraints
  # productionTempWorker=models.IntegerField() 
  # monthlyInventoryConstraints=models.IntegerField()

  

  
  