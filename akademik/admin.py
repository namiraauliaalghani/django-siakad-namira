from django.contrib import admin
from .models import TahunAkademik, MataKuliah, Jadwal, KRS

@admin.register(TahunAkademik)
class TahunAkademikAdmin(admin.ModelAdmin):
    list_display = ('tahun', 'semester')
    list_filter = ('semester',)
    search_fields = ('tahun', 'semester')


@admin.register(MataKuliah)
class MataKuliahAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kode', 'prodi', 'sks')
    list_filter = ('prodi',)
    search_fields = ('nama', 'kode', 'prodi')


@admin.register(Jadwal)
class JadwalAdmin(admin.ModelAdmin):
    list_display = ('mata_kuliah', 'dosen', 'hari', 'jam_mulai', 'jam_selesai', 'ruang', 'kuota_peserta', 'tahun_akademik')
    list_filter = ('hari', 'tahun_akademik', 'mata_kuliah')
    search_fields = ('dosen', 'mata_kuliah__nama', 'ruang')
    ordering = ('hari', 'jam_mulai')
    autocomplete_fields = ('mata_kuliah', 'tahun_akademik')


@admin.register(KRS)
class KRSAdmin(admin.ModelAdmin):
    list_display = ('mahasiswa', 'tahun_akademik')
    list_filter = ('tahun_akademik',)
    search_fields = ('mahasiswa',)
    filter_horizontal = ('jadwal',)  # Untuk mempermudah memilih jadwal dalam ManyToManyField
