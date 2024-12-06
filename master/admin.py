from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import (
    FieldTextFilter,
    RangeDateFilter,
    MultipleChoicesDropdownFilter,
    MultipleRelatedDropdownFilter,
)

from .models import (
    Prodi,
    Mahasiswa,
    Dosen,
    Ruang
)


@admin.register(Prodi)
class ProdiAdmin(ModelAdmin):
    pass


@admin.register(Mahasiswa)
class MahasiswaAdmin(ModelAdmin):
    pass


@admin.register(Dosen)
class DosenAdmin(ModelAdmin):
    list_filter_submit = True
    list_filter = [
        ("nama", FieldTextFilter),
        ("tgl_lahir", RangeDateFilter),
        ("jenis_kelamin", MultipleChoicesDropdownFilter,),
        ("prodi", MultipleRelatedDropdownFilter),
    ]


@admin.register(Ruang)
class RuangAdmin(ModelAdmin):
    pass
