from django.shortcuts import render

# Create your views here.
def profil(request):
    judul = "Maksud dan tujuan pendirian yayasan ini adalah :"
    s1 = ["Membantu usaha-usaha pemerintah dalam bidang pendidikan umum.", "Mendirikan sekolah-sekolah mulai dari taman kanak-kanak sampai dengan perguruan tinggi, termasuk juga sekolah-sekolah kejuruan.", "Merencanakan dan mengusahakan sarana pendidikan, serta sarana olah raga."]
    visi = ["Meningkatkan kualitas, relevansi dan daya saing pendidikan.", "Meningkatkan kualitas dan kuantitas penelitian dan pengabdian kepada masyarakat yang inovatif berbasis kehidupan nyata.", "Meningkatkan daya dukung tatakelola perguruan tinggi yang baik (Good University Good Governance)."]
    konteks = {
        'title': judul,
        's1': s1,
        'visi': visi,
    }
    return render(request, 'profil.html', konteks)