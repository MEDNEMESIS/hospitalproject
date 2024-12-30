from django.contrib import admin
from .models import Patient, Doctor, Diagnosis, Treatment, Payment

class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('diagnosis_date', 'temperature', 'blood_pressure', 'disease', 'patient', 'doctor')

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'address', 'contact', 'designation')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'address', 'age', 'weight', 'blood_type')

class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('treatment_date', 'name', 'amount_to_be_paid', 'status', 'diagnosis')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_date', 'treatment', 'patient', 'amount_paid', 'received_by')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Diagnosis, DiagnosisAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Payment, PaymentAdmin)