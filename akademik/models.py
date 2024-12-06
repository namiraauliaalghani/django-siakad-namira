from django.db import models

class TahunAkademik(models.Model):
    tahun = models.CharField(max_length=9)  # Contoh: "2023/2024"
    semester = models.CharField(max_length=10, choices=[('Ganjil', 'Ganjil'), ('Genap', 'Genap')])

    def __str__(self):
        return f"{self.tahun} - {self.semester}"


class MataKuliah(models.Model):
    nama = models.CharField(max_length=100)
    kode = models.CharField(max_length=20, unique=True)
    prodi = models.CharField(max_length=50)  # Program studi terkait
    sks = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nama} ({self.kode})"


class Jadwal(models.Model):
    dosen = models.CharField(max_length=100)  # Nama dosen, bisa juga pakai ForeignKey ke model Dosen
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE, related_name="jadwal")
    hari = models.CharField(max_length=10, choices=[
        ('Senin', 'Senin'), ('Selasa', 'Selasa'), ('Rabu', 'Rabu'),
        ('Kamis', 'Kamis'), ('Jumat', 'Jumat'), ('Sabtu', 'Sabtu'), ('Minggu', 'Minggu')
    ])
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    ruang = models.CharField(max_length=50)
    kuota_peserta = models.PositiveIntegerField()
    tahun_akademik = models.ForeignKey(TahunAkademik, on_delete=models.CASCADE, related_name="jadwal")

    def __str__(self):
        return f"{self.mata_kuliah.nama} - {self.hari} {self.jam_mulai}-{self.jam_selesai}"


class KRS(models.Model):
    tahun_akademik = models.ForeignKey(TahunAkademik, on_delete=models.CASCADE, related_name="krs")
    mahasiswa = models.CharField(max_length=100)  # Nama mahasiswa, bisa juga pakai ForeignKey ke model Mahasiswa
    jadwal = models.ManyToManyField(Jadwal, related_name="krs")

    def __str__(self):
        return f"KRS {self.mahasiswa} - {self.tahun_akademik}"
