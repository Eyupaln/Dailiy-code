# Day 01: Python ile İlk Adım

## Python Nedir?

Python, **1991'de Guido van Rossum** tarafından geliştirilmeye başlayan, açık kaynak kodlu ve yüksek seviyeli bir programlama dilidir. Basit ve okunabilir tasarımıyla bilinir, özellikle yeni başlayanlar için ideal bir dildir.

## Python Kurulumu

### Windows'ta Kurulum
1. [python.org](https://www.python.org) adresinden en son sürümü indirin
2. "Add Python to PATH" seçeneğini işaretleyin
3. "Customize installation" ekranında "Add Python to PATH" önemsiz olsun
4. Install'a tıklayın
5. Komut satırını yeniden başlatın

### Doğrulama
```bash
python --version
# Ya da
python3 --version
```

## İlk Program: Merhaba Dünya

Her programlama dilinde gelen en temel kod:

```python
print("Merhaba, Python!")
```

**Çıktı:**
```
Merhaba, Python!
```

## Değişkenler ve Veri Tipleri

Değişkenler ile verileri saklayabiliriz. Python'da tipe önceden ihtiyaç yok (dinamik dil).

```python
# Tam sayılar
yas = 25

# Onalı sayılar
pi = 3.14

# Metin (string)
ad = "Ayşe"

# Mantıksız değerler
aktif = True

# Değerleri yazdırma
print(yas, pi, ad, aktif)
```

### Kullanıcı Girişi

```python
isim = input("Adınızı girin: ")
print("Merhaba", isim, "!")
```

## Örnek Uygulama: Basit Hesap makinesi

```python
print("=== Basit Hesap Makinesi ===")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpım")
print("4. Bölüm")

secim = int(input("Yapmak istediğiniz işlemi seçin (1-4): "))

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

if secim == 1:
    print("Sonuç:", sayi1 + sayi2)
elif secim == 2:
    print("Sonuç:", sayi1 - sayi2)
elif secim == 3:
    print("Sonuç:", sayi1 * sayi2)
elif secim == 4:
    if sayi2 != 0:
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Hata: Sıfıra bölme yapılamaz!")
else:
    print("Geçersiz seçim!")
```

## Özet

| Konu | Açıklama |
|------|----------|
| **Python** | Yüksek seviyeli, okunabilir programlama dili |
| **print()** | Ekrana yazdırma |
| **Değişkenler** | Tip dışı (dinamik) veri saklama |
| **input()** | Kullanıcıdan veri alma |
| **Veri tipleri** | int, float, str, bool |

---

**Ödev:** Yukarıdaki kodu çalıştırabileceğiniz bir dosya oluşturun ve `print("Bugün Python öğreniyorum!")` ifadesini ekrana yazdırın.

---