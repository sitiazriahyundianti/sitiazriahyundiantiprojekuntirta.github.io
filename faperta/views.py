from django.shortcuts import render, redirect
from faperta.models import Mahasiswa
from faperta.forms import FormMahasiswa
from django.contrib import messages

def hapus_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.filter(id=id_mahasiswa)
    mahasiswa.delete()

    messages.success(request, "Data Berhasil Dihapus!")
    return redirect('hapus_mahasiswa', id_mahasiswa=id_mahasiswa)

def ubah_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.get(id=id_mahasiswa)
    template = 'ubah-mahasiswa.html'
    if request.POST:
        form = FormMahasiswa(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbaharui!")
            return redirect('ubah_mahasiswa', id_mahasiswa=id_mahasiswa)
    else:
        form = FormMahasiswa(instance=mahasiswa)
        konteks = {
            'form':form,
            'mahasiswa':mahasiswa,
        }
    return render(request, template, konteks)


# Create your views here.
def faperta(request):
    mahasiswa = Mahasiswa.objects.all()

    konteks = {
        'mahasiswa': mahasiswa,
    }
    return render(request, 'faperta.html', konteks)

def tambah_mahasiswa(request):
    if request.POST:
        form = FormMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            form = FormMahasiswa ()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-mahasiswa.html', konteks)
    else:
        form = FormMahasiswa()

        konteks = {
            'form': form,
    }

    return render(request, 'tambah-mahasiswa.html', konteks)
