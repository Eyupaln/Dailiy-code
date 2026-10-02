def en_buyuk(liste):
    #en büyük diye bir fonskiyon oluşturduk içine liste gelecek
    en = liste[0]
    #eni listenin 0.elamanına atadık
    for sayi in liste:
    #for ile listede döngü yapıyoruz sayi 
        if sayi > en:
        #eğer sayi en den büyükse 
            en = sayi
        #eni sayiya atıyor 
    return en #sonucu ver 

def en_buyuk(liste):
    en = liste[0]  # İlk elemanı en büyük kabul et
    for sayi in liste:  # Her elemanı kontrol et
        if sayi > en:  # Daha büyük mü?
            en = sayi  # Güncelle
    return en  # Sonucu döndür

def ciftleri_al(liste):
    ciftler = []#ciftler adında liste alıyor 
    for sayi in liste:#her elamanı kontrol et 
        if sayi % 2 == 0: #eğer sayı ikiye bölününce kalansızsa
            ciftler.append(sayi)#ciftler dizisine koy sayiyi 
    return ciftler #sonucu döndür

def kelime_say(metin):
    kelimeler = metin.split()#kelimeleri boşluk karakteri ile ayırır
    return len(kelimeler)#kelimeleri döndür 


class Sayac:
    def __init__(self):
        self.deger = 0 #değeri sıfıra ata
    
    def artir(self):
        self.deger += 1 #değeri 1 artırt 
    
    def sifirla(self):
        self.deger = 0 #değeri sıfırlat
