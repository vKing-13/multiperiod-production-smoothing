from django.urls import path

from . import views

urlpatterns=[
  path('',views.index,name="Home Page"),
  path('calculateFC/',views.calculateFinalCost,name="Calculate Final Cost"),
  path('calculateFHC/',views.calculateFiringHiringCost,name="Calculate Firing and Hiring Cost"),
  path('calculateIC/',views.calculateInventoryConstraints,name="Calculate Monthly Inventory Constraints"),
  path('calculateIHC/',views.calculateInventoryHoldingCost,name="Calculate Inventory Holding Cost"),
  path('calculateNTW/',views.calculateNumOfTempWorkers,name="Calculate Num. of Temp. Workers Monthly"),
  path('calculateRD/',views.calculateRemainingDemand,name="Calculate Remaining Demand Monthly"),
]