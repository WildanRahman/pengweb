from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from .forms import *
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    # return HttpResponse("Hello World, Project pertama menggunakan Django!")
    
    template = loader.get_template('home.html')
    context = {
        'title' : 'beritaku.id',
    }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('home.html')
    context = {
        'title' : 'beritaku.id',
    }
    return HttpResponse(template.render(context, request))

def anime(request):
    template = loader.get_template('anime.html')
    data = Data_Berita.objects.filter(kategori='anime')
    context = {
        'kategori' : 'ANIME',
        'data' : data
    }
    return HttpResponse(template.render(context, request))
    
def characters(request):
    template = loader.get_template('characters.html')
    data = Data_Berita.objects.filter(kategori='characters')
    context = {
        'kategori' : 'CHARACTERS',
        'data' : data
    }
    return HttpResponse(template.render(context, request))
    
def storyarc(request):
    template = loader.get_template('storyarc.html')
    data = Data_Berita.objects.filter(kategori='storyarc')
    context = {
        'kategori' : 'STORY ARC',
        'data' : data
    }
    return HttpResponse(template.render(context, request))

def manga(request):
    template = loader.get_template('manga.html')
    data = Data_Berita.objects.filter(kategori='manga')
    context = {
        'kategori' : 'MANGA',
        'data' : data
    }
    return HttpResponse(template.render(context, request))
    
def login(request):
    if request.method == "POST":
        emailku = request.POST.get("email")
        passwordku = request.POST.get("password")

        try:
            cekuser = Data_Pengguna.objects.get(email=emailku,password=passwordku)
            data = Data_Pengguna.objects.filter(email=emailku)
            for r in data:
                request.session['nama'] = r.nama

            request.session['email'] = emailku
            request.session.save()
            return redirect("/beritaku/pengguna")
        except:
            return HttpResponse("""<script> alert("Username / Password Salah"); 
                                  window.location.href = "/beritaku/login"; </script>""")

    return render(request,"login.html")

def dashboard(request):
    if request.session.has_key('email'):
        email = request.session['email']
        nama = request.session['nama']
        return render(request, "admin/dashboard.html", {"email": email, "nama": nama})
    else:
        return redirect("/beritaku/login")


def detail(request, berita_id):
    template = loader.get_template('detail.html')
    data = Data_Berita.objects.filter(id=berita_id)
    context = {
        'title' : 'Detail',
        'data' : data
    }
    return HttpResponse(template.render(context, request))

def pengguna(request):
    if request.session.has_key('email'):
        email = request.session['email']
        nama = request.session['nama']
        return render(request, "admin/pengguna.html", {"email": email, "nama": nama})
    else:
        return redirect("/beritaku/login")

def lihatdata(request):
    if request.session.has_key('email'):
        email = request.session['email']
        nama = request.session['nama']
        template = loader.get_template('admin/lihatdata.html')
        berita = Data_Berita.objects.all()
        context = {
            'title': 'beritaku.id',
            'data': berita,
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/beritaku/login")

def keloladata(request):
	form = DataBerita(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponse('<script> alert("Data berhasil disimpan"); window.location.href = "/beritaku/lihatdata"; </script>')
	pass
	return render(request,"admin/keloladata.html",{'form': form})
        


def logout(request):
    try:
        del request.session['email']
    except:
        pass
    return redirect("/beritaku/login")

def hapusdata(request, berita_id):
    try:
        berita = Data_Berita.objects.get(id=berita_id)
        berita.delete()
        return HttpResponse("""<script> alert("data berhasil dihapus"); window.location.href = "/beritaku/lihatdata"; </script>""")
    
    except Data_Berita.DoesNotExist:
        raise Http404("task tidak ditemukan.")
    
def editdata(request, berita_id):
    obj = get_object_or_404(Data_Berita, id = berita_id)
    
    form = DataBerita(request.POST or None, instance= obj)
    if form.is_valid():
        form.save()
        return redirect("/beritaku/lihatdata")
    data = {
        'dt':obj,
            }
    
    return render(request, 'admin/editdata.html', data)