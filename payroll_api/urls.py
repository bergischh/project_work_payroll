from django.urls import path

from api.views import user_views
from api.views import calon_karyawan_views
from api.views import departement_views
from api.views import karyawan_views
from api.views import periodGaji_views

urlpatterns = [
    # url untuk user
    path('all-users/', user_views.getUsers, name='get-users'),
    path('register/', user_views.register, name='register-users'),
    path('login/', user_views.login, name='login-users'),
    path('user-edit/<int:user_id>/', user_views.updateUser, name='update-users'),
    path('partial-user-edit/<int:user_id>/', user_views.PartialUpdateUser, name='partial_update_user'),
    path('delete-user/<int:user_id>/', user_views.deleteUser, name='delete-users'),

    # url untuk calon karyawan
    path('all-pewawancara/', calon_karyawan_views.getCalonKaryawan, name='get-pewawancara'),
    path('daftar-wawancara/', calon_karyawan_views.createCalonKaryawan, name='create-pewawancara'),
    path('edit-pewawancara/<int:id>/', calon_karyawan_views.editCalonKaryawan, name='edit-pewawancara'),
    path('delete-pewawancara/<int:id>/', calon_karyawan_views.deleteCalonKaryawan, name='delete-pewawancara'),

    # url untuk karyawan
    path('create-karyawan/', karyawan_views.createKaryawan.as_view(), name='create-karyawan'),
    path('karyawan-edit/<int:id>/', karyawan_views.editKaryawan, name='edit-karyawan'),
    path('karyawan-all/', karyawan_views.getKaryawan, name='get-karyawan'),
    path('karyawan-delete/<int:id>/', karyawan_views.deleteKaryawan, name='delete-karyawan'),

    # url untuk departement
    path('all-departement/', departement_views.getdepartement, name='get-departement'),
    path('create-departement/', departement_views.createdepartement, name='create-departement'),
    path('edit-depatement/<int:id>/', departement_views.editDepartement, name='edit-departement'),
    path('delete-departement/<int:id>/', departement_views.deleteDepartement, name='delete-departement'),

    # url untuk periode penggajian
    path('get-periodegaji/', periodGaji_views.getPeriodeGaji, name='get-periodegaji'),
    path('create-periodegaji/', periodGaji_views.postPeriodeGaji, name='create-periodegaji'),
    path('edit-periodegaji/<int:id>/', periodGaji_views.editPeriodeGaji, name='edit-periodegaji'),
    path('delete-periodegaji/<int:id>/', periodGaji_views.deletePeriodeGaji, name='delete-periodegaji')



]