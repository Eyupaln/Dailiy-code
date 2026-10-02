# 2 Ekim 2026 - Kütüphane Sistemi
# OOP Uygulaması

# ============================================================
# Kitap Sınıfı
# ============================================================
# Her kitabın bir adı, yazarı, sayfa sayısı ve ödünç durumu vardır

class Kitap:
    def __init__(self, ad, yazar, sayfa_sayisi):
        # Kitap oluşturulurken ad, yazar ve sayfa sayısı verilir
        self.ad = ad
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.odunc_mu = False  # Başlangıçta ödünçte değil

    def __repr__(self):
        # Kitabı string olarak gösterir
        durum = "Ödünçte" if self.odunc_mu else "Mevcut"
        return f'{self.ad} - {self.yazar} ({durum})'


# ============================================================
# Uye Sınıfı
# ============================================================
# Her üyenin bir adı, üye numarası ve ödünç aldığı kitaplar vardır

class Uye:
    def __init__(self, ad, uye_no):
        # Üye oluşturulurken ad ve üye numarası verilir
        self.ad = ad
        self.uye_no = uye_no
        self.odunc_alinanlar = []  # Ödünç alınan kitaplar (boş liste)

    def __repr__(self):
        # Üyeyi string olarak gösterir
        return f'{self.ad} (Üye No: {self.uye_no})'


# ============================================================
# Kutuphane Sınıfı
# ============================================================
# Kütüphane, kitapları ve üyeleri yönetir

class Kutuphane:
    def __init__(self):
        # Kütüphane oluşturulurken boş listeler oluşturulur
        self.kitaplar = []  # Tüm kitaplar
        self.uyeler = []    # Tüm üyeler

    def kitap_ekle(self, kitap):
        # Yeni kitap ekle
        self.kitaplar.append(kitap)
        print(f"'{kitap.ad}' kütüphaneye eklendi.")

    def uye_ekle(self, uye):
        # Yeni üye ekle
        self.uyeler.append(uye)
        print(f"'{uye.ad}' üye oldu.")

    def odunc_ver(self, uye, kitap):
        # Üyeye kitap ödünç ver
        if kitap.odunc_mu:
            # Kitap zaten ödünçte
            print(f"'{kitap.ad}' zaten ödünçte.")
        else:
            # Kitabı ödünç ver
            kitap.odunc_mu = True
            uye.odunc_alinanlar.append(kitap)
            print(f"'{kitap.ad}' → '{uye.ad}' ödünç verildi.")

    def geri_al(self, uye, kitap):
        # Üyeden kitabı geri al
        if kitap in uye.odunc_alinanlar:
            # Kitap bu üyede
            kitap.odunc_mu = False
            uye.odunc_alinanlar.remove(kitap)
            print(f"'{kitap.ad}' geri alındı.")
        else:
            # Kitap bu üyede değil
            print(f"'{kitap.ad}' bu üyede değil.")

    def listele(self):
        # Tüm kitapları ve üyeleri listele
        print("\n--- Kitaplar ---")
        for kitap in self.kitaplar:
            print(kitap)
        print("\n--- Üyeler ---")
        for uye in self.uyeler:
            print(uye)


# ============================================================
# Test
# ============================================================

# Kütüphane oluştur
kutuphane = Kutuphane()

# Kitap ekle
kitap1 = Kitap("1984", "George Orwell", 328)
kitap2 = Kitap("Sefiller", "Victor Hugo", 1232)
kitap3 = Kitap("Küçük Prens", "Antoine de Saint-Exupéry", 96)
kutuphane.kitap_ekle(kitap1)
kutuphane.kitap_ekle(kitap2)
kutuphane.kitap_ekle(kitap3)

# Üye ekle
uye1 = Uye("Ali", "U001")
uye2 = Uye("Ayşe", "U002")
kutuphane.uye_ekle(uye1)
kutuphane.uye_ekle(uye2)

# Ödünç ver
kutuphane.odunc_ver(uye1, kitap1)
kutuphane.odunc_ver(uye2, kitap2)
kutuphane.odunc_ver(uye1, kitap3)

# Listele
kutuphane.listele()

# Geri al
kutuphane.geri_al(uye1, kitap1)
kutuphane.listele()
