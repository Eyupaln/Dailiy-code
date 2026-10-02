# 1 Ekim 2026 - Egzersiz
# Kurallar:
# 1. Önce yorum satırıyla ne yapacağını yaz
# 2. Altına kodu yaz
# 3. Çalıştırıp testlerini print ile kontrol et
# 4. Takılırsan 10 dakika dene, sonra bana yaz

# ============================================================
# Seviye 1: Fonksiyon
# ============================================================

# 1. selamla(isim) yaz. selamla("Eyüp") çıktısı: Merhaba Eyüp!

def selamla(isim):
    return(f"merhaba {isim}")

print (selamla("eyyüp"))


# 2. cift_mi(sayi) yaz. Çiftse True, değilse False döndürsün.

def cift_mi(sayi):
    return sayi % 2 == 0 
print(cift_mi(4))
print(cift_mi(7))

# 3. toplam(liste) yaz. toplam([1, 2, 3]) çıktısı: 6 (hazır sum kullanma, döngüyle yaz).

def toplam(*liste):
    total= 0
    for num in liste:
        total += num
    return total

print (toplam(1,2,3))


# ============================================================
# Seviye 2: Liste ve döngü
# ============================================================

# 4. en_buyuk(liste) yaz. max kullanma, döngüyle bul.

def en_buyuk(liste):
    en = liste[0]
    for sayi in liste:
        if sayi > en:
            en=sayi
        return
    
# 5. ciftleri_al(liste) yaz. [1, 2, 3, 4] için [2, 4] döndürsün.

def ciftal(liste):
    ciftler=[]
    for sayi in liste % 2 == 0 :
        if sayi & 2 == 0 :
            ciftler.append(sayi)
    return ciftler


# 6. kelime_say(metin) yaz. "ali ata bak" için 3 döndürsün.
# bunu da anlamadım


# ============================================================
# Seviye 3: Küçük sınıf
# ============================================================

# 7. Sayac sınıfı yaz:
#    - __init__ içinde self.deger = 0
#    - artir() metodu 1 artırsın
#    - sifirla() metodu 0 yapsın
class Sayac:
    def __init__(self):
        self.deger=0

    def artir(self):
        self.deger +=1

    def azalt(self):
        self.azal -=1

    def sifirla(self):
        self.sifir=0
        
#
#    Test:
#    s = Sayac()
#    s.artir()
#    s.artir()
#    print(s.deger)  # 2



# ============================================================
# Testler (kodunu yazdıktan sonra çalıştır)
# ============================================================

if __name__ == "__main__":
    # 1. selamla
    # print(selamla("Eyüp"))

    # 2. cift_mi
    # print(cift_mi(4))
    # print(cift_mi(7))

    # 3. toplam
    # print(toplam([1, 2, 3]))

    # 4. en_buyuk
    # print(en_buyuk([3, 7, 2, 9, 1]))

    # 5. ciftleri_al
    # print(ciftleri_al([1, 2, 3, 4]))

    # 6. kelime_say
    # print(kelime_say("ali ata bak"))

    # 7. Sayac
    # s = Sayac()
    # s.artir()
    # s.artir()
    # print(s.deger)
    pass
