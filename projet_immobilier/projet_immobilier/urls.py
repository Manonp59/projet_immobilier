"""projet_immobilier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from prediction import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil/',views.accueil,name="accueil"), 
    path('login/', views.login_page,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('signup/',views.signup,name='signup'),
    path('estimation/',views.estimation,name='estimation'), 
    path('mes-estimations/',views.liste_estimations, name='mes-estimations'),
    path('mon-compte/',views.user_detail,name='mon-compte'),
    path('modifier-compte/',views.modifier_compte,name='modifier-compte'),
    path('estimation-details/<int:id>/', views.estimation_details, name='estimation-details'),
    path('modifier-estimation/<int:id>/',views.modifier_estimation,name='modifier-estimation')
]
