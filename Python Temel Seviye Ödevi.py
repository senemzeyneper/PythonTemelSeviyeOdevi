#%% Bölüm1 : print() Fonksiyonu ve Yorum Satırları
#1.
print("Merhaba, Python Dünyası!")

#2.
print("Python","öğrenmek","çok","eğlenceli",sep = "-")

#3.
print("Adınız:",end = " ")
print("Senem Zeynep")

#4.
print("Python Dersleri \n\t - Konu 1 \n\t - Konu 2 ")

#5.
'''
Atama yaptığımız değişkenleri ekrana yazdırdık.
'''
isim = "Ahmet"
# Ahmet değerini isim değişkenin atıyoruz.Tipi string.
yas = 25
#25 değerini yas değişkenine atıyoruz. Tipi integer.
print(isim)
#isim değikenini ekrana yazdırır.
print(yas)
#yaş değişkenini ekrana yazdırır.


#%% Bölüm2: Değişkenler ve Veri Tipleri
#1.
ad = "Senem Zeynep"
dogum_yılı = 1999
boy = 1.60
ogrenci_mi = True
print(f"Benim adım {ad}, {dogum_yılı} yılında doğdum.Boyum {boy} metre ve öğrencilik durumum: {ogrenci_mi}")

#2.
favori_meyveler =["çilek","portakal","elma"]
print("liste :",favori_meyveler,  "type: ",type(favori_meyveler))
araba_bilgileri = ("Toyota", "Corolla", 2022)
print("tuple :",araba_bilgileri, "type: ",type(araba_bilgileri))
ogrenci_notlari = {85,90,78}
print("set :",ogrenci_notlari , "type: ",type(ogrenci_notlari))
kisi_bilgileri = {
    "ad " : "Senem",
    "soyad " : "Er",
    "sehir " : "İstanbul"
    }
print("dic :",kisi_bilgileri, "type: ",type(kisi_bilgileri))

#%% Bölüm 3: Tip Dönüşümleri (Type Casting)
#1.
str_deger = "1923"
int_deger = int(str_deger) 
print(int_deger + 100)

#2.
kullanici_yas = input("Yaşınızı giriniz :")
son_yas = int(kullanici_yas) + 10
print(son_yas)

#%% Bölüm4 : Operatörler
#1.
sayi1 = 50 
sayi2 = 15
toplam = sayi1 + sayi2
fark = sayi1 - sayi2
çarpım = sayi1 * sayi2
bölüm = sayi1 / sayi2
print("Sayıların toplamı:",toplam)
print("Sayıların farkı:",fark)
print("Sayıların çarpımı:",çarpım)
print("Sayıların bölümü:",bölüm)

#2.
sayi3 = int(input("Bir sayı giriniz :"))
bool1 = sayi3 > 100
bool2 = sayi3 == 100
bool3 = sayi3 < 100
print (f" 100'den büyük {bool1}, 100'e eşit {bool2}, 100'den küçük {bool3}")

#3.
kullanici_adi = "admin"
sifre = "12345"
if(kullanici_adi == "admin" and sifre == "12345"):
    print("Giriş yaptnız")
elif(kullanici_adi == "admin" or sifre == "12345"):
    if(kullanici_adi == "admin" and True):
        print("Sifrenizi yanlış girdiniz.Tekrar deneyiniz")
    else:
        print("Kullanıcı adınızı yanlış girdiniz.Tekrar deneyiniz ")
else:
    print("Giriş başarısız")
    
#%% Bölüm 5: math Modülü ve Dahili Fonksiyonlar

#1.
import math
r = 7
alan = math.pi * math.pow(r, 2)
cevre = 2 * math.pi * r
print("Dairenin alanı:", alan)
print("Dairenin çevresi:", cevre)

#2.
liste2= [15,4,27,13,32,8]
print("En büyük değer :",max(liste2))
print("En küçük değer :",min(liste2))
print("Toplam :",sum(liste2))


