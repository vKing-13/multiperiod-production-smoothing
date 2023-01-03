from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .import views

urlpatterns = [
    path('', views.index, name="home"),

    # path('worker-signup/',views.worker_signup_view ),
    # path('worker-login/',LoginView.as_view(template_name="main/worker_login.html"),name="worker-login"),

    path('boss-signup/', views.boss_signup_view),
    path('boss-login/', LoginView.as_view(template_name="main/boss_login.html"),
         name="boss-login"),

    path('logout', views.logout_view, name='logout'),

    path('admin-login/', LoginView.as_view(template_name="main/admin_login.html"),
         name="admin-login"),
    path('admin_view_user/', views.admin_view_user_view, name="admin_view_user"),
    # path('delete-boss/<int:pk>', views.delete_boss_view,name='delete-boss'),
    # path('delete-worker/<int:pk>', views.delete_worker_view,name='delete-worker'),


    # # path('calculateFC/',views.calculateFinalCost,name="Calculate Final Cost"),
    # path('calculateFHC/',views.calculateFiringHiringCost,name="Calculate Firing and Hiring Cost"),
    # path('calculateIC/',views.calculateInventoryConstraints,name="Calculate Monthly Inventory Constraints"),
    # path('calculateIHC/',views.calculateInventoryHoldingCost,name="Calculate Inventory Holding Cost"),
    # # path('calculateNTW/',views.calculateNumOfTempWorkers,name="Calculate Num. of Temp. Workers Monthly"),
    # path('calculateRD/',views.calculateRemainingDemand,name="Calculate Remaining Demand Monthly"),
    # path('resetFinalCost/',views.resetFC,name="Reset Final Cost")
]
