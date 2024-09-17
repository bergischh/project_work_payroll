from rest_framework import serializers
from django.utils import timezone
from .models.user_models import Users
from .models.calonkaryawan_models import CalonKaryawan
from .models.departement_models import Departement
from .models.karyawan_models import Karyawan
from .models.periodGaji_models import periodePenggajian
from .models.tunjangan_models import tunjanganKaryawan
from .models.pinjamankaryawan_models import PinjamanKaryawan
from .models.laporanpenggajian_models import LaporanPenggajian
from .models.kehadirankaryawan_models import KehadiranKaryawan
from .models.slipgaji_models import SlipGaji
from .models.transaksi_pembayaran_pinjaman import TransaksiPinjaman

class UsersSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Users
        fields = [
            "user_id",
            "username",
            "role", 
            "email",
            "password",
        ]
    
    def create(self, validated_data):
        user = Users(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data.get('role', Users.Role.CALON_KARYAWAN)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validate_data) :
        instance.username = validate_data.get('username', instance.username)
        instance.email = validate_data.get('email', instance.email)
        instance.role = validate_data.get('role', instance.role)
        password = validate_data.get('password')
        if password : 
            instance.set_password(password)
            instance.save()
        return instance
    

        # Serializer Untuk Calon Karyawan 
class CalonKaryawanSerializers(serializers.ModelSerializer) :
    upload_at = serializers.DateTimeField(read_only=True)
    class Meta :
        model = CalonKaryawan
        fields = '__all__'

    def update(self, instance, validate_data) :
        instance.upload_at = timezone.now()
        return super().update(instance, self.validated_data)
    

        # Serializer Untuk Karyawan #
class KaryawanSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Karyawan
        fields = '__all__'

    def create(self, validated_data):
        dataKaryawan = Karyawan(
            role = validated_data.get('role', Users.Role.CALON_KARYAWAN),
            nik = validated_data['nik'],
            nama_karyawan = validated_data['nama_karyawan'],
            tempat_lahir = validated_data['tempat_lahir'],
            tanggal_lahir = validated_data['tanggal_lahir'],
            agama = validated_data['agama'],
            status = validated_data['status'],
            jumlah_anak = validated_data['jumlah_anak'],
            alamat = validated_data['alamat'],
            no_telepon = validated_data['no_telpon'],
            email = validated_data['email'],
            jabatan = validated_data['jabatan'],
            foto = validated_data['foto']

        )

        dataKaryawan.save()

        return super().create(validated_data)

    def update(self, instance, validate_data) :
        instance.role = validate_data.get('role', instance.role)
        instance.nik = validate_data.get('nik', instance.nik)
        instance.nama_karyawan = validate_data('nama_karyawan', instance.nama_karyawan)
        instance.tempat_lahir = validate_data('tempat_lahir', instance.tempat_lahir)
        instance.tanggal_lahir = validate_data('tanggal_lahir', instance.tanggal_lahir)
        instance.agama = validate_data('agama', instance.agama)
        instance.status = validate_data('status', instance.status)
        instance.jumlah_anak = validate_data('jumlah_anak', instance.jumlah_anak)
        instance.alamat = validate_data('alamat', instance.alamat)
        instance.no_telpon = validate_data('no_telpon', instance.no_telpon)
        instance.email = validate_data('email', instance.email)
        instance.jabatan = validate_data('jabatan', instance.jabatan)
        instance.foto = validate_data('foto', instance.foto)

        instance.save()
            
        return instance
    

        # Serializer Untuk Departement #
class DepartementSerializers(serializers.ModelSerializer) :
        class Meta : 
            model = Departement
            fields = [
                'nama_departement'
            ]

        def create(self, validated_data):
            nameDepartment = Departement(
                nama_departement = validated_data['nama_departement']
            )

            nameDepartment.save()

            return super().create(validated_data)

        def update(self, instance, validate_data) :
            instance.nama_departement = validate_data.get('nama_departement', instance.nama_departement)

            instance.save()

            return instance
        

        # Serializer Untuk Periode Penggajian #
class PeriodeGajiSerializers(serializers.ModelSerializer) :
    class Meta : 
        model = periodePenggajian 
        fields = '__all__'
    
    def create(self, validated_data):
        # Jangan gunakan nama kelas sebagai nama variabel
        periode = periodePenggajian(
            start_date=validated_data['start_date'],
            end_date=validated_data['end_date'],
            status_periode=validated_data.get('statusPeriode', periodePenggajian.Status.non_active)
        )

        periode.save()

        return periode
    
    def update(self, instance, validated_data):
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.status_periode = validated_data.get('status_periode', instance.status_periode)

        instance.save()

        return super().update(instance, validated_data)
    

        # Serializer Untuk Tunjangan Karyawan #
class tunjanganSerializers(serializers.ModelSerializer) :
    class Meta :
        model = tunjanganKaryawan
        fields = '__all__'

    def create(self, validated_data):
        tunjangan = tunjanganKaryawan(
            tunjangan_makan = validated_data['tunjangan_makan'],
            tunjangan_kesehatan = validated_data['tunjangan_kesehatan'],
            tunjangan_jabatan = validated_data['tunjangan_makan'],
            THR = validated_data['THR'],
            bonus = validated_data['bonus']
        )

        tunjangan.save()

        return super().create(validated_data)

    def update(self, instance, validate_data):
        instance.tunjangan_makan = validate_data.get('tunjangan_makan', instance.tunjangan_makan)
        instance.tunjangan_kesehatan = validate_data.get('tunjangan_kesehatan', instance.tunjangan_kesehatan)
        instance.tunjangan_jabatan = validate_data.get('tunjangan_jabatan', instance.tunjangan_jabatan)
        instance.THR = validate_data.get('THR', instance.THR)
        instance.bonus = validate_data.get('bonus', instance.bonus)
        
        instance.save()  # Jangan lupa untuk menyimpan perubahan ke database.
        
        return instance
    
    
        # Serializer Untuk Pinjaman Karyawan #
class PinjamanKaryawanSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = PinjamanKaryawan
        fields = '__all__'

    def create(self, validated_data):
        pinjaman = PinjamanKaryawan(
            jumlah_pinjaman = validated_data['jumlah_pinjaman'],
            tanggal_pinjaman = validated_data['tanggal_pinjaman'],
            tenggat_pinjaman = validated_data['tenggat_pinjaman']
        )

        pinjaman.save()

        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.jumlah_pinjam = validated_data.get('jumlah_pinjaman', instance.jumlah_pinjaman)
        instance.tanggal_pinjaman = validated_data.get('tanggal_pinjaman', instance.tanggal_pinjaman)
        instance.tenggat_pinjaman = validated_data.get('tenggat_pinjaman', instance.tenggat_pinjaman)

        instance.save()

        return super().update(instance, validated_data)
    
        # Serlizer untuk Laporan Penggajian 
class LaporanPenggajianSerializer(serializers.ModelSerializer) :
    class Meta :
        model = LaporanPenggajian
        fields = '__all__'

    def create(self, validated_data):
        laporan = LaporanPenggajian(
            tanggal_gaji = validated_data['tanggal_gaji'],
            gaji_mentah = validated_data['gaji_mentah'],
            pinjaman = validated_data['pinjaman'],
            gaji_total = validated_data['gaji_total'],
            jumlah_izin = validated_data['jumlah_izin'],
            jumlah_sakit = validated_data['jumlah_sakit']
        )

        laporan.save()

        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        instance.tanggal_gaji =  validated_data.get('tanggal_gaji', instance.tanggal_gaji)
        instance.gaji_mentah = validated_data.get('gaji_mentah', instance.gaji_mentah)
        instance.pinjaman = validated_data.get('pinjaman', instance.pinjaman)
        instance.gaji_total = validated_data.get('gaji_total', instance.gaji_total)
        instance.jumlah_izin = validated_data.get('jumlah_izin', instance.jumlah_izin)
        instance.jumlah_sakit = validated_data.get('jumlah_sakit', instance.jumlah_sakit)

        instance.save()
        
        return super().update(instance, validated_data)
    

        # Serilizer untuk kehaidran karyawan 
class KehadiranKaryawanSerializer(serializers.ModelSerializer) :
    class Meta :
        model = KehadiranKaryawan
        fields = '__all__'

    def create(self, validated_data):
        kehadiran = KehadiranKaryawan(
            tanggal = validated_data['tanggal'],
            informasi_kehadiran = validated_data['informasi_kehadiran'],
            jam_masuk = validated_data['jam_masuk'],
            jam_pulang = validated_data['jam_pulang'],
            total_jam_kerja = validated_data['total_jam_kerja'],
            kehadiran_karyawan = validated_data['kehadiran_karyawan'],
            total_jam_lembur = validated_data['total_jam_lembur'],
            biaya_pengobatan = validated_data['biaya_pengobatan']
        )

        kehadiran.save()

        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.tanggal = validated_data.get('tanggal', instance.tanggal)
        instance.informasi_kehadiran = validated_data.get('informasi_kehadiran', instance.informasi_kehadiran)
        instance.jam_masuk = validated_data.get('jam_masuk', instance.jam_masuk)
        instance.jam_pulang = validated_data.get('jam_pulang', instance.jam_pulang)
        instance.total_jam_kerja = validated_data.get('total_jam_kerja', instance.total_jam_kerja)
        instance.kehadiran_karyawan = validated_data.get('kehadiran_karyawan', instance.kehadiran_karyawan)
        instance.total_jam_lembur = validated_data.get('total_jam_lembur', instance.total_jam_lembur)
        instance.biaya_pengobatan = validated_data.get('biaya_pengobatan', instance.biaya_pengobatan)

        instance.save()

        return super().update(instance, validated_data)
    
    # Serializer untuk Slip Gaji 
class SlipGajiSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = SlipGaji
        fields = '__all__'

    def create(self, validated_data):
        slipgaji = SlipGaji(
            diterima_dari = validated_data['diterima_dari'],
            nominal_gaji = validated_data['nomminal_gaji'],
            terbilang = validated_data['terbilang'],
            untuk_pembayaran = validated_data['untuk_pembayaran']
        )

        slipgaji.save()

        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        instance.diterima_dari = validated_data.get('diterima_dari', instance.diterima_dari)
        instance.nominal_gaji = validated_data.get('nominal_gaji', instance.nominal_gaji)
        instance.terbilang = validated_data.get('terbilang', instance.terbilang)
        instance.untuk_pembayaran = validated_data('untuk_pembayaran', instance.untuk_pembayaran)

        instance.save()

        return super().update(instance, validated_data)
    
    # Serializer untuk Transaksi Pembayaran Pinjaman 
class TransaksiPinjamanSerializers(serializers.ModelSerializer) :
    
    class Meta : 
        model = TransaksiPinjaman
        fields = '__all__'

    def create(self, validated_data):
        pembayaran = TransaksiPinjaman(
            tanggal_pembayaran = validated_data['tanggal_pemabayaran'],
            jumlah_pembayaran = validated_data['jumlah_pembayaran']
        )

        pembayaran.save()

        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        instance.tanggal_pembayaran = validated_data.get('tanggal_pembayaran', instance.tanggal_pembayaran)
        instance.jumlah_pembayaran = validated_data.get('jumlah_pembayaran', instance.jumlah_pembayaran)

        return super().update(instance, validated_data)
        
