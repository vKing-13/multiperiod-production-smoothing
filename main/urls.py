from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from .import views

urlpatterns=[
  path('',views.index,name="home"),

  path('worker-signup/',views.worker_signup_view ),
  path('worker-signup/worker_login/',LoginView.as_view(template_name="main/worker_login.html")),

  path('boss-signup/',views.boss_signup_view ),
  path('boss-signup/boss_login/',LoginView.as_view(template_name="main/boss_login.html")),

  path('admin-login/',LoginView.as_view(template_name="main/admin_login.html")),

  path('admin_view_user/',views.admin_view_user_view,name="admin_view_user"),

  path('calculateFC/',views.calculateFinalCost,name="Calculate Final Cost"),
  path('calculateFHC/',views.calculateFiringHiringCost,name="Calculate Firing and Hiring Cost"),
  path('calculateIC/',views.calculateInventoryConstraints,name="Calculate Monthly Inventory Constraints"),
  path('calculateIHC/',views.calculateInventoryHoldingCost,name="Calculate Inventory Holding Cost"),
  path('calculateNTW/',views.calculateNumOfTempWorkers,name="Calculate Num. of Temp. Workers Monthly"),
  path('calculateRD/',views.calculateRemainingDemand,name="Calculate Remaining Demand Monthly"),
  path('resetFinalCost/',views.resetFC,name="Reset Final Cost")
]