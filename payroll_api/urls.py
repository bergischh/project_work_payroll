from django.urls import path

from api.views import user_views
from api.views import calon_karyawan_views
from api.views import departement_views
from api.views import karyawan_views
from api.views import periodGaji_views
from api.views import tunjangan_views
from api.views import pinjamanKaryawan_views
from api.views import laporangaji_views
from api.views import kehadirankaryawan_views
from api.views import slipgaji_views
from api.views import transaksipembayaran_views


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
    path('create-karyawan/', karyawan_views.createKaryawan, name='create-karyawan'),
    path('karyawan-edit/<int:id>/', karyawan_views.editKaryawan, name='edit-karyawan'),
    path('karyawan-all/', karyawan_views.getKaryawan, name='get-karyawan'),
    path('karyawan-delete/<int:id>/', karyawan_views.deleteKaryawan, name='delete-karyawan'),

    # url untuk departement
    path('all-departement/', departement_views.getdepartement, name='get-departement'),
    path('create-departement/', departement_views.createdepartement, name='create-departement'),
    path('edit-departement/<int:id>/', departement_views.editDepartement, name='edit-departement'),
    path('delete-departement/<int:id>/', departement_views.deleteDepartement, name='delete-departement'),

    # url untuk periode penggajian
    path('get-periodegaji/', periodGaji_views.getPeriodeGaji, name='get-periodegaji'),
    path('create-periodegaji/', periodGaji_views.postPeriodeGaji, name='create-periodegaji'),
    path('edit-periodegaji/<int:id>/', periodGaji_views.editPeriodeGaji, name='edit-periodegaji'),
    path('delete-periodegaji/<int:id>/', periodGaji_views.deletePeriodeGaji, name='delete-periodegaji'),

    # url untuk tunjangan karyawan
    path('get-tunjangan/', tunjangan_views.getTunjangan, name='get-tunjangan'),
    path('create-tunjangan/', tunjangan_views.postTunjangan, name='create-tunjangan'),
    path('edit-tunjangan/<int:id>/', tunjangan_views.editTunjangan, name='edit-tunjangan'),
    path('delete-tunjangan/<int:id>/', tunjangan_views.deleteTunjangan, name='delete-tunjangan'),

    # url untuk pinjaman karyawan 
    path('all-pinjaman/', pinjamanKaryawan_views.getPinjamanKaryawan, name='get-pinjaman'),
    path('create-pinjaman/', pinjamanKaryawan_views.postPinjaman, name='create-pinjaman'),
    path('edit-pinjaman/<int:id>/', pinjamanKaryawan_views.updatePinjaman, name='ediit-pinjaman'),
    path('delete-pinjaman/<int:id>/', pinjamanKaryawan_views.deletePinjaman, name='delete-pinnjaman'),

    # url untuk laporan penggajian 
    path('all-laporan-penggajian/', laporangaji_views.getLaporanGaji, name='get-laporan'),
    path('create-laporan-gaji/', laporangaji_views.postLaporanGaji, name='create-laporan'),
    path('edit-laporan-karyawan/<int:id>/', laporangaji_views.updateLaporanGaji, name='edit-laporan'),
    path('delete-laporan-gaji/<int:id>/', laporangaji_views.deleteLaporanGaji, name='delete-laporan'),

    # url untuk kehadiran karyawan 
    path('all-kehadiran-karyawan/', kehadirankaryawan_views.getKehadiranKaryawan, name='get-kehadiran'),
    path('create-kehadiran-karyawan/', kehadirankaryawan_views.postKehadiranKaryawan, name='create-kehadiran-karyawan'),
    path('edit-kehadiran-karyawan/<int:id>/', kehadirankaryawan_views.updateKehadiranKaryawan, name='edit-kehadiran'),
    path('delete-kehadiran-karyawan/<int:id>/', kehadirankaryawan_views.deleteKehadiranKaryawan, name='delete-kehadiran'),

    # url untuk slip gaji
    path('all-slip-gaji/', slipgaji_views.getSlipGaji, name='get-slipgaji'),
    path('create-slip-gaji/', slipgaji_views.postSlipGaji, name='create-slip-gaji'),
    path('edit-slip-gaji/<int:id>/', slipgaji_views.updateTransaksi, name='edit-slip-gaji'),
    path('delete-slip-gaji/<int:id>/', slipgaji_views.deletetransaksi, name='delete-slip-gaji'),
   
    # url untuk transaksi pinjaman
    path('all-transaksi/', transaksipembayaran_views.getTransaksi, name='get-transaksi'),
    path('create-transaksi/', transaksipembayaran_views.postTransaksi, name='create-transaksi'),
    path('edit-transaksi/<int:id>/', transaksipembayaran_views.updateTransaksi, name='create-transaksi'),
    path('delete-transaksi/<int:id>/', transaksipembayaran_views.deletetransaksi, name='delete-transaksi')



]