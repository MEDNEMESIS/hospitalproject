"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include
from myhospital.views import add_patient_view,edit_patient_view,delete_patient_view,add_doctor_view,edit_doctor_view,delete_doctor_view,add_diagnosis_view,edit_diagnosis_view,delete_diagnosis_view,add_treatment_view,edit_treatment_view,delete_treatment_view,add_payment_view,edit_payment_view,delete_payment_view,sign_up_view,index_View,custom_logout_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_View, name='index_page'),
    

    path('signup_list/', sign_up_view, name='signup_page'),
    path("logout/",custom_logout_view, name="logout"),
   

    


    
    path('accounts/',include('django.contrib.auth.urls')),
    path('add_patient/',add_patient_view,name='add_patient_page'),
    path('edit_patient/<int:patient_id>/',edit_patient_view,name='edit_patient_page'),
    path('delete_patient/<int:patient_id>/',delete_patient_view,name='delete_patient_page'),
    #doctor
    path('add_doctor/',add_doctor_view,name='add_doctor_page'),
    path('edit_doctor/<int:doctor_id>/',edit_doctor_view,name='edit_doctor_page'),
    path('delete_doctor/<int:doctor_id>/',delete_doctor_view,name='delete_doctor_page'),
    #diagnosis
    path('add_diagnosis/',add_diagnosis_view,name='add_diagnosis_page'),
    path('edit_diagnosis/<int:diagnosis_id>/',edit_diagnosis_view,name='edit_diagnosis_page'),
    path('delete_diagnosis/<int:diagnosis_id>/',delete_diagnosis_view,name='delete_diagnosis_page'),

     #Treatment
    path('add_treatment/',add_treatment_view,name='add_treatment_page'),
    path('edit_treatment/<int:treatment_id>/',edit_treatment_view,name='edit_treatment_page'),
    path('delete_treatment/<int:treatment_id>/',delete_treatment_view,name='delete_treatment_page'),
        #PAYMENT
    path('add_payment/',add_payment_view,name='add_payment_page'),
    path('edit_payment/<int:payment_id>/',edit_payment_view,name='edit_payment_page'),
    path('delete_payment/<int:payment_id>/',delete_payment_view,name='delete_payment_page'),

]


