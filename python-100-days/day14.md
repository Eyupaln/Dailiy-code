# Python-100-Days: Day 14 — Fonksiyonlar ve Modüller

## Fonksiyon Nedir?

Fonksiyon, **tekrar kullanılabilen kod bloğudur**. Amacı:
- **Kod tekrarını önle**
- **Modülerlik** sağla
- **Okunabilirlik** artır

---

## Fonksiyon Tanımlama

```python
def fonksiyon_adi(parametre1, parametre2):
    # Fonksiyon gövdesi
    sonuc = parametre1 + parametre2
    return sonuc  # Dönüş değeri
```

### Örnek: Faktoriyel

```python
def faktoriyel(n):
    sonuc = 1
    for i in range(2, n + 1):
        sonuc *= i
    return sonuc

print(faktoriyel(5))  # 120
```

---

## Parametre Türleri

### 1. Pozisyonel Parametreler

```python
def topla(a, b):
    return a + b

print(topla(3, 5))  # 8
```

### 2. Anahtar Kelime Parametreler

```python
def kisi(ad, yas):
    return f"{ad}, {yas} yaşında"

print(kisi(ad="Ali", yas=25))  # Ali, 25 yaşında
```

### 3. Varsayılan Parametreler

```python
def selamla(ad, mesaj="Merhaba"):
    return f"{mesaj}, {ad}!"

print(selamla("Ali"))              # Merhaba, Ali!
print(selamla("Ali", "Selam"))     # Selam, Ali!
```

### 4. *args (Değişken Sayıda Pozisyonel Parametre)

```python
def toplam(*sayilar):
    sonuc = 0
    for sayi in sayilar:
        sonuc += sayi
    return sonuc

print(toplam(1, 2, 3))      # 6
print(toplam(1, 2, 3, 4))   # 10
```

### 5. **kwargs (Değişken Sayıda Anahtar Kelime Parametre)

```python
def bilgi(**kwargs):
    for anahtar, deger in kwargs.items():
        print(f"{anahtar}: {deger}")

bilgi(ad="Ali", yas=25, sehir="İstanbul")
# ad: Ali
# yas: 25
# sehir: İstanbul
```

---

## Return Değeri

Fonksiyonlar bir veya daha fazla değer döndürebilir:

```python
def hesapla(a, b):
    toplam = a + b
    fark = a - b
    return toplam, fark

sonuc1, sonuc2 = hesapla(10, 3)
print(sonuc1)  # 13
print(sonuc2)  # 7
```

**Not:** `return` yoksa fonksiyon `None` döndürür.

---

## Modüller

Modül, **Python kodunu içeren dosyalar**. Amaç:
- **Kod organizasyonu**
- **Yeniden kullanım**
- **İsim çakışmalarını önleme**

### Modül İçe Aktarma

```python
# Tüm modülü içe aktar
import math
print(math.pi)  # 3.14159...

# Belirli fonksiyonu içe aktar
from math import sqrt
print(sqrt(16))  # 4.0

# Kısaltma
import numpy as np
```

### Kendi Modülünü Oluşturma

**dosya: `hesap.py`**
```python
def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b
```

**dosya: `main.py`**
```python
import hesap

print(hesap.topla(5, 3))   # 8
print(hesap.cikar(5, 3))   # 2
```

---

## Özet Tablo

| Özellik | Açıklama |
|---------|----------|
| `def` | Fonksiyon tanımlama |
| `return` | Dönüş değeri |
| `*args` | Değişken pozisyonel parametre |
| `**kwargs` | Değişken anahtar kelime parametre |
| `import` | Modül içe aktarma |
| `from ... import` | Belirli fonksiyon içe aktarma |

---

## Sıradaki Adım

Day 15: Fonksiyon pratiği
