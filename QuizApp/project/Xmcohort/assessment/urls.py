from django.urls import path
from .import views

urlpatterns = [
   
    path('cratequestion/',views.createquestion,name='cratequestion'),
    path('home/',views.home,name='home'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('addcandidate/',views.addcandidate,name='addcandi'),
]