# Day 07: Fonksiyonlar (Functions)

## Fonksiyonlar Nedir?

Fonksiyonlar, tekrar kullanılabilir kod bloklarıdır. Bir görevi yerine getirir ve sonuç döndürür. "Don't Repeat Yourself" (DRY) prensibine uymak için kullanılır.

### Fonksiyon Tanımı

```python
def fonksiyon_adı(parametre1, parametre2):
    # Fonksiyon gövdesi
    sonuc = parametre1 + parametre2
    return sonuc
```

### Temel Örnek

```python
def selam_ver(isim):
    """Kullanıcıya selam veren fonksiyon"""
    print(f"Merhaba, {isim}!")

# Fonksiyonu çağırma (invoke)
selam_ver("Ayşe")  # Çıktı: Merhaba, Ayşe!
selam_ver("Mehmet")  # Çıktı: Merhaba, Mehmet!
```

### parametreler ve argümanlar

- **parametre**: Fonksiyon tanımında tanımlanan değişken
- **argüman**: Fonksiyon çağrısında geçirilen değer

```python
def carpma(isim, soyisim):
    """Tam isim döndüren fonksiyon"""
    return f"{isim} {soyisim}"

# Çoklu çağrı
print(carpma("Ali", "Veli"))  # Çıktı: Ali Veli
print(carpma("Elif", "Can"))  # Çıktı: Elif Can
```

### Öntanımlı Parametre Değerleri

```python
def selam_ver(isim="Dünya"):
    """Öntanımlı isimle selam ver"""
    print(f"Merhaba, {isim}!")

# Parametresiz çağrı (öntanımlı kullanılır)
selam_ver()  # Çıktı: Merhaba, Dünya!

# Parametreli çağrı
selam_ver("Python")  # Çıktı: Merhaba, Python!
```

### Keyword Argümanlar

```python
def hesapla(toplam, indirim=0):
    """Toplam ile indirim hesaplayan fonksiyon"""
    sonuc = toplam - indirim
    return sonuc

# Sadece required parametre
print(hesapla(100))  # 100

# İsteğe bağlı parametre
print(hesapla(100, 20))  # 80
print(hesapla(indirim=20, toplam=100))  # 80 (keyword arg)
```

### Lambda Fonksiyonlar (Anonymous Functions)

Tek satırlık anonim fonksiyonlar:

```python
# Normal fonksiyon
def kare(x):
    return x ** 2

# Lambda fonksiyon
kare = lambda x: x ** 2

print(kare(5))  # Çıktı: 25
```

### Fonksiyon ile Sıfır Bölden Büyük Kontrolü

```python
def pozitif_mi(sayı):
    """Sayı pozitif ise True, değilse False döner"""
    if sayı > 0:
        return True
    else:
        return False

# Kullanım
print(pozitif_mi(5))   # True
print(pozitif_mi(-3))  # False
print(pozitif_mi(0))   # False
```

### Docstring (Belgeleme)

Fonksiyonun ne yaptığını açıklamak için üç çift tırnak kullanılır:

```python
def kare_al(x):
    """
    Verilen sayıyı karesini döndürür.
    
    Args:
        x (int or float): Karesini alınacak sayı
    
    Returns:
        int or float: Sayıın karesi
    """
    return x ** 2

print(kare_al(5))  # Çıktı: 25
print(kare_al.__doc__)  # Docstring'i görüntüler
```

## Özet

| Konu | Açıklama |
|------|----------|
| **def** | Fonksiyon tanımlamak için kullanılır |
| **return** | Fonksiyonundan değer döndürmek için |
| **parametre** | Fonksiyona giden veri |
| **argument** | Çağrı sırasında geçen değer |
| **Öntanımlı** | Varsayılan değer |
| **Keyword** | Anahtar kelime ile geçirme |
| **Lambda** | Anonim, tek satırlı fonksiyon |
| **Docstring** | Fonksiyonun açıklaması |

---

**Ödev:** Aşağıdaki kodu yazıp çalıştırmayı deneyin:

```python
# Kendinizi seven bir fonksiyon oluşturun

def kendimi_tanitim(isim, yaş, şehir="Bilgi Yok"):
    """Kendi tanıtımını yapan fonksiyon"""
    print(f"Ben {isim}, {yaş' yaşındayım ve şehirim {şehir}.")

# Farklı çağrıları deneyin
kendimi_tanitim("Ali", 25)
kendimi_tanitim("Ayşe", 30, "İstanbul")
kendimi_tanitim(isim="Mehmet", yaş=40)  # şehir öntanımlı kullanılır
```