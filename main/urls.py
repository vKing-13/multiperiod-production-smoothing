from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .import views

urlpatterns=[
  path('',views.index,name="Home Page"),

  path('login/',views.login,name="Login"),
  path('worker-signup/',views.worker_signup_view ),
  path('worker-signup/worker_login/',LoginView.as_view(template_name="main/worker_login.html")),
  path('boss-signup/',views.boss_signup_view ),
  path('boss-signup/boss_login/',LoginView.as_view(template_name="main/boss_login.html")),


  path('calculateFC/',views.calculateFinalCost,name="Calculate Final Cost"),
  path('calculateFHC/',views.calculateFiringHiringCost,name="Calculate Firing and Hiring Cost"),
  path('calculateIC/',views.calculateInventoryConstraints,name="Calculate Monthly Inventory Constraints"),
  path('calculateIHC/',views.calculateInventoryHoldingCost,name="Calculate Inventory Holding Cost"),
  path('calculateNTW/',views.calculateNumOfTempWorkers,name="Calculate Num. of Temp. Workers Monthly"),
  path('calculateRD/',views.calculateRemainingDemand,name="Calculate Remaining Demand Monthly"),
  path('resetFinalCost/',views.resetFC,name="Reset Final Cost")
]