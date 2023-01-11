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

class FourMonthPlan(models.Model):
    #Input
    planName = models.CharField(max_length=200)                                             # Plan Name
    # Month1
    demand1 = models.IntegerField(default=0)			                                    # Demand for Month 1
    numPermanent1 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 1
    prodPermanent1 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 1
    prodTemporary1 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 1
    costHiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 1
    costFiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 1
    costHoldingUnit1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 1
    # Month2
    demand2 = models.IntegerField(default=0)			                                    # Demand for Month 2
    numPermanent2 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 2
    prodPermanent2 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 2
    prodTemporary2 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 2
    costHiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 2
    costFiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 2
    costHoldingUnit2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 2
    # Month3
    demand3 = models.IntegerField(default=0)			                                    # Demand for Month 3
    numPermanent3 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 3
    prodPermanent3 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 3
    prodTemporary3 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 3
    costHiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 3
    costFiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 3
    costHoldingUnit3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 3
    # Month4
    demand4 = models.IntegerField(default=0)			                                    # Demand for Month 4
    numPermanent4 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 4
    prodPermanent4 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 4
    prodTemporary4 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 4
    costHiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 4
    costFiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 4
    costHoldingUnit4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 4
    
    inventoryInitial = models.IntegerField(default=0)	                                    # Initial Inventory Level
    inventoryFinal = models.IntegerField(default=0)		                                    # Final Inventory Level / Ending Inventory for Month 4 
    # Optimized Output
    inventoryMonth1 = models.IntegerField(default=0)                                        # Ending Inventory for Month 1
    inventoryMonth2 = models.IntegerField(default=0)                                        # Ending Inventory for Month 2
    inventoryMonth3 = models.IntegerField(default=0)                                        # Ending Inventory for Month 3
    hiredTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 1
    hiredTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 2
    hiredTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 3
    hiredTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 4
    firedTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 1
    firedTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 2
    firedTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 3
    firedTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 4
    optimalCost = models.DecimalField(max_digits=19, decimal_places=2, default=0)           # Optimized Cost for Multi-Period Planning 
    
class FiveMonthPlan(models.Model):
    #Input
    planName = models.CharField(max_length=200)                                             # Plan Name
    # Month1
    demand1 = models.IntegerField(default=0)			                                    # Demand for Month 1
    numPermanent1 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 1
    prodPermanent1 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 1
    prodTemporary1 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 1
    costHiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 1
    costFiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 1
    costHoldingUnit1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 1
    # Month2
    demand2 = models.IntegerField(default=0)			                                    # Demand for Month 2
    numPermanent2 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 2
    prodPermanent2 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 2
    prodTemporary2 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 2
    costHiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 2
    costFiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 2
    costHoldingUnit2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 2
    # Month3
    demand3 = models.IntegerField(default=0)			                                    # Demand for Month 3
    numPermanent3 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 3
    prodPermanent3 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 3
    prodTemporary3 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 3
    costHiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 3
    costFiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 3
    costHoldingUnit3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 3
    # Month4
    demand4 = models.IntegerField(default=0)			                                    # Demand for Month 4
    numPermanent4 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 4
    prodPermanent4 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 4
    prodTemporary4 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 4
    costHiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 4
    costFiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 4
    costHoldingUnit4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 4
    # Month5
    demand5 = models.IntegerField(default=0)			                                    # Demand for Month 5
    numPermanent5 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 5
    prodPermanent5 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 5
    prodTemporary5 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 5
    costHiring5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 5
    costFiring5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 5
    costHoldingUnit5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 5
    
    inventoryInitial = models.IntegerField(default=0)	                                    # Initial Inventory Level
    inventoryFinal = models.IntegerField(default=0)		                                    # Final Inventory Level / Ending Inventory for Month 5 
    # Optimized Output
    inventoryMonth1 = models.IntegerField(default=0)                                        # Ending Inventory for Month 1
    inventoryMonth2 = models.IntegerField(default=0)                                        # Ending Inventory for Month 2
    inventoryMonth3 = models.IntegerField(default=0)                                        # Ending Inventory for Month 3
    inventoryMonth4 = models.IntegerField(default=0)                                        # Ending Inventory for Month 4
    hiredTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 1
    hiredTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 2
    hiredTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 3
    hiredTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 4
    hiredTemporary5 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 5
    firedTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 1
    firedTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 2
    firedTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 3
    firedTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 4
    firedTemporary5 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 5
    optimalCost = models.DecimalField(max_digits=19, decimal_places=2, default=0)           # Optimized Cost for Multi-Period Planning 
    
class SixMonthPlan(models.Model):
    #Input
    planName = models.CharField(max_length=200)                                             # Plan Name
    # Month1
    demand1 = models.IntegerField(default=0)			                                    # Demand for Month 1
    numPermanent1 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 1
    prodPermanent1 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 1
    prodTemporary1 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 1
    costHiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 1
    costFiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 1
    costHoldingUnit1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 1
    # Month2
    demand2 = models.IntegerField(default=0)			                                    # Demand for Month 2
    numPermanent2 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 2
    prodPermanent2 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 2
    prodTemporary2 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 2
    costHiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 2
    costFiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 2
    costHoldingUnit2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 2
    # Month3
    demand3 = models.IntegerField(default=0)			                                    # Demand for Month 3
    numPermanent3 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 3
    prodPermanent3 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 3
    prodTemporary3 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 3
    costHiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 3
    costFiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 3
    costHoldingUnit3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 3
    # Month4
    demand4 = models.IntegerField(default=0)			                                    # Demand for Month 4
    numPermanent4 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 4
    prodPermanent4 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 4
    prodTemporary4 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 4
    costHiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 4
    costFiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 4
    costHoldingUnit4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 4
    # Month5
    demand5 = models.IntegerField(default=0)			                                    # Demand for Month 5
    numPermanent5 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 5
    prodPermanent5 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 5
    prodTemporary5 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 5
    costHiring5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 5
    costFiring5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 5
    costHoldingUnit5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 5
    # Month6
    demand6 = models.IntegerField(default=0)			                                    # Demand for Month 6
    numPermanent6 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 6
    prodPermanent6 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 6
    prodTemporary6 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 6
    costHiring6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 6
    costFiring6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 6
    costHoldingUnit6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 6
    
    inventoryInitial = models.IntegerField(default=0)	                                    # Initial Inventory Level
    inventoryFinal = models.IntegerField(default=0)		                                    # Final Inventory Level / Ending Inventory for Month 6 
    # Optimized Output
    inventoryMonth1 = models.IntegerField(default=0)                                        # Ending Inventory for Month 1
    inventoryMonth2 = models.IntegerField(default=0)                                        # Ending Inventory for Month 2
    inventoryMonth3 = models.IntegerField(default=0)                                        # Ending Inventory for Month 3
    inventoryMonth4 = models.IntegerField(default=0)                                        # Ending Inventory for Month 4
    inventoryMonth5 = models.IntegerField(default=0)                                        # Ending Inventory for Month 5
    hiredTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 1
    hiredTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 2
    hiredTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 3
    hiredTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 4
    hiredTemporary5 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 5
    hiredTemporary6 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 6
    firedTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 1
    firedTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 2
    firedTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 3
    firedTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 4
    firedTemporary5 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 5
    firedTemporary6 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 6
    optimalCost = models.DecimalField(max_digits=19, decimal_places=2, default=0)           # Optimized Cost for Multi-Period Planning 
    
class SevenMonthPlan(models.Model):
    #Input
    planName = models.CharField(max_length=200)                                             # Plan Name
    # Month1
    demand1 = models.IntegerField(default=0)			                                    # Demand for Month 1
    numPermanent1 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 1
    prodPermanent1 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 1
    prodTemporary1 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 1
    costHiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 1
    costFiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 1
    costHoldingUnit1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 1
    # Month2
    demand2 = models.IntegerField(default=0)			                                    # Demand for Month 2
    numPermanent2 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 2
    prodPermanent2 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 2
    prodTemporary2 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 2
    costHiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 2
    costFiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 2
    costHoldingUnit2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 2
    # Month3
    demand3 = models.IntegerField(default=0)			                                    # Demand for Month 3
    numPermanent3 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 3
    prodPermanent3 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 3
    prodTemporary3 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 3
    costHiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 3
    costFiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 3
    costHoldingUnit3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 3
    # Month4
    demand4 = models.IntegerField(default=0)			                                    # Demand for Month 4
    numPermanent4 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 4
    prodPermanent4 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 4
    prodTemporary4 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 4
    costHiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 4
    costFiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 4
    costHoldingUnit4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 4
    # Month5
    demand5 = models.IntegerField(default=0)			                                    # Demand for Month 5
    numPermanent5 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 5
    prodPermanent5 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 5
    prodTemporary5 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 5
    costHiring5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 5
    costFiring5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 5
    costHoldingUnit5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 5
    # Month6
    demand6 = models.IntegerField(default=0)			                                    # Demand for Month 6
    numPermanent6 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 6
    prodPermanent6 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 6
    prodTemporary6 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 6
    costHiring6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 6
    costFiring6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 6
    costHoldingUnit6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 6
    # Month7
    demand7 = models.IntegerField(default=0)			                                    # Demand for Month 7
    numPermanent7 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 7
    prodPermanent7 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 7
    prodTemporary7 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 7
    costHiring7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 7
    costFiring7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 7
    costHoldingUnit7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 7
    
    inventoryInitial = models.IntegerField(default=0)	                                    # Initial Inventory Level
    inventoryFinal = models.IntegerField(default=0)		                                    # Final Inventory Level / Ending Inventory for Month 7 
    # Optimized Output
    inventoryMonth1 = models.IntegerField(default=0)                                        # Ending Inventory for Month 1
    inventoryMonth2 = models.IntegerField(default=0)                                        # Ending Inventory for Month 2
    inventoryMonth3 = models.IntegerField(default=0)                                        # Ending Inventory for Month 3
    inventoryMonth4 = models.IntegerField(default=0)                                        # Ending Inventory for Month 4
    inventoryMonth5 = models.IntegerField(default=0)                                        # Ending Inventory for Month 5
    inventoryMonth6 = models.IntegerField(default=0)                                        # Ending Inventory for Month 6
    hiredTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 1
    hiredTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 2
    hiredTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 3
    hiredTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 4
    hiredTemporary5 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 5
    hiredTemporary6 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 6
    hiredTemporary7 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 7
    firedTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 1
    firedTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 2
    firedTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 3
    firedTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 4
    firedTemporary5 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 5
    firedTemporary6 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 6
    firedTemporary7 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 7
    optimalCost = models.DecimalField(max_digits=19, decimal_places=2, default=0)           # Optimized Cost for Multi-Period Planning 

class EightMonthPlan(models.Model):
    #Input
    planName = models.CharField(max_length=200)                                             # Plan Name
    # Month1
    demand1 = models.IntegerField(default=0)			                                    # Demand for Month 1
    numPermanent1 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 1
    prodPermanent1 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 1
    prodTemporary1 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 1
    costHiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 1
    costFiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 1
    costHoldingUnit1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 1
    # Month2
    demand2 = models.IntegerField(default=0)			                                    # Demand for Month 2
    numPermanent2 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 2
    prodPermanent2 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 2
    prodTemporary2 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 2
    costHiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 2
    costFiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 2
    costHoldingUnit2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 2
    # Month3
    demand3 = models.IntegerField(default=0)			                                    # Demand for Month 3
    numPermanent3 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 3
    prodPermanent3 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 3
    prodTemporary3 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 3
    costHiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 3
    costFiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 3
    costHoldingUnit3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 3
    # Month4
    demand4 = models.IntegerField(default=0)			                                    # Demand for Month 4
    numPermanent4 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 4
    prodPermanent4 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 4
    prodTemporary4 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 4
    costHiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 4
    costFiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 4
    costHoldingUnit4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 4
    # Month5
    demand5 = models.IntegerField(default=0)			                                    # Demand for Month 5
    numPermanent5 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 5
    prodPermanent5 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 5
    prodTemporary5 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 5
    costHiring5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 5
    costFiring5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 5
    costHoldingUnit5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 5
    # Month6
    demand6 = models.IntegerField(default=0)			                                    # Demand for Month 6
    numPermanent6 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 6
    prodPermanent6 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 6
    prodTemporary6 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 6
    costHiring6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 6
    costFiring6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 6
    costHoldingUnit6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 6
    # Month7
    demand7 = models.IntegerField(default=0)			                                    # Demand for Month 7
    numPermanent7 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 7
    prodPermanent7 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 7
    prodTemporary7 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 7
    costHiring7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 7
    costFiring7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 7
    costHoldingUnit7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 7
    # Month8
    demand8 = models.IntegerField(default=0)			                                    # Demand for Month 8
    numPermanent8 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 8
    prodPermanent8 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 8
    prodTemporary8 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 8
    costHiring8 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 8
    costFiring8 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 8
    costHoldingUnit8 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 8
    
    inventoryInitial = models.IntegerField(default=0)	                                    # Initial Inventory Level
    inventoryFinal = models.IntegerField(default=0)		                                    # Final Inventory Level / Ending Inventory for Month 8
    # Optimized Output
    inventoryMonth1 = models.IntegerField(default=0)                                        # Ending Inventory for Month 1
    inventoryMonth2 = models.IntegerField(default=0)                                        # Ending Inventory for Month 2
    inventoryMonth3 = models.IntegerField(default=0)                                        # Ending Inventory for Month 3
    inventoryMonth4 = models.IntegerField(default=0)                                        # Ending Inventory for Month 4
    inventoryMonth5 = models.IntegerField(default=0)                                        # Ending Inventory for Month 5
    inventoryMonth6 = models.IntegerField(default=0)                                        # Ending Inventory for Month 6
    inventoryMonth7 = models.IntegerField(default=0)                                        # Ending Inventory for Month 7
    hiredTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 1
    hiredTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 2
    hiredTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 3
    hiredTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 4
    hiredTemporary5 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 5
    hiredTemporary6 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 6
    hiredTemporary7 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 7
    hiredTemporary8 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 8
    firedTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 1
    firedTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 2
    firedTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 3
    firedTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 4
    firedTemporary5 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 5
    firedTemporary6 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 6
    firedTemporary7 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 7
    firedTemporary8 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 8
    optimalCost = models.DecimalField(max_digits=19, decimal_places=2, default=0)           # Optimized Cost for Multi-Period Planning 
    
class NineMonthPlan(models.Model):
    #Input
    planName = models.CharField(max_length=200)                                             # Plan Name
    # Month1
    demand1 = models.IntegerField(default=0)			                                    # Demand for Month 1
    numPermanent1 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 1
    prodPermanent1 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 1
    prodTemporary1 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 1
    costHiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 1
    costFiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 1
    costHoldingUnit1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 1
    # Month2
    demand2 = models.IntegerField(default=0)			                                    # Demand for Month 2
    numPermanent2 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 2
    prodPermanent2 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 2
    prodTemporary2 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 2
    costHiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 2
    costFiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 2
    costHoldingUnit2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 2
    # Month3
    demand3 = models.IntegerField(default=0)			                                    # Demand for Month 3
    numPermanent3 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 3
    prodPermanent3 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 3
    prodTemporary3 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 3
    costHiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 3
    costFiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 3
    costHoldingUnit3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 3
    # Month4
    demand4 = models.IntegerField(default=0)			                                    # Demand for Month 4
    numPermanent4 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 4
    prodPermanent4 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 4
    prodTemporary4 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 4
    costHiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 4
    costFiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 4
    costHoldingUnit4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 4
    # Month5
    demand5 = models.IntegerField(default=0)			                                    # Demand for Month 5
    numPermanent5 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 5
    prodPermanent5 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 5
    prodTemporary5 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 5
    costHiring5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 5
    costFiring5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 5
    costHoldingUnit5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 5
    # Month6
    demand6 = models.IntegerField(default=0)			                                    # Demand for Month 6
    numPermanent6 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 6
    prodPermanent6 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 6
    prodTemporary6 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 6
    costHiring6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 6
    costFiring6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 6
    costHoldingUnit6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 6
    # Month7
    demand7 = models.IntegerField(default=0)			                                    # Demand for Month 7
    numPermanent7 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 7
    prodPermanent7 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 7
    prodTemporary7 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 7
    costHiring7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 7
    costFiring7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 7
    costHoldingUnit7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 7
    # Month8
    demand8 = models.IntegerField(default=0)			                                    # Demand for Month 8
    numPermanent8 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 8
    prodPermanent8 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 8
    prodTemporary8 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 8
    costHiring8 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 8
    costFiring8 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 8
    costHoldingUnit8 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 8
    # Month9
    demand9 = models.IntegerField(default=0)			                                    # Demand for Month 9
    numPermanent9 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 9
    prodPermanent9 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 9
    prodTemporary9 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 9
    costHiring9 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 9
    costFiring9 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 9
    costHoldingUnit9 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 9
    
    inventoryInitial = models.IntegerField(default=0)	                                    # Initial Inventory Level
    inventoryFinal = models.IntegerField(default=0)		                                    # Final Inventory Level / Ending Inventory for Month 9
    # Optimized Output
    inventoryMonth1 = models.IntegerField(default=0)                                        # Ending Inventory for Month 1
    inventoryMonth2 = models.IntegerField(default=0)                                        # Ending Inventory for Month 2
    inventoryMonth3 = models.IntegerField(default=0)                                        # Ending Inventory for Month 3
    inventoryMonth4 = models.IntegerField(default=0)                                        # Ending Inventory for Month 4
    inventoryMonth5 = models.IntegerField(default=0)                                        # Ending Inventory for Month 5
    inventoryMonth6 = models.IntegerField(default=0)                                        # Ending Inventory for Month 6
    inventoryMonth7 = models.IntegerField(default=0)                                        # Ending Inventory for Month 7
    inventoryMonth8 = models.IntegerField(default=0)                                        # Ending Inventory for Month 8
    hiredTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 1
    hiredTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 2
    hiredTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 3
    hiredTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 4
    hiredTemporary5 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 5
    hiredTemporary6 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 6
    hiredTemporary7 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 7
    hiredTemporary8 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 8
    hiredTemporary9 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 9
    firedTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 1
    firedTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 2
    firedTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 3
    firedTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 4
    firedTemporary5 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 5
    firedTemporary6 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 6
    firedTemporary7 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 7
    firedTemporary8 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 8
    firedTemporary9 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 9
    optimalCost = models.DecimalField(max_digits=19, decimal_places=2, default=0)           # Optimized Cost for Multi-Period Planning 
    
class TenMonthPlan(models.Model):
    #Input
    planName = models.CharField(max_length=200)                                             # Plan Name
    # Month1
    demand1 = models.IntegerField(default=0)			                                    # Demand for Month 1
    numPermanent1 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 1
    prodPermanent1 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 1
    prodTemporary1 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 1
    costHiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 1
    costFiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 1
    costHoldingUnit1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 1
    # Month2
    demand2 = models.IntegerField(default=0)			                                    # Demand for Month 2
    numPermanent2 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 2
    prodPermanent2 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 2
    prodTemporary2 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 2
    costHiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 2
    costFiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 2
    costHoldingUnit2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 2
    # Month3
    demand3 = models.IntegerField(default=0)			                                    # Demand for Month 3
    numPermanent3 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 3
    prodPermanent3 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 3
    prodTemporary3 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 3
    costHiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 3
    costFiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 3
    costHoldingUnit3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 3
    # Month4
    demand4 = models.IntegerField(default=0)			                                    # Demand for Month 4
    numPermanent4 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 4
    prodPermanent4 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 4
    prodTemporary4 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 4
    costHiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 4
    costFiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 4
    costHoldingUnit4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 4
    # Month5
    demand5 = models.IntegerField(default=0)			                                    # Demand for Month 5
    numPermanent5 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 5
    prodPermanent5 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 5
    prodTemporary5 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 5
    costHiring5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 5
    costFiring5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 5
    costHoldingUnit5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 5
    # Month6
    demand6 = models.IntegerField(default=0)			                                    # Demand for Month 6
    numPermanent6 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 6
    prodPermanent6 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 6
    prodTemporary6 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 6
    costHiring6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 6
    costFiring6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 6
    costHoldingUnit6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 6
    # Month7
    demand7 = models.IntegerField(default=0)			                                    # Demand for Month 7
    numPermanent7 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 7
    prodPermanent7 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 7
    prodTemporary7 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 7
    costHiring7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 7
    costFiring7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 7
    costHoldingUnit7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 7
    # Month8
    demand8 = models.IntegerField(default=0)			                                    # Demand for Month 8
    numPermanent8 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 8
    prodPermanent8 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 8
    prodTemporary8 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 8
    costHiring8 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 8
    costFiring8 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 8
    costHoldingUnit8 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 8
    # Month9
    demand9 = models.IntegerField(default=0)			                                    # Demand for Month 9
    numPermanent9 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 9
    prodPermanent9 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 9
    prodTemporary9 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 9
    costHiring9 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 9
    costFiring9 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 9
    costHoldingUnit9 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 9
    # Month10
    demand10 = models.IntegerField(default=0)			                                    # Demand for Month 10
    numPermanent10 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 10
    prodPermanent10 = models.IntegerField(default=1)		                                # Production of a Permanent Worker for Month 10
    prodTemporary10 = models.IntegerField(default=1)		                                # Production of a Temporary Worker for Month 10
    costHiring10 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 10
    costFiring10 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 10
    costHoldingUnit10 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 10
    
    inventoryInitial = models.IntegerField(default=0)	                                    # Initial Inventory Level
    inventoryFinal = models.IntegerField(default=0)		                                    # Final Inventory Level / Ending Inventory for Month 10
    # Optimized Output
    inventoryMonth1 = models.IntegerField(default=0)                                        # Ending Inventory for Month 1
    inventoryMonth2 = models.IntegerField(default=0)                                        # Ending Inventory for Month 2
    inventoryMonth3 = models.IntegerField(default=0)                                        # Ending Inventory for Month 3
    inventoryMonth4 = models.IntegerField(default=0)                                        # Ending Inventory for Month 4
    inventoryMonth5 = models.IntegerField(default=0)                                        # Ending Inventory for Month 5
    inventoryMonth6 = models.IntegerField(default=0)                                        # Ending Inventory for Month 6
    inventoryMonth7 = models.IntegerField(default=0)                                        # Ending Inventory for Month 7
    inventoryMonth8 = models.IntegerField(default=0)                                        # Ending Inventory for Month 8
    inventoryMonth9 = models.IntegerField(default=0)                                        # Ending Inventory for Month 9
    hiredTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 1
    hiredTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 2
    hiredTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 3
    hiredTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 4
    hiredTemporary5 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 5
    hiredTemporary6 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 6
    hiredTemporary7 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 7
    hiredTemporary8 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 8
    hiredTemporary9 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 9
    hiredTemporary10 = models.IntegerField(default=0)                                       # Number of Temporary Worker Hired for Month 10
    firedTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 1
    firedTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 2
    firedTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 3
    firedTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 4
    firedTemporary5 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 5
    firedTemporary6 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 6
    firedTemporary7 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 7
    firedTemporary8 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 8
    firedTemporary9 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 9
    firedTemporary10 = models.IntegerField(default=0)                                       # Number of Temporary Worker Fired for Month 10
    optimalCost = models.DecimalField(max_digits=19, decimal_places=2, default=0)           # Optimized Cost for Multi-Period Planning
    
class ElevenMonthPlan(models.Model):
    #Input
    planName = models.CharField(max_length=200)                                             # Plan Name
    # Month1
    demand1 = models.IntegerField(default=0)			                                    # Demand for Month 1
    numPermanent1 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 1
    prodPermanent1 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 1
    prodTemporary1 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 1
    costHiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 1
    costFiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 1
    costHoldingUnit1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 1
    # Month2
    demand2 = models.IntegerField(default=0)			                                    # Demand for Month 2
    numPermanent2 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 2
    prodPermanent2 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 2
    prodTemporary2 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 2
    costHiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 2
    costFiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 2
    costHoldingUnit2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 2
    # Month3
    demand3 = models.IntegerField(default=0)			                                    # Demand for Month 3
    numPermanent3 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 3
    prodPermanent3 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 3
    prodTemporary3 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 3
    costHiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 3
    costFiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 3
    costHoldingUnit3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 3
    # Month4
    demand4 = models.IntegerField(default=0)			                                    # Demand for Month 4
    numPermanent4 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 4
    prodPermanent4 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 4
    prodTemporary4 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 4
    costHiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 4
    costFiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 4
    costHoldingUnit4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 4
    # Month5
    demand5 = models.IntegerField(default=0)			                                    # Demand for Month 5
    numPermanent5 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 5
    prodPermanent5 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 5
    prodTemporary5 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 5
    costHiring5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 5
    costFiring5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 5
    costHoldingUnit5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 5
    # Month6
    demand6 = models.IntegerField(default=0)			                                    # Demand for Month 6
    numPermanent6 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 6
    prodPermanent6 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 6
    prodTemporary6 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 6
    costHiring6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 6
    costFiring6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 6
    costHoldingUnit6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 6
    # Month7
    demand7 = models.IntegerField(default=0)			                                    # Demand for Month 7
    numPermanent7 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 7
    prodPermanent7 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 7
    prodTemporary7 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 7
    costHiring7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 7
    costFiring7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 7
    costHoldingUnit7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 7
    # Month8
    demand8 = models.IntegerField(default=0)			                                    # Demand for Month 8
    numPermanent8 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 8
    prodPermanent8 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 8
    prodTemporary8 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 8
    costHiring8 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 8
    costFiring8 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 8
    costHoldingUnit8 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 8
    # Month9
    demand9 = models.IntegerField(default=0)			                                    # Demand for Month 9
    numPermanent9 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 9
    prodPermanent9 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 9
    prodTemporary9 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 9
    costHiring9 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 9
    costFiring9 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 9
    costHoldingUnit9 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 9
    # Month10
    demand10 = models.IntegerField(default=0)			                                    # Demand for Month 10
    numPermanent10 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 10
    prodPermanent10 = models.IntegerField(default=1)		                                # Production of a Permanent Worker for Month 10
    prodTemporary10 = models.IntegerField(default=1)		                                # Production of a Temporary Worker for Month 10
    costHiring10 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 10
    costFiring10 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 10
    costHoldingUnit10 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 10
    # Month11
    demand11 = models.IntegerField(default=0)			                                    # Demand for Month 11
    numPermanent11 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 11
    prodPermanent11 = models.IntegerField(default=1)		                                # Production of a Permanent Worker for Month 11
    prodTemporary11 = models.IntegerField(default=1)		                                # Production of a Temporary Worker for Month 11
    costHiring11 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 11
    costFiring11 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 11
    costHoldingUnit11 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 11
    
    inventoryInitial = models.IntegerField(default=0)	                                    # Initial Inventory Level
    inventoryFinal = models.IntegerField(default=0)		                                    # Final Inventory Level / Ending Inventory for Month 11
    # Optimized Output
    inventoryMonth1 = models.IntegerField(default=0)                                        # Ending Inventory for Month 1
    inventoryMonth2 = models.IntegerField(default=0)                                        # Ending Inventory for Month 2
    inventoryMonth3 = models.IntegerField(default=0)                                        # Ending Inventory for Month 3
    inventoryMonth4 = models.IntegerField(default=0)                                        # Ending Inventory for Month 4
    inventoryMonth5 = models.IntegerField(default=0)                                        # Ending Inventory for Month 5
    inventoryMonth6 = models.IntegerField(default=0)                                        # Ending Inventory for Month 6
    inventoryMonth7 = models.IntegerField(default=0)                                        # Ending Inventory for Month 7
    inventoryMonth8 = models.IntegerField(default=0)                                        # Ending Inventory for Month 8
    inventoryMonth9 = models.IntegerField(default=0)                                        # Ending Inventory for Month 9
    inventoryMonth10 = models.IntegerField(default=0)                                       # Ending Inventory for Month 10
    hiredTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 1
    hiredTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 2
    hiredTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 3
    hiredTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 4
    hiredTemporary5 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 5
    hiredTemporary6 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 6
    hiredTemporary7 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 7
    hiredTemporary8 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 8
    hiredTemporary9 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 9
    hiredTemporary10 = models.IntegerField(default=0)                                       # Number of Temporary Worker Hired for Month 10
    hiredTemporary11 = models.IntegerField(default=0)                                       # Number of Temporary Worker Hired for Month 11
    firedTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 1
    firedTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 2
    firedTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 3
    firedTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 4
    firedTemporary5 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 5
    firedTemporary6 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 6
    firedTemporary7 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 7
    firedTemporary8 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 8
    firedTemporary9 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 9
    firedTemporary10 = models.IntegerField(default=0)                                       # Number of Temporary Worker Fired for Month 10
    firedTemporary11 = models.IntegerField(default=0)                                       # Number of Temporary Worker Fired for Month 11
    optimalCost = models.DecimalField(max_digits=19, decimal_places=2, default=0)           # Optimized Cost for Multi-Period Planning 
    
class TwelveMonthPlan(models.Model):
    #Input
    planName = models.CharField(max_length=200)                                             # Plan Name
    # Month1
    demand1 = models.IntegerField(default=0)			                                    # Demand for Month 1
    numPermanent1 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 1
    prodPermanent1 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 1
    prodTemporary1 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 1
    costHiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 1
    costFiring1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 1
    costHoldingUnit1 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 1
    # Month2
    demand2 = models.IntegerField(default=0)			                                    # Demand for Month 2
    numPermanent2 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 2
    prodPermanent2 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 2
    prodTemporary2 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 2
    costHiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 2
    costFiring2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 2
    costHoldingUnit2 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 2
    # Month3
    demand3 = models.IntegerField(default=0)			                                    # Demand for Month 3
    numPermanent3 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 3
    prodPermanent3 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 3
    prodTemporary3 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 3
    costHiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 3
    costFiring3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 3
    costHoldingUnit3 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 3
    # Month4
    demand4 = models.IntegerField(default=0)			                                    # Demand for Month 4
    numPermanent4 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 4
    prodPermanent4 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 4
    prodTemporary4 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 4
    costHiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 4
    costFiring4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 4
    costHoldingUnit4 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 4
    # Month5
    demand5 = models.IntegerField(default=0)			                                    # Demand for Month 5
    numPermanent5 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 5
    prodPermanent5 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 5
    prodTemporary5 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 5
    costHiring5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 5
    costFiring5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 5
    costHoldingUnit5 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 5
    # Month6
    demand6 = models.IntegerField(default=0)			                                    # Demand for Month 6
    numPermanent6 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 6
    prodPermanent6 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 6
    prodTemporary6 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 6
    costHiring6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 6
    costFiring6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 6
    costHoldingUnit6 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 6
    # Month7
    demand7 = models.IntegerField(default=0)			                                    # Demand for Month 7
    numPermanent7 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 7
    prodPermanent7 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 7
    prodTemporary7 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 7
    costHiring7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 7
    costFiring7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 7
    costHoldingUnit7 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 7
    # Month8
    demand8 = models.IntegerField(default=0)			                                    # Demand for Month 8
    numPermanent8 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 8
    prodPermanent8 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 8
    prodTemporary8 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 8
    costHiring8 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 8
    costFiring8 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 8
    costHoldingUnit8 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 8
    # Month9
    demand9 = models.IntegerField(default=0)			                                    # Demand for Month 9
    numPermanent9 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 9
    prodPermanent9 = models.IntegerField(default=1)		                                    # Production of a Permanent Worker for Month 9
    prodTemporary9 = models.IntegerField(default=1)		                                    # Production of a Temporary Worker for Month 9
    costHiring9 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 9
    costFiring9 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 9
    costHoldingUnit9 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 9
    # Month10
    demand10 = models.IntegerField(default=0)			                                    # Demand for Month 10
    numPermanent10 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 10
    prodPermanent10 = models.IntegerField(default=1)		                                # Production of a Permanent Worker for Month 10
    prodTemporary10 = models.IntegerField(default=1)		                                # Production of a Temporary Worker for Month 10
    costHiring10 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 10
    costFiring10 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 10
    costHoldingUnit10 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 10
    # Month11
    demand11 = models.IntegerField(default=0)			                                    # Demand for Month 11
    numPermanent11 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 11
    prodPermanent11 = models.IntegerField(default=1)		                                # Production of a Permanent Worker for Month 11
    prodTemporary11 = models.IntegerField(default=1)		                                # Production of a Temporary Worker for Month 11
    costHiring11 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 11
    costFiring11 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 11
    costHoldingUnit11 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 11
    # Month12
    demand12 = models.IntegerField(default=0)			                                    # Demand for Month 12
    numPermanent12 = models.IntegerField(default=0)		                                    # Number of Permanent Worker(s) for Month 12
    prodPermanent12 = models.IntegerField(default=1)		                                # Production of a Permanent Worker for Month 12
    prodTemporary12 = models.IntegerField(default=1)		                                # Production of a Temporary Worker for Month 12
    costHiring12 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Hiring Cost for Month 12
    costFiring12 = models.DecimalField(max_digits=19, decimal_places=2, default=1)			# Temporary Worker Firing Cost for Month 12
    costHoldingUnit12 = models.DecimalField(max_digits=19, decimal_places=2, default=1)		# Monthly Holding Cost per Unit for Month 12
    
    inventoryInitial = models.IntegerField(default=0)	                                    # Initial Inventory Level
    inventoryFinal = models.IntegerField(default=0)		                                    # Final Inventory Level / Ending Inventory for Month 12
    # Optimized Output
    inventoryMonth1 = models.IntegerField(default=0)                                        # Ending Inventory for Month 1
    inventoryMonth2 = models.IntegerField(default=0)                                        # Ending Inventory for Month 2
    inventoryMonth3 = models.IntegerField(default=0)                                        # Ending Inventory for Month 3
    inventoryMonth4 = models.IntegerField(default=0)                                        # Ending Inventory for Month 4
    inventoryMonth5 = models.IntegerField(default=0)                                        # Ending Inventory for Month 5
    inventoryMonth6 = models.IntegerField(default=0)                                        # Ending Inventory for Month 6
    inventoryMonth7 = models.IntegerField(default=0)                                        # Ending Inventory for Month 7
    inventoryMonth8 = models.IntegerField(default=0)                                        # Ending Inventory for Month 8
    inventoryMonth9 = models.IntegerField(default=0)                                        # Ending Inventory for Month 9
    inventoryMonth10 = models.IntegerField(default=0)                                       # Ending Inventory for Month 10
    inventoryMonth11 = models.IntegerField(default=0)                                       # Ending Inventory for Month 11
    hiredTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 1
    hiredTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 2
    hiredTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 3
    hiredTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 4
    hiredTemporary5 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 5
    hiredTemporary6 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 6
    hiredTemporary7 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 7
    hiredTemporary8 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 8
    hiredTemporary9 = models.IntegerField(default=0)                                        # Number of Temporary Worker Hired for Month 9
    hiredTemporary10 = models.IntegerField(default=0)                                       # Number of Temporary Worker Hired for Month 10
    hiredTemporary11 = models.IntegerField(default=0)                                       # Number of Temporary Worker Hired for Month 11
    hiredTemporary12 = models.IntegerField(default=0)                                       # Number of Temporary Worker Hired for Month 12
    firedTemporary1 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 1
    firedTemporary2 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 2
    firedTemporary3 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 3
    firedTemporary4 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 4
    firedTemporary5 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 5
    firedTemporary6 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 6
    firedTemporary7 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 7
    firedTemporary8 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 8
    firedTemporary9 = models.IntegerField(default=0)                                        # Number of Temporary Worker Fired for Month 9
    firedTemporary10 = models.IntegerField(default=0)                                       # Number of Temporary Worker Fired for Month 10
    firedTemporary11 = models.IntegerField(default=0)                                       # Number of Temporary Worker Fired for Month 11
    firedTemporary12 = models.IntegerField(default=0)                                       # Number of Temporary Worker Fired for Month 12
    optimalCost = models.DecimalField(max_digits=19, decimal_places=2, default=0)           # Optimized Cost for Multi-Period Planning 