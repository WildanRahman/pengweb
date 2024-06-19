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
        'title' : 'telcomedy.xd',
    }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('home.html')
    context = {
        'title' : 'telcomedy.xd',
    }
    return HttpResponse(template.render(context, request))

def anime(request):
    template = loader.get_template('anime.html')
    data = Data_Comedy.objects.filter(kategori='anime')
    context = {
        'kategori' : 'ANIME',
        'data' : data
    }
    return HttpResponse(template.render(context, request))
    
def random(request):
    template = loader.get_template('random.html')
    data = Data_Comedy.objects.filter(kategori='random')
    context = {
        'kategori' : 'RANDOM',
        'data' : data
    }
    return HttpResponse(template.render(context, request))
    
def ittp(request):
    template = loader.get_template('ittp.html')
    data = Data_Comedy.objects.filter(kategori='ittp')
    context = {
        'kategori' : 'ITTP',
        'data' : data
    }
    return HttpResponse(template.render(context, request))

def feeling(request):
    template = loader.get_template('feeling.html')
    data = Data_Comedy.objects.filter(kategori='feeling')
    context = {
        'kategori' : 'FEELING',
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
            return redirect("/telcomedy/pengguna")
        except:
            return HttpResponse("""<script> alert("Username / Password Salah"); 
                                  window.location.href = "/telcomedy/login"; </script>""")

    return render(request,"login.html")

def dashboard(request):
    if request.session.has_key('email'):
        email = request.session['email']
        nama = request.session['nama']
        return render(request, "dashboard.html", {"email": email, "nama": nama})
    else:
        return redirect("/telcomedy/login")


def detail(request, berita_id):
    template = loader.get_template('detail.html')
    data = Data_Comedy.objects.filter(id=berita_id)
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
        return redirect("/telcomedy/login")

def lihatdata(request):
    if request.session.has_key('email'):
        email = request.session['email']
        nama = request.session['nama']
        template = loader.get_template('admin/lihatdata.html')
        berita = Data_Comedy.objects.all()
        context = {
            'title': 'telcomedy.xd',
            'data': berita,
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/telcomedy/login")

def keloladata(request):
	form = DataMeme(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponse('<script> alert("Data berhasil disimpan"); window.location.href = "/telcomedy/lihatdata"; </script>')
	pass
	return render(request,"admin/keloladata.html",{'form': form})
        


def logout(request):
    try:
        del request.session['email']
    except:
        pass
    return redirect("/telcomedy/login")

def hapusdata(request, berita_id):
    try:
        berita = Data_Comedy.objects.get(id=berita_id)
        berita.delete()
        return HttpResponse("""<script> alert("data berhasil dihapus"); window.location.href = "/telcomedy/lihatdata"; </script>""")
    
    except Data_Comedy.DoesNotExist:
        raise Http404("task tidak ditemukan.")
    
def editdata(request, berita_id):
    obj = get_object_or_404(Data_Comedy, id = berita_id)
    
    form = DataMeme(request.POST or None, instance= obj)
    if form.is_valid():
        form.save()
        return redirect("/telcomedy/lihatdata")
    data = {
        'dt':obj,
            }
    
    return render(request, 'admin/editdata.html', data)