from tika import parser

raw = parser.from_file('tez3.pdf')

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
print(yil)

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
print(danisman + " " + juri1 + " " + juri2)

metin = metin[y+25:]
x = metin.find("ÖNSÖZ")
donem = metin[:x-19]
parts = donem.split(".")
if(int(parts[1]) >= 9 and int(parts[1]) <= 12):
    donem = "Güz " + parts[2]
else:
    donem = "Bahar " + parts[2]
print(donem)

x = metin.find('Öğrenci No:')
metin = metin[x+12:]
y = metin.find('Adı Soyadı')
ogrNo = metin[:y-3]
ogretim = ogrNo[5] + ". Öğretim"
print(ogrNo + " " + ogretim)

x = metin.find('ÖZET')
metin = metin[x+4:]
x = metin.find('ÖZET')
metin = metin[x+7:]
y = metin.find('Anahtar kelimeler:')
ozet = metin[:y-3].replace('\n', '').strip()
print(ozet)

metin = metin[y+19:]
x = metin.find('.')
kelimeler = metin[:x].replace('\n', '')
print(kelimeler)