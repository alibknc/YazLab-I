from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from tika import parser
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import File, User
from django.contrib import messages

dersler = ['ARAŞTIRMA PROBLEMLERİ', 'BİTİRME PROJESİ']
ogretimler = ['1. Öğretim', '2. Öğretim']

@login_required(login_url='/')
def home_view(request):
    if(request.user.is_superuser):
        return redirect('table')
    queryset = User.objects.filter(id=request.user.id)
    context = {'d': queryset[0]}

    return render(request, 'home.html', context)

class Home(TemplateView):
    template_name = 'base.html'

@login_required(login_url='/')
def upload(request):
    if(request.user.is_superuser):
        return redirect('table')

    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        readPDF(context['url'], uploaded_file, request)

    messages.info(request, 'Dosya Başarıyla Yüklendi!')
    return render(request, 'upload.html', context)


def readPDF(file, pdf, request):
    raw = parser.from_file('.\\'+file)

    metin = raw['content']

    x = metin.find('LİSANS TEZİ')
    metin = metin[x+11:]
    y = metin.find('KOCAELİ')
    temp = metin[:y]
    temp = temp.split("\n")

    for i in temp:
        i.strip()
        if i == ' ' or i == " " or len(i) < 1:
            temp.remove(i)

    a = []
    for i in temp:
        if i != "" and len(i) > 1:
            a.append(i.strip())

    baslik = a[0]
    isim = a[1]

    metin = metin[y+8:]
    x = metin.find('KOCAELİ ÜNİVERSİTESİ')
    yil = metin[:x-5]
    metin = metin[x:]

    x = metin.find('BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ')
    metin = metin[x+39:]
    y = metin.find(baslik.split()[0])
    ders = metin[:y-9]

    x = metin.find(isim)
    metin = metin[x+len(isim):]
    y = metin.find("Tezin")
    temp = metin[:y-5]
    a = temp.split(" ................................................")
    danisman = (a[0].split(" \nDanışman, Kocaeli Üniv."))[0][0:].strip()
    juri1 = (a[1].split(" \nJüri Üyesi, Kocaeli Üniv."))[0][2:].strip()
    juri2 = (a[2].split(" \nJüri Üyesi, Kocaeli Üniv."))[0][2:].strip()

    metin = metin[y+25:]
    x = metin.find("ÖNSÖZ")
    donem = metin[:x-19]
    parts = donem.split(".")
    if(int(parts[1]) >= 9 and int(parts[1]) <= 12):
        donem = "Güz " + parts[2]
    else:
        donem = "Bahar " + parts[2]

    x = metin.find('Öğrenci No:')
    metin = metin[x+12:]
    y = metin.find('Adı Soyadı')
    ogrNo = metin[:y-3]
    ogretim = ogrNo[5] + ". Öğretim"

    x = metin.find('ÖZET')
    metin = metin[x+4:]
    x = metin.find('ÖZET')
    metin = metin[x+7:]
    y = metin.find('Anahtar kelimeler:')
    ozet = metin[:y-3].replace('\n', '').strip()

    metin = metin[y+19:]
    x = metin.find('.')
    kelimeler = metin[:x].replace('\n', '')

    File.objects.create(hocaID=request.user.id, yazarAdi=isim, dersAdi=ders, baslik=baslik, donem=donem, danisman=danisman,
                        juriler=juri1+","+juri2, numara=ogrNo, ogretim=ogretim, ozet=ozet, anahtarKelimeler=kelimeler, pdf=pdf)

@login_required(login_url='/')
def Table(request):
    queryset = File.objects.all()
    if(not request.user.is_superuser):
        queryset = queryset.filter(hocaID=request.user.id)

    baslik = request.GET.get('baslik')
    numara = request.GET.get('numara')
    anahtar = request.GET.get('anahtar')
    ogretim = request.GET.get('ogretim')
    ders = request.GET.get('ders')
    donem = request.GET.get('donem')
    
    if validParameter(baslik):
        queryset = queryset.filter(baslik__icontains=baslik)

    if validParameter(numara):
        queryset = queryset.filter(numara__icontains=numara)

    if validParameter(anahtar):
        queryset = queryset.filter(anahtarKelimeler__icontains=anahtar)

    if validParameter(ogretim) and ogretim != "Seçiniz...":
        queryset = queryset.filter(ogretim=ogretim)

    if validParameter(ders) and ders != "Seçiniz...":
        queryset = queryset.filter(dersAdi__icontains=ders)

    if validParameter(donem) and donem != "Seçiniz...":
        queryset = queryset.filter(donem__icontains=donem) 

    context = {'d': queryset, 'dersler': dersler, 'ogretimler': ogretimler, 'donemler': donemOlustur()}

    return render(request, 'table.html', context)

def validParameter(param):
    return param != '' and param is not None

@cache_control(no_cache=True, must_revalidate=True)
def logOut(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def details_view(request, id):
    queryset = File.objects.filter(numara=id)
    context = {'d': queryset}

    return render(request, 'details.html', context)

def donemOlustur():
    donemler = []
    yil1 = 2015
    yil2 = 2022
    for i in range(yil1, yil2):
        dnm1 = "Güz " + str(i)
        dnm2 = "Bahar " + str(i)
        donemler.append(dnm1)
        donemler.append(dnm2)
    return donemler