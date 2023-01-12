from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .import views

urlpatterns = [
    path('', views.index, name="home"),

    # path('worker-signup/',views.worker_signup_view ),
    # path('worker-login/',LoginView.as_view(template_name="main/worker_login.html"),name="worker-login"),

    path('login/', LoginView.as_view(template_name="main/login.html"),
         name="login"),

    path('logout', views.logout_view, name='logout'),
    path('history', views.history, name='history'),
    path('formula', views.formula, name='formula'),
    path('contact',views.contact,name='contact'),
    
    path('viewDetailFour/<plan_Name>/', views.viewDetailFour, name='viewDetailFour'),
    path('deleteDetailFour/<plan_Name>/', views.deleteDetailFour, name='deleteDetailFour'),
    path('downloadFour/<plan_Name>/', views.downloadFour,name='downloadFour'),
    path('demandFour/<plan_Name>/', views.demandFour, name='demandFour'),
    path('numPermanentFour/<plan_Name>/', views.numPermanentFour, name='numPermanentFour'),
    path('prodPermanentFour/<plan_Name>/', views.prodPermanentFour, name='prodPermanentFour'),
    path('prodTemporaryFour/<plan_Name>/', views.prodTemporaryFour, name='prodTemporaryFour'),
    path('costHiringFour/<plan_Name>/', views.costHiringFour, name='costHiringFour'),
    path('costFiringFour/<plan_Name>/', views.costFiringFour, name='costFiringFour'),
    path('costHoldingUnitFour/<plan_Name>/', views.costHoldingUnitFour, name='costHoldingUnitFour'),
    
    path('viewDetailFive/<plan_Name>/', views.viewDetailFive, name='viewDetailFive'),
    path('deleteDetailFive/<plan_Name>/', views.deleteDetailFive, name='deleteDetailFive'),
    path('downloadFive/<plan_Name>/', views.downloadFive,name='downloadFive'),
    path('demandFive/<plan_Name>/', views.demandFive, name='demandFive'),
    path('numPermanentFive/<plan_Name>/', views.numPermanentFive, name='numPermanentFive'),
    path('prodPermanentFive/<plan_Name>/', views.prodPermanentFive, name='prodPermanentFive'),
    path('prodTemporaryFive/<plan_Name>/', views.prodTemporaryFive, name='prodTemporaryFive'),
    path('costHiringFive/<plan_Name>/', views.costHiringFive, name='costHiringFive'),
    path('costFiringFive/<plan_Name>/', views.costFiringFive, name='costFiringFive'),
    path('costHoldingUnitFive/<plan_Name>/', views.costHoldingUnitFive, name='costHoldingUnitFive'),
    
    path('viewDetailSix/<plan_Name>/', views.viewDetailSix, name='viewDetailSix'),
    path('deleteDetailSix/<plan_Name>/', views.deleteDetailSix, name='deleteDetailSix'),
    path('downloadSix/<plan_Name>/', views.downloadSix,name='downloadSix'),
    path('demandSix/<plan_Name>/', views.demandSix, name='demandSix'),
    path('numPermanentSix/<plan_Name>/', views.numPermanentSix, name='numPermanentSix'),
    path('prodPermanentSix/<plan_Name>/', views.prodPermanentSix, name='prodPermanentSix'),
    path('prodTemporarySix/<plan_Name>/', views.prodTemporarySix, name='prodTemporarySix'),
    path('costHiringSix/<plan_Name>/', views.costHiringSix, name='costHiringSix'),
    path('costFiringSix/<plan_Name>/', views.costFiringSix, name='costFiringSix'),
    path('costHoldingUnitSix/<plan_Name>/', views.costHoldingUnitSix, name='costHoldingUnitSix'),
    
    path('viewDetailSeven/<plan_Name>/', views.viewDetailSeven, name='viewDetailSeven'),
    path('deleteDetailSeven/<plan_Name>/', views.deleteDetailSeven, name='deleteDetailSeven'),
    path('downloadSeven/<plan_Name>/', views.downloadSeven,name='downloadSeven'),
    path('demandSeven/<plan_Name>/', views.demandSeven, name='demandSeven'),
    path('numPermanentSeven/<plan_Name>/', views.numPermanentSeven, name='numPermanentSeven'),
    path('prodPermanentSeven/<plan_Name>/', views.prodPermanentSeven, name='prodPermanentSeven'),
    path('prodTemporarySeven/<plan_Name>/', views.prodTemporarySeven, name='prodTemporarySeven'),
    path('costHiringSeven/<plan_Name>/', views.costHiringSeven, name='costHiringSeven'),
    path('costFiringSeven/<plan_Name>/', views.costFiringSeven, name='costFiringSeven'),
    path('costHoldingUnitSeven/<plan_Name>/', views.costHoldingUnitSeven, name='costHoldingUnitSeven'),
    
    path('viewDetailEight/<plan_Name>/', views.viewDetailEight, name='viewDetailEight'),
    path('deleteDetailEight/<plan_Name>/', views.deleteDetailEight, name='deleteDetailEight'),
    path('downloadEight/<plan_Name>/', views.downloadEight,name='downloadEight'),
    path('demandEight/<plan_Name>/', views.demandEight, name='demandEight'),
    path('numPermanentEight/<plan_Name>/', views.numPermanentEight, name='numPermanentEight'),
    path('prodPermanentEight/<plan_Name>/', views.prodPermanentEight, name='prodPermanentEight'),
    path('prodTemporaryEight/<plan_Name>/', views.prodTemporaryEight, name='prodTemporaryEight'),
    path('costHiringEight/<plan_Name>/', views.costHiringEight, name='costHiringEight'),
    path('costFiringEight/<plan_Name>/', views.costFiringEight, name='costFiringEight'),
    path('costHoldingUnitEight/<plan_Name>/', views.costHoldingUnitEight, name='costHoldingUnitEight'),
    
    path('viewDetailNine/<plan_Name>/', views.viewDetailNine, name='viewDetailNine'),
    path('deleteDetailNine/<plan_Name>/', views.deleteDetailNine, name='deleteDetailNine'),
    path('downloadNine/<plan_Name>/', views.downloadNine,name='downloadNine'),
    path('demandNine/<plan_Name>/', views.demandNine, name='demandNine'),
    path('numPermanentNine/<plan_Name>/', views.numPermanentNine, name='numPermanentNine'),
    path('prodPermanentNine/<plan_Name>/', views.prodPermanentNine, name='prodPermanentNine'),
    path('prodTemporaryNine/<plan_Name>/', views.prodTemporaryNine, name='prodTemporaryNine'),
    path('costHiringNine/<plan_Name>/', views.costHiringNine, name='costHiringNine'),
    path('costFiringNine/<plan_Name>/', views.costFiringNine, name='costFiringNine'),
    path('costHoldingUnitNine/<plan_Name>/', views.costHoldingUnitNine, name='costHoldingUnitNine'),
    
    path('viewDetailTen/<plan_Name>/', views.viewDetailTen, name='viewDetailTen'),
    path('deleteDetailTen/<plan_Name>/', views.deleteDetailTen, name='deleteDetailTen'),
    path('downloadTen/<plan_Name>/', views.downloadTen,name='downloadTen'),
    path('demandTen/<plan_Name>/', views.demandTen, name='demandTen'),
    path('numPermanentTen/<plan_Name>/', views.numPermanentTen, name='numPermanentTen'),
    path('prodPermanentTen/<plan_Name>/', views.prodPermanentTen, name='prodPermanentTen'),
    path('prodTemporaryTen/<plan_Name>/', views.prodTemporaryTen, name='prodTemporaryTen'),
    path('costHiringTen/<plan_Name>/', views.costHiringTen, name='costHiringTen'),
    path('costFiringTen/<plan_Name>/', views.costFiringTen, name='costFiringTen'),
    path('costHoldingUnitTen/<plan_Name>/', views.costHoldingUnitTen, name='costHoldingUnitTen'),
    
    path('viewDetailEleven/<plan_Name>/', views.viewDetailEleven, name='viewDetailEleven'),
    path('deleteDetailEleven/<plan_Name>/', views.deleteDetailEleven, name='deleteDetailEleven'),
    path('downloadEleven/<plan_Name>/', views.downloadEleven,name='downloadEleven'),
    path('demandEleven/<plan_Name>/', views.demandEleven, name='demandEleven'),
    path('numPermanentEleven/<plan_Name>/', views.numPermanentEleven, name='numPermanentEleven'),
    path('prodPermanentEleven/<plan_Name>/', views.prodPermanentEleven, name='prodPermanentEleven'),
    path('prodTemporaryEleven/<plan_Name>/', views.prodTemporaryEleven, name='prodTemporaryEleven'),
    path('costHiringEleven/<plan_Name>/', views.costHiringEleven, name='costHiringEleven'),
    path('costFiringEleven/<plan_Name>/', views.costFiringEleven, name='costFiringEleven'),
    path('costHoldingUnitEleven/<plan_Name>/', views.costHoldingUnitEleven, name='costHoldingUnitEleven'),
    
    path('viewDetailTwelve/<plan_Name>/', views.viewDetailTwelve, name='viewDetailTwelve'),
    path('deleteDetailTwelve/<plan_Name>/', views.deleteDetailTwelve, name='deleteDetailTwelve'),
    path('downloadTwelve/<plan_Name>/', views.downloadTwelve,name='downloadTwelve'),
    path('demandTwelve/<plan_Name>/', views.demandTwelve, name='demandTwelve'),
    path('numPermanentTwelve/<plan_Name>/', views.numPermanentTwelve, name='numPermanentTwelve'),
    path('prodPermanentTwelve/<plan_Name>/', views.prodPermanentTwelve, name='prodPermanentTwelve'),
    path('prodTemporaryTwelve/<plan_Name>/', views.prodTemporaryTwelve, name='prodTemporaryTwelve'),
    path('costHiringTwelve/<plan_Name>/', views.costHiringTwelve, name='costHiringTwelve'),
    path('costFiringTwelve/<plan_Name>/', views.costFiringTwelve, name='costFiringTwelve'),
    path('costHoldingUnitTwelve/<plan_Name>/', views.costHoldingUnitTwelve, name='costHoldingUnitTwelve')
]
