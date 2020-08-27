from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class AdministratorForm(ModelForm):
    class Meta:
        model = Administrator
        fields = '__all__'
        exclude = ['user']


class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'


class MedicForm(ModelForm):
    class Meta:
        model = Medic
        fields = '__all__'
        widgets = {
            'admission': forms.DateInput(attrs={'type': 'date'}, format="%Y-%m-%d"),
        }


class SurgeryForm(ModelForm):
    class Meta:
        model = Surgery
        fields = '__all__'
        widgets = {
            #'duration': forms.DurationInput(),
            'description': forms.Textarea()
        }


class SpeciesForm(ModelForm):
    class Meta:
        model = Species
        fields = '__all__'


class BreedForm(ModelForm):
    class Meta:
        model = Breed
        fields = '__all__'


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'


class ShiftForm(ModelForm):
    class Meta:
        model = Shift
        fields = '__all__'
        widgets = {
            'start': forms.TimeInput(attrs={'type': 'time'}),
            'end': forms.TimeInput(attrs={'type': 'time'}),
        }


class MedicCellPhoneForm(ModelForm):
    class Meta:
        model = Medic_CellPhone
        fields = '__all__'


class OwnerCellPhoneForm(ModelForm):
    class Meta:
        model = Owner_CellPhone
        fields = '__all__'


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'date_first_attended': forms.DateInput(attrs={'type': 'date'}, format="%Y-%m-%d"),
        }


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}, format="%Y-%m-%d"),
            'booked': forms.DateInput(attrs={'type': 'date'}, format="%Y-%m-%d"),
            'description': forms.Textarea(),
        }


class DiseaseForm(ModelForm):
    class Meta:
        model = Disease
        fields = '__all__'


class DiseasesForm(ModelForm):
    class Meta:
        model = Diseases
        fields = '__all__'


class WorkingShiftForm(ModelForm):
    class Meta:
        model = WorkingShift
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}, format="%Y-%m-%d"),
        }
