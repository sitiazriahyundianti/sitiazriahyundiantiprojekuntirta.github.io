from django.shortcuts import render

# Create your views here.
def pascasarjana(request):
    judul = "Profil"
    s1 = ["Visi & Misi", "Sejarah"]

    konteks = {
        'title': judul,
        's1': s1,
    }
    return render(request, 'indexpascasarjana.html', konteks)
