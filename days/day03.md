# Day 03: Yorumlar, Girdi ve Çıktı

## Yorumlar (Comments)

Yorumlar, kodun anlaşılırlığını artırmak ve nedan yapıldığını belgelemek için kullanılır. Python'da yorum satırı `#` karakteri ile başlar.

```python
# Bu bir yorum satırı
print("Bu yorumdan etkilenmez")

# Değişken ataması
x = 5  # Bu yorum da değişkenin açıklamasıdır
```

### Çok Satırlı Yorumlar

```python
'''
Bu bir
çok satırlı
yorum bloğudur.
'''
print("Hala yorumdasınız")
```

## Kullanıcı Girişi (Input)

Kullanıcıdan veri almak için `input()` fonksiyonu kullanılır. Gelen her şey `string` (metin) olarak kabul edilir.

```python
isim = input("Adınızı girin: ")
print("Merhaba", isim, "!")
```

### Tip Dönüşümü

```python
# Sayıya dönüştürme
yas_str = input("Yaşınızı girin: ")
yas_int = int(yas_str)
print("Yas tipi:", type(yas_int))

# Ondalı sayıya dönüştürme
poz_str = input("Lütfen bir sayı girin: ")
poz_float = float(poz_str)
print("Float tipi:", type(poz_float))
```

## Çıktı Biçimlendirme

### 1. Basit Yazdırma

```python
ad = "Ayşe"
yas = 25
print("Benim adım", ad, "ve yaşı", yas, ".")
```

### 2. F-String (Python 3.6+)

```python
print(f"Benim adım {ad} ve yaşı {yas}.")
print(f"5'in karesi {5**2}.")
```

### 3. Format Metodu

```python
print("Benim adım {} ve yaşı {}.".format(ad, yas))
```

## Örnek Uygulama: Kullanıcı Bilgileri Toplama

```python
print("=== Kullanıcı Bilgileri ===")

# Kullanıcıdan isim ve soyisim alın
ad = input("Adınızı girin: ")
soyad = input("Soyadınızı girin: ")

# Yaş alın ve integer'a dönüştürülmesi
yas_girdisi = input("Yaşınızı girin: ")
yas = int(yas_girdisi)

# Basit bir ekrana yazdırma
print("-" * 30)
print(f"Ad Soyad: {ad} {soyad}")
print(f"Yaş: {yas}")
print(f"Doşum yılı: {2026 - yas}")
print("-" * 30)
```

## Hata Yönetimi (Girişler İçin)

Kullanıcının yanlış veri girmesi durumunda programın çökmemesi için `try-except` kullanılabilir:

```python
try:
    yas = int(input("Yaşınızı girin: "))
    print("Geçerli bir yaş girdiniz:", yas)
except ValueError:
    print("Hata: Lütfen sayısal bir değer girin!")
```

## Özet

| Konu | Açıklama |
|------|----------|
| **Yorumlar** | `#` ile satır, `'''` ile blok |
| **Input** | `input()` fonksiyonu, string döner |
| **Tip Dönüşümü** | `int()`, `float()`, `str()` |
| **Çıktı** | `print()`, f-String, `.format()` |
| **Hata Yönetimi** | `try-except` bloğu |

---

**Ödev:** Aşağıdaki kodu yazıp çalıştırmayı deneyin:

```python
print("=== Yaş Hesaplama ===")
giris = input("Doğum yılınızı girin: ")

try:
    yil = int(giris)
    yas = 2026 - yil
    print(f"Şu anki yasınız: {yas}")
    print(f"10 yil sonra: {yas + 10}")
except ValueError:
    print("Lütfen geçerli bir yıl girin!")
```