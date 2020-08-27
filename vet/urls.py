from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register, name='register'),
    path('create_admin/<str:pk>/', views.createadmin, name='create_admin'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('addresses/', views.addresses, name='addresses'),
    path('create_address', views.createaddress, name='create_address'),
    path('update_address/<str:pk>/', views.updateaddress, name='update_address'),
    path('delete_address/<str:pk>/', views.deleteaddress, name='delete_address'),

    path('owners/', views.owners, name='owners'),
    path('create_owner/', views.createowner, name='create_owner'),
    path('update_owner/<str:pk>/', views.updateowner, name='update_owner'),
    path('delete_owner/<str:pk>/', views.deleteowner, name='delete_owner'),

    path('medics/', views.medics, name='medics'),
    path('create_medic/', views.createmedic, name='create_medic'),
    path('update_medic/<str:pk>/', views.updatemedic, name='update_medic'),
    path('delete_medic/<str:pk>/', views.deletemedic, name='delete_medic'),

    path('surgeries/', views.surgeries, name='surgeries'),
    path('create_surgery/', views.createsurgery, name='create_surgery'),
    path('update_surgery/<str:pk>/', views.updatesurgery, name='update_surgery'),
    path('delete_surgery/<str:pk>/', views.deletesurgery, name='delete_surgery'),

    path('breeds_species/', views.breeds_species, name='breeds_species'),

    path('create_species/', views.createspecies, name='create_species'),
    path('update_species/<str:pk>/', views.updatespecies, name='update_species'),
    path('delete_species/<str:pk>/', views.deletespecies, name='delete_species'),

    path('create_breed/', views.createbreed, name='create_breed'),
    path('update_breed/<str:pk>/', views.updatebreed, name='update_breed'),
    path('delete_breed/<str:pk>/', views.deletebreed, name='delete_breed'),

    path('medicines/', views.medicines, name='medicines'),
    path('create_medicine/', views.createmedicine, name='create_medicine'),
    path('update_medicine/<str:pk>/',
         views.updatemedicine, name='update_medicine'),
    path('delete_medicine/<str:pk>/',
         views.deletemedicine, name='delete_medicine'),

    path('shifts/', views.shifts, name='shifts'),
    path('create_shift/', views.createshift, name='create_shift'),
    path('update_shift/<str:pk>/', views.updateshift, name='update_shift'),
    path('delete_shift/<str:pk>/', views.deleteshift, name='delete_shift'),

    path('ownerphones/<str:fk>/', views.ownerphones, name='ownerphones'),
    path('create_ownerphone/<str:pk>/',
         views.createownerphone, name='create_ownerphone'),
    path('update_ownerphone/<str:pk>/',
         views.updateownerphone, name='update_ownerphone'),
    path('delete_ownerphone/<str:pk>/',
         views.deleteownerphone, name='delete_ownerphone'),

    path('medicphones/<str:fk>/', views.medicphones, name='medicphones'),
    path('create_medicphone/<str:pk>/',
         views.createmedicphone, name='create_medicphone'),
    path('update_medicphone/<str:pk>/',
         views.updatemedicphone, name='update_medicphone'),
    path('delete_medicphone/<str:pk>/',
         views.deletemedicphone, name='delete_medicphone'),

    path('patients/', views.patients, name='patients'),
    path('create_patient/', views.createpatient, name='create_patient'),
    path('update_patient/<str:pk>/', views.updatepatient, name='update_patient'),
    path('delete_patient/<str:pk>/', views.deletepatient, name='delete_patient'),

    path('appointments/', views.appointments, name='appointments'),
    path('create_appointment/', views.createappointment, name='create_appointment'),
    path('update_appointment/<str:pk>/',
         views.updateappointment, name='update_appointment'),
    path('delete_appointment/<str:pk>/',
         views.deleteappointment, name='delete_appointment'),

    path('disease/', views.disease, name='disease'),
    path('create_disease/', views.createdisease, name='create_disease'),
    path('update_disease/<str:pk>/', views.updatedisease, name='update_disease'),
    path('delete_disease/<str:pk>/', views.deletedisease, name='delete_disease'),

    path('diseases/', views.diseases, name='diseases'),
    path('create_diseases/', views.creatediseases, name='create_diseases'),
    path('update_diseases/<str:pk>/', views.updatediseases, name='update_diseases'),
    path('delete_diseases/<str:pk>/', views.deletediseases, name='delete_diseases'),

    path('workingshifts/', views.workingshifts, name='workingshifts'),
    path('create_workingshift/', views.createworkingshift,
         name='create_workingshift'),
    path('update_workingshift/<str:pk>/',
         views.updateworkingshift, name='update_workingshift'),
     path('delete_workingshift/<str:pk>/',
         views.deleteworkingshift, name='delete_workingshift'),

    path('report/', views.report, name='report'),
]
