from django.shortcuts import render

# Create your views here.
def fkip(request):
    judul = "Akademik"
    s1 = ["Program Studi S-1", "Program Studi S-2", "Program Studi S-3"]

    konteks = {
        'title': judul,
        's1': s1,
    }
    return render(request, 'indexfkip.html', konteks)
