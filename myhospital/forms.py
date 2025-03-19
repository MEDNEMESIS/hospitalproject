from django.forms import ModelForm
from myhospital.models import Patient,Doctor,Diagnosis,Treatment,Payment

class PatientForm(ModelForm):
    class Meta:
        model=Patient
        fields='__all__'
        
#doctor form
class DoctorForm(ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'

        #diagnosis form
class DiagnosisForm(ModelForm):
    class Meta:
        model=Diagnosis
        fields='__all__'

       #treatment form
class TreatmentForm(ModelForm):
    class Meta:
        model=Treatment
        fields='__all__'

           #payment form
class PaymentForm(ModelForm):
    class Meta:
        model=Payment
        fields='__all__'
          