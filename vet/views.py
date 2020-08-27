from django.shortcuts import redirect, render
from django.forms import inlineformset_factory

from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.forms import formset_factory

from django.contrib import messages
import datetime

from .decorators import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import *


@unauthenticated_user
def register(request):
    form = createUserForm()
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='sysdba')
            user.groups.add(group)
            admin = Administrator.objects.create(
                user=user,
            )
            return redirect('/create_admin/{}/'.format(str(admin.id)))

    context = {'form': form, }
    return render(request, 'vet/register_form.html', context)


@unauthenticated_user
def createadmin(request, pk):
    admin = Administrator.objects.get(id=pk)
    form = AdministratorForm(instance=admin)
    if request.method == 'POST':
        form = AdministratorForm(request.POST, instance=admin)
        if form.is_valid():
            form.save()
            return redirect('/login')

    context = {'form': form,}
    return render(request, 'vet/admin_form.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'vet/login_form.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def home(request):

    return render(request, 'vet/dashboard.html', )

@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def addresses(request):
    addresses = Address.objects.all()
    context = {'addresses': addresses}
    return render(request, 'vet/addresses.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def createaddress(request):
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/addresses')

    context = {'form': form, }
    return render(request, 'vet/address_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def updateaddress(request, pk):
    address = Address.objects.get(id=pk)
    form = AddressForm(instance=address)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('/addresses')

    context = {'form': form, }
    return render(request, 'vet/address_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def deleteaddress(request, pk):
    address = Address.objects.get(id=pk)
    if request.method == 'POST':
        address.delete()
        return redirect('/addresses')

    context = {'item': address}
    return render(request, 'vet/delete_address.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def owners(request):
    owners = Owner.objects.all()
    context = {'owners': owners}
    return render(request, 'vet/owners.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def createowner(request):
    form = OwnerForm()
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/owners')

    context = {'form': form, 'tbl': 'owner'}
    return render(request, 'vet/people_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def updateowner(request, pk):
    owner = Owner.objects.get(id=pk)
    form = OwnerForm(instance=owner)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('/owners')

    context = {'form': form, 'tbl': 'owner'}
    return render(request, 'vet/people_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def deleteowner(request, pk):
    owner = Owner.objects.get(id=pk)
    if request.method == 'POST':
        owner.delete()
        return redirect('/owners')

    context = {'item': owner, 'tbl': 'owner'}
    return render(request, 'vet/delete_people.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def medics(request):
    medics = Medic.objects.all()
    context = {'medics': medics}
    return render(request, 'vet/medics.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def createmedic(request):
    form = MedicForm()
    if request.method == 'POST':
        form = MedicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/medics')

    context = {'form': form, 'tbl': 'medic'}
    return render(request, 'vet/people_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def updatemedic(request, pk):
    medic = Medic.objects.get(id=pk)
    form = MedicForm(instance=medic)
    if request.method == 'POST':
        form = MedicForm(request.POST, instance=medic)
        if form.is_valid():
            form.save()
            return redirect('/medics')

    context = {'form': form, 'tbl': 'medic'}
    return render(request, 'vet/people_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def deletemedic(request, pk):
    medic = Medic.objects.get(id=pk)
    if request.method == 'POST':
        medic.delete()
        return redirect('/medics')

    context = {'item': medic, 'tbl': 'medic'}
    return render(request, 'vet/delete_people.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def surgeries(request):
    surgeries = Surgery.objects.all()
    context = {'surgeries': surgeries}
    return render(request, 'vet/surgeries.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def createsurgery(request):
    form = SurgeryForm()
    if request.method == 'POST':
        form = SurgeryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/surgeries')

    context = {'form': form}
    return render(request, 'vet/surgery_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def updatesurgery(request, pk):
    surgery = Surgery.objects.get(id=pk)
    form = SurgeryForm(instance=surgery)
    if request.method == 'POST':
        form = SurgeryForm(request.POST, instance=surgery)
        if form.is_valid():
            form.save()
            return redirect('/surgeries')

    context = {'form': form}
    return render(request, 'vet/surgery_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def deletesurgery(request, pk):
    surgery = Surgery.objects.get(id=pk)
    if request.method == 'POST':
        surgery.delete()
        return redirect('/surgeries')

    context = {'item': surgery}
    return render(request, 'vet/delete_surgery.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def breeds_species(request):
    breeds = Breed.objects.all()
    species = Species.objects.all()
    context = {'breeds': breeds, 'species': species}
    return render(request, 'vet/breeds_species.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def createbreed(request):
    form = BreedForm()
    if request.method == 'POST':
        form = BreedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/breeds_species')
    context = {'form': form}
    return render(request, 'vet/breed_species_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def updatebreed(request, pk):
    breed = Breed.objects.get(id=pk)
    form = BreedForm(instance=breed)
    if request.method == 'POST':
        form = BreedForm(request.POST, instance=breed)
        if form.is_valid():
            form.save()
            return redirect('/breeds_species')

    context = {'form': form}
    return render(request, 'vet/breed_species_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def deletebreed(request, pk):
    breed = Breed.objects.get(id=pk)
    if request.method == 'POST':
        breed.delete()
        return redirect('/breeds_species')

    context = {'item': breed}
    return render(request, 'vet/delete_breed_species.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def createspecies(request):
    form = SpeciesForm()
    if request.method == 'POST':
        form = SpeciesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/breeds_species')
    context = {'form': form, 'species': True}
    return render(request, 'vet/breed_species_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def updatespecies(request, pk):
    species = Species.objects.get(id=pk)
    form = SpeciesForm(instance=species)
    if request.method == 'POST':
        form = SpeciesForm(request.POST, instance=species)
        if form.is_valid():
            form.save()
            return redirect('/breeds_species')
    context = {'form': form, 'species': True}
    return render(request, 'vet/breed_species_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def deletespecies(request, pk):
    species = Species.objects.get(id=pk)
    if request.method == 'POST':
        species.delete()
        return redirect('/breeds_species')

    context = {'item': species, 'species': True}
    return render(request, 'vet/delete_breed_species.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def medicines(request):
    medicines = Medicine.objects.all()
    context = {'medicines': medicines}
    return render(request, 'vet/medicines.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def createmedicine(request):
    form = MedicineForm()
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/medicines')

    context = {'form': form}
    return render(request, 'vet/medicine_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def updatemedicine(request, pk):
    medicine = Medicine.objects.get(id=pk)
    form = MedicineForm(instance=medicine)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('/medicines')

    context = {'form': form}
    return render(request, 'vet/medicine_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def deletemedicine(request, pk):
    medicine = Medicine.objects.get(id=pk)
    if request.method == 'POST':
        medicine.delete()
        return redirect('/medicines')

    context = {'item': medicine}
    return render(request, 'vet/delete_medicine.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def shifts(request):
    shifts = Shift.objects.all()
    context = {'shifts': shifts}
    return render(request, 'vet/shifts.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def createshift(request):
    form = ShiftForm()
    if request.method == 'POST':
        form = ShiftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/shifts')

    context = {'form': form}
    return render(request, 'vet/shift_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def updateshift(request, pk):
    shift = Shift.objects.get(id=pk)
    form = ShiftForm(instance=shift)
    if request.method == 'POST':
        form = ShiftForm(request.POST, instance=shift)
        if form.is_valid():
            form.save()
            return redirect('/shifts')

    context = {'form': form}
    return render(request, 'vet/shift_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def deleteshift(request, pk):
    shift = Shift.objects.get(id=pk)
    if request.method == 'POST':
        shift.delete()
        return redirect('/shifts')

    context = {'item': shift}
    return render(request, 'vet/delete_shift.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def ownerphones(request, fk):
    cellphones = Owner_CellPhone.objects.filter(owner__id=fk)
    quantity = cellphones.count()

    context = {'cellphones': cellphones,
               'q': quantity, 'pk': fk, 'owner': True}
    return render(request, 'vet/cellphones.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def createownerphone(request, pk):
    cellphones = Owner_CellPhone.objects.filter(owner__id=pk)
    quantity = cellphones.count()

    CellFormSet = inlineformset_factory(
        Owner, Owner_CellPhone, fields=('cellphone',), extra=2-quantity)

    owner = Owner.objects.get(id=pk)
    formset = CellFormSet(
        queryset=Owner_CellPhone.objects.none(), instance=owner)
    if request.method == 'POST':
        form = OwnerCellPhoneForm(request.POST)
        formset = CellFormSet(request.POST, instance=owner)
        if formset.is_valid():
            formset.save()
            return redirect('/owners')

    context = {'form': formset, 'owner': True}
    return render(request, 'vet/cellphone_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def updateownerphone(request, pk):
    cellphone = Owner_CellPhone.objects.get(cellphone=pk)
    form = OwnerCellPhoneForm(instance=cellphone)
    if request.method == 'POST':
        cellphone.delete()
        form = OwnerCellPhoneForm(request.POST, instance=cellphone)
        if form.is_valid():
            form.save()
            return redirect('/owners')

    context = {'form': form, 'owner': True}
    return render(request, 'vet/cellphone_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def deleteownerphone(request, pk):
    cellphone = Owner_CellPhone.objects.get(cellphone=pk)
    if request.method == 'POST':
        cellphone.delete()
        return redirect('/owners')

    context = {'item': cellphone, 'owner': True}
    return render(request, 'vet/delete_cellphone.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def medicphones(request, fk):
    cellphones = Medic_CellPhone.objects.filter(medic__id=fk)
    quantity = cellphones.count()

    context = {'cellphones': cellphones,
               'q': quantity, 'pk': fk, 'medic': True}
    return render(request, 'vet/cellphones.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def createmedicphone(request, pk):
    cellphones = Medic_CellPhone.objects.filter(medic__id=pk)
    quantity = cellphones.count()

    CellFormSet = inlineformset_factory(
        Medic, Medic_CellPhone, fields=('cellphone',), extra=2-quantity)

    medic = Medic.objects.get(id=pk)
    formset = CellFormSet(
        queryset=Medic_CellPhone.objects.none(), instance=medic)
    if request.method == 'POST':
        form = MedicCellPhoneForm(request.POST)
        formset = CellFormSet(request.POST, instance=medic)
        if formset.is_valid():
            formset.save()
            return redirect('/medics')

    context = {'form': formset, 'medic': True}
    return render(request, 'vet/cellphone_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def updatemedicphone(request, pk):
    cellphone = Medic_CellPhone.objects.get(cellphone=pk)
    form = MedicCellPhoneForm(instance=cellphone)
    if request.method == 'POST':
        cellphone.delete()
        form = MedicCellPhoneForm(request.POST, instance=cellphone)
        if form.is_valid():
            form.save()
            return redirect('/medics')

    context = {'form': form, 'medic': True}
    return render(request, 'vet/cellphone_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def deletemedicphone(request, pk):
    cellphone = Medic_CellPhone.objects.get(cellphone=pk)
    if request.method == 'POST':
        cellphone.delete()
        return redirect('/medics')

    context = {'item': cellphone, 'medic': True}
    return render(request, 'vet/delete_cellphone.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def patients(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'vet/patients.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def createpatient(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/patients')

    context = {'form': form}
    return render(request, 'vet/patient_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def updatepatient(request, pk):
    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient)
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('/patients')
    context = {'form': form}
    return render(request, 'vet/patient_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def deletepatient(request, pk):
    patient = Patient.objects.get(id=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('/patients')
    context = {'item': patient}
    return render(request, 'vet/delete_patient.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def appointments(request):
    appointments = Appointment.objects.all()
    context = {'appointments': appointments}
    return render(request, 'vet/appointments.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def createappointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/appointments')

    context = {'form': form}
    return render(request, 'vet/appointment_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def updateappointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    form = AppointmentForm(instance=appointment)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('/appointments')

    context = {'form': form}
    return render(request, 'vet/appointment_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def deleteappointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('/appointments')

    context = {'item': appointment}
    return render(request, 'vet/delete_appointment.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def disease(request):
    diseases = Disease.objects.all()
    context = {'diseases': diseases}
    return render(request, 'vet/disease.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def createdisease(request):
    form = DiseaseForm()
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/disease')

    context = {'form': form}
    return render(request, 'vet/disease_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def updatedisease(request, pk):
    disease = Disease.objects.get(id=pk)
    form = DiseaseForm(instance=disease)
    if request.method == 'POST':
        form = DiseaseForm(request.POST, instance=disease)
        if form.is_valid():
            form.save()
            return redirect('/disease')
    context = {'form': form}
    return render(request, 'vet/disease_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def deletedisease(request, pk):
    disease = Disease.objects.get(id=pk)
    if request.method == 'POST':
        disease.delete()
        return redirect('/disease')
    context = {'item': disease}
    return render(request, 'vet/delete_disease.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def diseases(request):
    diseases = Diseases.objects.all()
    context = {'diseases': diseases}
    return render(request, 'vet/diseases.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def creatediseases(request):
    form = DiseasesForm()
    if request.method == 'POST':
        form = DiseasesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/diseases')

    context = {'form': form}
    return render(request, 'vet/diseases_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def updatediseases(request, pk):
    disease = Diseases.objects.get(id=pk)
    form = DiseasesForm(instance=disease)
    if request.method == 'POST':
        form = DiseasesForm(request.POST, instance=disease)
        if form.is_valid():
            form.save()
            return redirect('/diseases')
    context = {'form': form}
    return render(request, 'vet/diseases_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def deletediseases(request, pk):
    disease = Diseases.objects.get(id=pk)
    if request.method == 'POST':
        diseases.delete()
        return redirect('/diseases')
    context = {'item': disease}
    return render(request, 'vet/delete_diseases.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def workingshifts(request):
    workingshifts = WorkingShift.objects.all()
    context = {'workingshifts': workingshifts}
    return render(request, 'vet/working_shifts.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def createworkingshift(request):
    form = WorkingShiftForm()
    if request.method == 'POST':
        form = WorkingShiftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/workingshifts')

    context = {'form': form}
    return render(request, 'vet/workingshift_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def updateworkingshift(request, pk):
    workingshift = WorkingShift.objects.get(id=pk)
    form = WorkingShiftForm(instance=workingshift)
    if request.method == 'POST':
        form = WorkingShiftForm(request.POST, instance=workingshift)
        if form.is_valid():
            form.save()
            return redirect('/workingshifts')
    context = {'form': form}
    return render(request, 'vet/workingshift_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def deleteworkingshift(request, pk):
    workingshift = WorkingShift.objects.get(id=pk)
    if request.method == 'POST':
        workingshift.delete()
        return redirect('/workingshifts')
    context = {'item': workingshift}
    return render(request, 'vet/delete_workingshift.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['sysdba'])
def report(request):
    data = Appointment.objects.all().order_by('booked')
    cellphones = Owner_CellPhone.objects.all()
    context = {'data': data, 'phones': cellphones}
    return render(request, 'vet/report.html', context)
