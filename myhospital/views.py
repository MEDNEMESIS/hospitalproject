from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
#importing logout from django
from django.contrib.auth import logout
from django.contrib import messages




from myhospital.forms import PatientForm,DoctorForm,DiagnosisForm,TreatmentForm,PaymentForm
from  myhospital.models import Patient,Doctor,Diagnosis,Treatment,Payment


@login_required
def index_View(request):
    return render (request,'index.html')


def custom_logout_view(request):
    logout(request)
    return redirect('index.html')




@login_required
def add_patient_view(request):
    message=''
    if request.method=="POST":
        patient_Form=PatientForm(request.POST)
        if patient_Form.is_valid():
            patient_Form.save()
            messages.success(request,"Patient Added Succesfully")
            patient_Form=PatientForm()
    else:
        patient_Form=PatientForm()

    patients=Patient.objects.all

        
            
    context={
            'form':patient_Form,
            'message':message,
            'patients':patients
        }

    return render(request,'add_patient.html',context)




def edit_patient_view(request,patient_id):
    message=''
    patient=Patient.objects.get(id=patient_id)
    if request.method=="POST":
        patient_Form=PatientForm(request.POST,instance=patient)
        if patient_Form.is_valid():
            patient_Form.save()
            messages.success(request,"changes Added Succesfully")
            return redirect(add_patient_view)
        else:
            message="Invalid Form"
    else:
        patient_Form=PatientForm(instance=patient)

        
    context={
            'form':patient_Form,
            'message':message,
            'patient':patient
        }

    return render(request,'edit_patient.html',context)




def delete_patient_view(request,patient_id):
    
    patient=Patient.objects.get(id=patient_id)
    patient.delete()

    return redirect(add_patient_view) 
#doctor view

@login_required
def add_doctor_view(request):
    message='' 
    if request.method=="POST":
        doctor_Form=DoctorForm(request.POST)
        if doctor_Form.is_valid():
            doctor_Form.save()
            messages.success(request,"Doctor Added Succesfully")
            doctor_Form=DoctorForm()
    else:
        doctor_Form=DoctorForm()

    doctors=Doctor.objects.all

        
            
    context={
            'form':doctor_Form,
            'message':message,
            'doctors':doctors
        }

    return render(request,'add_doctor.html',context)




def edit_doctor_view(request,doctor_id):
    message=''
    doctor=Doctor.objects.get(id=doctor_id)
    if request.method=="POST":
        doctor_Form=DoctorForm(request.POST,instance=doctor)
        if doctor_Form.is_valid():
            doctor_Form.save()
            message="changes Added Succesfully"
            return redirect(add_doctor_view)
        else:
            message="Invalid Form"
    else:
        doctor_Form=DoctorForm(instance=doctor)

        
    context={
            'form':doctor_Form,
            'message':message,
            'doctor':doctor
        }

    return render(request,'edit_doctor.html',context)




def delete_doctor_view(request,doctor_id):
    
    doctor=Doctor.objects.get(id=doctor_id)
    doctor.delete()

    return redirect(add_doctor_view) 

#diagnosis view

@login_required
def add_diagnosis_view(request):
    message='' 
    if request.method=="POST":
        diagnosis_Form=DiagnosisForm(request.POST)
        if diagnosis_Form.is_valid():
            diagnosis_Form.save()
          
            messages.success(request,"Diagnosis Added Succesfully")
            diagnosis_Form=DiagnosisForm()
    else:
        diagnosis_Form=DiagnosisForm()

    diagnosiss=Diagnosis.objects.all

        
            
    context={
            'form':diagnosis_Form,
            'message':message,
            'diagnosiss':diagnosiss
        }

    return render(request,'add_diagnosis.html',context)



@login_required
def edit_diagnosis_view(request,diagnosis_id):
    message=''
    diagnosis=Diagnosis.objects.get(id=diagnosis_id)
    if request.method=="POST":
        diagnosis_Form=DiagnosisForm(request.POST,instance=diagnosis)
        if diagnosis_Form.is_valid():
            diagnosis_Form.save()
        
            messages.success(request,"diagnosis edited Succesfully")
            return redirect(add_diagnosis_view)
        else:
            message="Invalid Form"
    else:
        diagnosis_Form=DiagnosisForm(instance=diagnosis)

        
    context={
            'form':diagnosis_Form,
            'message':message,
            'doctor':diagnosis
        }

    return render(request,'edit_diagnosis.html',context)




def delete_diagnosis_view(request,diagnosis_id):
    
    diagnosis=Diagnosis.objects.get(id=diagnosis_id)
    diagnosis.delete()

    return redirect(add_diagnosis_view) 






#treatment view

@login_required
def add_treatment_view(request):
    message='' 
    if request.method=="POST":
        treatment_Form=TreatmentForm(request.POST)
        if treatment_Form.is_valid():
            treatment_Form.save()
     
            messages.success(request,"Treatment Added Succesfully")
            treatment_Form=TreatmentForm()
            
    else:
        treatment_Form=TreatmentForm()

    treatments=Treatment.objects.all

        
            
    context={
            'form':treatment_Form,
            'message':message,
            'treatments':treatments
        }

    return render(request,'add_treatment.html',context)




def edit_treatment_view(request,treatment_id):
    message=''
    treatment=Treatment.objects.get(id=treatment_id)
    if request.method=="POST":
        treatment_Form=TreatmentForm(request.POST,instance=treatment)
        if treatment_Form.is_valid():
            treatment_Form.save()
            message="changes Added Succesfully"
            return redirect(add_treatment_view)
        else:
            message="Invalid Form"
    else:
        treatment_Form=TreatmentForm(instance=treatment)

        
    context={
            'form':treatment_Form,
            'message':message,
            'treatment':treatment
        }

    return render(request,'edit_treatment.html',context)




def delete_treatment_view(request,treatment_id):
    
    treatment=Treatment.objects.get(id=treatment_id)
    treatment.delete()

    return redirect(add_treatment_view) 




#PAYMENT view
@login_required
def add_payment_view(request):
    message='' 
    if request.method=="POST":
        payment_Form=PaymentForm(request.POST)
        if payment_Form.is_valid():
            payment_Form.save()
           
            messages.success(request,"Payment Added Succesfully")
            payment_Form=PaymentForm()


    else:
        payment_Form=PaymentForm()

    payments=Payment.objects.all

        
            
    context={
            'form':payment_Form,
            'message':message,
            'payments':payments
        }

    return render(request,'add_payment.html',context)




def edit_payment_view(request,payment_id):
    message=''
    payment=Payment.objects.get(id=payment_id)
    if request.method=="POST":
        payment_Form=PaymentForm(request.POST,instance=payment)
        if payment_Form.is_valid():
            payment_Form.save()
            message="changes Added Succesfully"
            return redirect(add_payment_view)
        else:
            message="Invalid Form"
    else:
        payment_Form=PaymentForm(instance=payment)

        
    context={
            'form':payment_Form,
            'message':message,
            'payment':payment
        }

    return render(request,'edit_payment.html',context)




def delete_payment_view(request,payment_id):
    
    
    payment=Payment.objects.get(id=payment_id)
    payment.delete()

    return redirect(add_payment_view) 


def sign_up_view(request):
    if request.method=="POST":
        signup_form=UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            message="user created successfully"
            
    
        else:
               message="something went wrong"
           
    else:
        signup_form=UserCreationForm()
     

    context={
            'form':signup_form
            
        }
    return render(request,'registration/signup.html',context)





