from django.db import models


class Patient(models.Model):
    GENDER_OPTIONS = [
        ('M', 'male'),
        ('F', 'female'),
    ]

    BLOOD_OPTIONS = [
        ('O','O'),
        ('A','A'),
        ('B','B'),
        ('B+','B+'),
        ('A+','A+'),
        
    ]
    
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now_add=True) 
    gender = models.CharField(choices=GENDER_OPTIONS, max_length=1, default='M')
    address = models.CharField(max_length=50)
    weight = models.IntegerField(default=0)
    blood_type = models.CharField(choices=BLOOD_OPTIONS,max_length=2,default='0')
    next_of_kin = models.CharField(max_length=50)
    kin_contact = models.CharField(max_length=12)
    age = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.gender})"


class Doctor(models.Model):
    GENDER_OPTIONS = [
        ('M', 'male'),
        ('F', 'female'),
    ]

    name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER_OPTIONS, max_length=1, default='M')
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=12)
    designation = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"


class Diagnosis(models.Model): 
    diagnosis_date = models.DateField(auto_now_add=True)  
    temperature = models.CharField(max_length=20)
    blood_pressure = models.CharField(max_length=20, default='120/80')
    disease = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,default=1)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"{self.disease} (Patient: {self.patient.name}, Doctor: {self.doctor.name})"


class Treatment(models.Model):
    STATUS_OPTIONS = [
        ('C', 'CLEARED'),
        ('U', 'UNPAID'),
    ]

    treatment_date = models.DateField(auto_now_add=True)  
    name = models.CharField(max_length=50, default='General Treatment')
    prescription = models.TextField(max_length=100)
    recommendations = models.CharField(max_length=40)
    amount_to_be_paid = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS_OPTIONS, max_length=1, null=True, default='U')
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"{self.name} - {self.diagnosis.disease}"


class Payment(models.Model):

    METHOD_OPTIONS = [
        ('CASH', 'CASH'),
        ('CREDIT CARD', 'CREDIT CARD'),
        ('MASTER CARD', 'MASTER CARD'),
        ('PAY PAL', 'PAY PAL'),
        ('MOBILE MONEY', 'MOBILE MONEY'),
        ('BANK TRANSFER', 'BANK TRANSFER'),

    ]
    payment_date = models.DateField(auto_now_add=True) 
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE,default=1)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,default=1) 
    amount_paid = models.IntegerField(default=0)
    received_by = models.CharField(max_length=50)
    payment_method = models.CharField(choices=METHOD_OPTIONS,max_length=50,default='CASH')

    def __str__(self):
        return f"Payment for {self.treatment.name} on {self.payment_date} via {self.payment_method} for {self.patient.name}"