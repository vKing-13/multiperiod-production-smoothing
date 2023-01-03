from django.db import models
from django.contrib.auth.models import User


class BossExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joindate = models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.first_name

    @property
    def get_id(self):
        return self.user.id

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

class PlanDatabase(models.Model):
    #Input
    planName = models.CharField(max_length=200)                                 # Plan Name
    demand1 = models.IntegerField()			                                    # Demand for Month 1
    demand2 = models.IntegerField()			                                    # Demand for Month 2
    demand3 = models.IntegerField()			                                    # Demand for Month 3
    demand4 = models.IntegerField()			                                    # Demand for Month 4
    numPermanent = models.IntegerField()		                                # Number of Permanent Worker(s)
    prodPermanent = models.IntegerField()		                                # Production of a Permanent Worker
    prodTemporary = models.IntegerField()		                                # Production of a Temporary Worker
    costHiring = models.DecimalField(max_digits=19, decimal_places=2)			# Temporary Worker Hiring Cost
    costFiring = models.DecimalField(max_digits=19, decimal_places=2)			# Temporary Worker Firing Cost
    costHoldingUnit = models.DecimalField(max_digits=19, decimal_places=2)		# Monthly Holding Cost per Unit
    inventoryInitial = models.IntegerField()	                                # Initial Inventory Level
    inventoryFinal = models.IntegerField()		                                # Final Inventory Level
    #Output
    inventoryMonth1 = models.IntegerField()                                     # Ending Inventory for Month 1
    inventoryMonth2 = models.IntegerField()                                     # Ending Inventory for Month 2
    inventoryMonth3 = models.IntegerField()                                     # Ending Inventory for Month 3
    hiredTemporary1 = models.IntegerField()                                     # Number of Temporary Worker Hired for Month 1
    hiredTemporary2 = models.IntegerField()                                     # Number of Temporary Worker Hired for Month 2
    hiredTemporary3 = models.IntegerField()                                     # Number of Temporary Worker Hired for Month 3
    hiredTemporary4 = models.IntegerField()                                     # Number of Temporary Worker Hired for Month 4
    firedTemporary1 = models.IntegerField()                                     # Number of Temporary Worker Fired for Month 1
    firedTemporary2 = models.IntegerField()                                     # Number of Temporary Worker Fired for Month 2
    firedTemporary3 = models.IntegerField()                                     # Number of Temporary Worker Fired for Month 3
    firedTemporary4 = models.IntegerField()                                     # Number of Temporary Worker Fired for Month 4
    optimalCost = models.DecimalField(max_digits=19, decimal_places=2)          # Optimized Cost for Multi-Period Planning 