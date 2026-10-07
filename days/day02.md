# Day 02: Değişkenler ve Veri Tipleri

## Değişkenler Nedir?

Değişkenler, programınız içinde kullanılacak verileri saklamak için kullanılan isimlerdir. Python'da değişken tanımlamak için bir tipe önceden ihtiyaç yok (dinamik tiplendirme).

## Temel Veri Tipleri

### 1. Tam Sayılar (Integers)
```python
sayi = 10
derinlik = -5
```

### 2. Ondalı Sayılar (Floats)
```python
pi = 3.14
yuzde = 50.5
```

### 3. Metinler (Strings)
```python
ad = "Ayşe"
metin = 'Merhaba Dunya'
```

### 4. Mantıksız Değerler (Booleans)
```python
aktif = True
kayitli = False
```

## Değişken Ataması ve Yazdırma

```python
# Birden çok değişken ataması
x, y, z = 1, 2, 3

# Değerleri yazdırma
print(x, y, z)

# Değişkenin türünü kontrol etme
print("x tipi:", type(x))
```

## Sabitler (Constants)

Tekrar kullanılacak aynı değeri saklamak için sabitler kullanılır. Python'da kesin bir constant (sabit) yoktur ama konvansiyonel olarak tüm büyük harfle isimlendirilir.

```python
PI = 3.14159
MAX_SAYI = 100
print(PI)
```

## Klavye Girdisi ve Çıktı

### Formatlı Çıktı (f-Strings)

Python 3'te yeni gelen en kolay çıktı formatı:

```python
ad = "Elif"
yaş = 25

# Eski yol
print("Ad: " + ad + ", Yaş: " + str(yaş))

# Yeni yol (f-String)
print(f"Ad: {ad}, Yaş: {yaş}")
```

### Çok Satırlı Girdi

```python
ad = input("Adınızı girin: ")
soyad = input("Soyadınızı girin: ")
print(f"{ad} {soyad} hayatında Python öğreniyor!")
```

## Değişken İsimlendirme Kuraları

1. Harf, rakam veya `_` (alt çizgi) içerebilir
2. Rakamla başlayamaz: `x1` ✅, `1x` ❌
3. Boşluk içeremez: `ad_soyad` ✅, `ad soyad` ❌
4. Python anahtar kelimeleri kullanılamaz: `class`, `def`, `import` vb.
5. Konvansiyonel: `snake_case` (iki_kelime_arasi_alt_cizgi)

### İsimlendirme Örnekleri

| Doğru | Yanlış |
|-------|--------|
| `kisí_ad` | `kişi ad` |
| `user_name` | `user name` |
| `sayi_1` | `1.sayi` |
| `toplam` | `toplam!` |

## Özet

| Konu | Açıklama |
|------|----------|
| **Değişken** | Veriyi saklayan isim |
| **Türler** | int, float, str, bool |
| **Atama** | `=` operatörü |
| **Çıktı** | `print()`, f-String |
| **İsimlendirme** | snake_case kuralı |

---

**Ödev:** Aşağıdaki kodu yazıp çalıştırmayı deneyin:

```python
# Kendinizi tanıtmak için bir kod
isim = input("Adınızı girin: ")
yaş = int(input("Yaşınızı girin: "))

print(f"Merhaba {isim}, yaşı {yaş} olan kullanıcıya hoş geldiniz!")

# Yaşınızın 10 yıl sonraki halini hesaplayın
gelecekgeles = yaş + 10
print(f"10 yıl sonra siz {gelecekgeles} yaşında olacaksınız!")
```