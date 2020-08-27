from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    city = models.CharField(null=False, max_length=20)
    neighborhood = models.CharField(null=True, max_length=20)
    street = models.CharField(null=True, max_length=20)

    def __str__(self):
        return ('{} {} {}'.format(self.city, self.neighborhood, self.street))

    class Meta:
        verbose_name_plural = 'Addresses'


class Administrator(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    first_name = models.CharField(null=False, max_length=20)
    middle_name = models.CharField(null=False, max_length=20)
    last_name = models.CharField(null=False, max_length=20)
    telephone = models.CharField(null=False, max_length=10)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Administrators'

    def __str__(self):
        return ('{} {} {}'.format(self.first_name , self.middle_name , self.last_name))


class Owner(models.Model):
    first_name = models.CharField(null=False, max_length=20)
    middle_name = models.CharField(null=False, max_length=20)
    last_name = models.CharField(null=False, max_length=20)
    telephone = models.CharField(null=False, max_length=10)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Owners'

    def __str__(self):
        return ('{} {} {}'.format(self.first_name , self.middle_name , self.last_name))


class Medic(models.Model):
    first_name = models.CharField(null=False, max_length=20)
    middle_name = models.CharField(null=False, max_length=20)
    last_name = models.CharField(null=False, max_length=20)
    telephone = models.CharField(null=False, max_length=10)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
    emergencies = models.BooleanField()
    admission = models.DateField(auto_now_add=False, null=False)

    class Meta:
        verbose_name_plural = 'Medics'

    def __str__(self):
        return ('{} {} {}'.format(self.first_name , self.middle_name , self.last_name))


class Surgery(models.Model):
    RISKS = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    duration = models.DurationField(null=False)
    description = models.CharField(null=False, max_length=100)
    risk = models.CharField(null=False, max_length=7, choices=RISKS)
    name = models.CharField(null=False, max_length=50, unique=True)
    anesthesia = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Surgeries'

    def __str__(self):
        return self.name


class Species(models.Model):
    name = models.CharField(null=False, max_length=50)
    family = models.CharField(null=False, max_length=50)

    class Meta:
        verbose_name_plural = 'Species'
        unique_together = ['name','family']

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(null=False, max_length=50, unique=True)
    low = models.IntegerField(null = False)
    high = models.IntegerField(null = False)

    class Meta:
        verbose_name_plural = 'Breeds'

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(null=False, max_length=50, unique=True)
    dosage = models.CharField(null=False, max_length=50)
    administration = models.CharField(null=False, max_length=50)

    class Meta:
        verbose_name_plural = 'Medicines'

    def __str__(self):
        return self.name


class Shift(models.Model):
    NAMES = [
        ('Day', 'Day'),
        ('Evening', 'Evening'),
        ('Night', 'Night'),
    ]
    start = models.TimeField(null=False)
    end = models.TimeField(null=False)
    name = models.CharField(null=False, max_length=50, choices=NAMES)

    class Meta:
        verbose_name_plural = 'Shifts'
        unique_together=['start','end','name']

    def __str__(self):
        return self.name


class Owner_CellPhone(models.Model):
    owner = models.ForeignKey(Owner, null=False, on_delete=models.CASCADE)
    cellphone = models.CharField(null=False, max_length=10, primary_key=True)

    class Meta:
        unique_together = ['owner','cellphone']

    def __str__(self):
        return self.cellphone


class Medic_CellPhone(models.Model):
    medic = models.ForeignKey(Medic, null=False, on_delete=models.CASCADE)
    cellphone = models.CharField(null=False, max_length=10, primary_key=True)

    class Meta:
        unique_together = ['medic','cellphone']
        
    def __str__(self):
        return self.cellphone


class Patient(models.Model):
    name = models.CharField(null=False, max_length=20)
    species = models.ForeignKey(Species, null=True, on_delete=models.SET_NULL)
    breed = models.ForeignKey(Breed, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(Owner, null=True, on_delete=models.SET_NULL)
    primary_care_doctor = models.ForeignKey(
        Medic, null=True, on_delete=models.SET_NULL)
    photo = models.ImageField(null=False, blank=True, default='default.png')
    date_first_attended = models.DateField(
        auto_now_add=False, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Patients'

    def __str__(self):
        return (self.name)


class Appointment(models.Model):
    date = models.DateField(auto_now_add=False, null = False)
    patient = models.ForeignKey(Patient, null=False, on_delete=models.CASCADE)
    description = models.CharField(null=False, max_length=50)
    surgery = models.ForeignKey(Surgery, null=True, blank=True, on_delete=models.SET_NULL)
    medic = models.ForeignKey(Medic, null=False, on_delete=models.CASCADE)
    booked = models.DateField(auto_now_add=False, null = False)

    def __str__(self):
        return ('{},{},{}'.format(self.date, self.patient , self.medic))

class Disease(models.Model):
    name = models.CharField(null=False, max_length=20)

    class Meta:
        verbose_name_plural = 'Diseases'

    def __str__(self):
        return self.name

###############################
class Diseases(models.Model):
    breed = models.ForeignKey(Breed, null=False, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, null=False, on_delete=models.CASCADE)
    medication = models.ForeignKey(
        Medicine, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Diseases and Medication'
        unique_together = ['breed','disease','medication']

    def __str__(self):
        return ('{},{},{}'.format(self.breed , self.disease , self.medication))

class WorkingShift(models.Model):
    shift = models.ForeignKey(Shift, null=False, on_delete=models.CASCADE)
    medic = models.ForeignKey(Medic, null=False, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, null=False)

    class Meta:
        verbose_name_plural = 'WorkingShifts'
        unique_together = ['shift','medic','date']

    def __str__(self):
        return ('{},{},{}'.format(self.shift , self.medic , self.date))
###############################

class Audit(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    table = models.CharField(max_length=20)
    op = models.CharField(max_length=1)
    user = models.CharField(max_length=15)
