from django.shortcuts import render, redirect
from .models import Makaleler

from django.core.paginator import Paginator

# Create your views here.
def index(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'mainapp/index.html', {'ucmakale' : ucmakale})

def about(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'mainapp/about.html', {'ucmakale' : ucmakale})

def ailehukuku(request):
    ucmakale= Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'mainapp/ailehukuku.html', {'ucmakale' : ucmakale, 'nbar' : 'ailehukuku'})

def cezahukuku(request):
    ucmakale= Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'mainapp/cezahukuku.html', {'ucmakale' : ucmakale, 'nbar' : 'cezahukuku'})

def gayrimenkulhukuku(request):
    ucmakale= Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'mainapp/gayrimenkulhukuku.html', {'ucmakale' : ucmakale, 'nbar' : 'gayrimenkulhukuku'})

def icrahukuku(request):
    ucmakale= Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'mainapp/icrahukuku.html', {'ucmakale' : ucmakale, 'nbar' : 'icrahukuku'})

def ishukuku(request):
    ucmakale= Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'mainapp/ishukuku.html', {'ucmakale' : ucmakale, 'nbar' : 'ishukuku'})

def mirashukuku(request):
    ucmakale= Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'mainapp/mirashukuku.html', {'ucmakale' : ucmakale, 'nbar' : 'mirashukuku'})

def tazminathukuku(request):
    ucmakale= Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'mainapp/tazminathukuku.html', {'ucmakale' : ucmakale, 'nbar' : 'tazminathukuku'})

def ticarethukuku(request):
    ucmakale= Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'mainapp/ticarethukuku.html', {'ucmakale' : ucmakale, 'nbar' : 'ticarethukuku'})

def tiphukuku(request):
    ucmakale= Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'mainapp/tiphukuku.html', {'ucmakale' : ucmakale, 'nbar' : 'tiphukuku'})

def iletisim(request):
    ucmakale= Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    if request.method == 'POST':
        adsoyad = request.POST.get('isim')
        telefon = request.POST.get('telefon')
        mesaj = request.POST.get('mesaj')
        print(adsoyad)

        return redirect('index')

    return render(request, 'mainapp/iletisim.html', {'ucmakale' : ucmakale})

def yayinlar(request):
    ucmakale= Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    if request.GET.get('hukuki-alan'):

        alan = request.GET.get('hukuki-alan')

        makale_list = Makaleler.objects.filter(makale_kategori=alan)

        paginator = Paginator(makale_list, 4)

        page = request.GET.get('page')
        articles = paginator.get_page(page)

        return render(request, 'mainapp/yayinlar.html', {'articles' : articles, 'ucmakale' : ucmakale, 'alan' : alan })
    else:
        makale_list = Makaleler.objects.all()
        paginator = Paginator(makale_list, 4)

        page = request.GET.get('page')
        articles = paginator.get_page(page)
        return render(request, 'mainapp/yayinlar.html', {'articles' : articles, 'ucmakale' : ucmakale})

def makaledetay(request, makaleslug):

    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]

    oncekimakale = Makaleler.objects.all().order_by('?').first()
    sonrakimakale = Makaleler.objects.all().order_by('?').first()

    makale = Makaleler.objects.get(makale_slug=makaleslug)

    return render(request, 'mainapp/makaledetay.html', {'makale' : makale,'ucmakale' : ucmakale, 'oncekimakale' : oncekimakale, 'sonrakimakale' : sonrakimakale})
