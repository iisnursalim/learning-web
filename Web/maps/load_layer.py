import os
from django.contrib.gis.utils import LayerMapping
from .models import Jalan, Jembatan, Kesehatan, Drainase, Kab_Sidrap
    
jalan_mapping = {
    'remark': 'REMARK',
    'shape_leng': 'SHAPE_Leng',
    'surveyor': 'SURVEYOR',
    'surv_time': 'SURV_TIME',
    'number': 'NUMBER',
    'name': 'NAME',
    'length_km': 'LENGTH_KM',
    'width_m': 'WIDTH_M',
    'tpp': 'TPP',
    'tpu': 'TPU',
    'lhr': 'LHR',
    'status': 'STATUS',
    'surf_type': 'SURF_TYPE',
    'kondisi': 'KONDISI',
    'hambatan': 'HAMBATAN',
    'tahun': 'TAHUN',
    'anggaran': 'ANGGARAN',
    'geom': 'LINESTRING25D',
}

jalan_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'media', 'Jalan.shp'),
)

jembatan_mapping = {
    'surveyor': 'SURVEYOR',
    'surv_date': 'SURV_DATE',
    'nama': 'NAMA',
    'pal_km': 'PAL_KM',
    'panjang_m': 'PANJANG_M',
    'lebar_m': 'LEBAR_M',
    'bentang': 'BENTANG',
    'tipe_jem': 'TIPE_JEM',
    'penyebrang': 'PENYEBRANG',
    'bhn_konstr': 'BHN_KONSTR',
    'kondisi': 'KONDISI',
    'tahun': 'TAHUN',
    'anggaran': 'ANGGARAN',
    'geom': 'POINT25D',
}

jembatan_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'media', 'Jembatan.shp'),
)

kesehatan_mapping = {
    'namobj': 'NAMOBJ',
    'remark': 'REMARK',
    'alamat': 'ALAMAT',
    'jml_dktr': 'JML_DKTR',
    'jml_prwt': 'JML_PRWT',
    'jml_pasien': 'JML_PASIEN',
    'jml_ruang': 'JML_RUANG',
    'fasilitas': 'FASILITAS',
    'kond_bgnn': 'KOND_BGNN',
    'tahun': 'TAHUN',
    'anggaran': 'ANGGARAN',
    'sumb_dana': 'SUMB_DANA',
    'kontraktor': 'KONTRAKTOR',
    'surv_time': 'SURV_TIME',
    'geom': 'POINT25D',
}

kesehatan_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'media', 'Kesehatan.shp'),
)

drainase_mapping = {
    'lcode': 'LCODE',
    'shape_leng': 'SHAPE_Leng',
    'rpru': 'RPRU',
    'kemiringan': 'KEMIRINGAN',
    'panjang_m': 'PANJANG_M',
    'kdlmn_m': 'KDLMN_M',
    'kondisi': 'KONDISI',
    'tahun': 'TAHUN',
    'anggaran': 'ANGGARAN',
    'kontraktor': 'KONTRAKTOR',
    'surv_time': 'SURV_TIME',
    'geom': 'LINESTRING25D',
}

drainase_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'media', 'Drainase.shp'),
)

kab_sidrap_mapping = {
    'provinsi': 'PROVINSI',
    'kecamatan': 'KECAMATAN',
    'desa': 'DESA',
    'sumber': 'SUMBER',
    'kode2010': 'KODE2010',
    'provno': 'PROVNO',
    'kabkotno': 'KABKOTNO',
    'kecno': 'KECNO',
    'desano': 'DESANO',
    'kabkot': 'KABKOT',
    'geom': 'MULTIPOLYGON',
}

kab_sidrap_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'media', 'Kab_Sidrap.shp'),
)

def run(verbose=True):
    lm = LayerMapping(Jalan, jalan_shp, jalan_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

def run(verbose=True):    
    lm = LayerMapping(Jembatan, jembatan_shp, jembatan_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

def run(verbose=True): 
    lm = LayerMapping(Kesehatan, kesehatan_shp, kesehatan_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

def run(verbose=True):
    lm = LayerMapping(Drainase, drainase_shp, drainase_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

def run(verbose=True): 
    lm = LayerMapping(Kab_Sidrap, kab_sidrap_shp, kab_sidrap_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


