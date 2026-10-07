# Day 09: Sözlükler (Dict)

## Sözlükler (Dictionaries) Nedir?

Sözlükler, **anahtar-değer (key-value)** çiftlerinden oluşan değiştirilebilir koleksiyonlardır. Listeler gibi indis numaralı erişim yerine, anahtarlar kullanılarak değerlere erişilir.

### Sözlük Tanımı

```python
# Boş bir sözlük
bilgiler = {}

# Elemanlar ile birlikte oluşturulmuş sözlük
kisi = {
    "ad": "Ali",
    "yaş": 25,
    "şehir": "İstanbul",
    "ehliyet_var": True
}
```

### Anahtar-Değer Çiftlerine Erişim

```python
# Değer erişimi (anahtar kullanarak)
print(kisi["ad"])  # Çıktı: Ali
print(kıya["şehir"])  # Çıktı: İstanbul

# Yeni anahtar-değer ekleme
kisi["telefon"] = "555-1234"

# Var olanı güncelleme
kisi["yaş"] = 26

# Anahtar silme
del kisi["ehliyet_var"]
```

### Sözlük Metotları

| Metot | Açıklama |
|-------|----------|
| `keys()` | Tüm anahtarları döndürür |
| `values()` | Tüm değerleri döndürür |
| `items()` | Tüm anahtar-değer çiftlerini döndürür |
| `get(key)` | Belirtilen anahtarın değerini döndürür (anahtar yoksa None veya varsayılan) |
| `pop(key)` | Belirtilen anahtarı çıkarır ve değerini döndürür |
| `update(other_dict)` | Diğer sözlüğün elemanlarını ekler |

```python
kisi = {"ad": "Ali", "yaş": 25}

# Anahtarları al
print(kisi.keys())  # dict_keys(['ad', 'yaş'])

# değerleri al
print(kisi.values())  # dict_values(['Ali', 25])

# Anahtar-değer çiftlerini al
print(kisi.items())  # dict_items([('ad', 'Ali'), ('yaş', 25)])

# get ile erişim (anahtar yoksa None döner)
print(kisi.get("ad"))  # Ali
print(kisi.get("mail"))  # None (mail yok)

# get ile varsayılan değer
print(kisi.get("mail", "Yok"))  # Yok

# pop ile çıkarma ve döndürme
çıkarilan_değer = kisi.pop("yaş")
print("Çıkarılan yaş:", çıkarilan_değer)  # 25
print("Kalan sözlük:", kisi)  # {'ad': 'Ali'}
```

### İç İçe Sözlükler

```python
veritabani = {
    "kullanici1": {
        "ad": "Ali",
        "yaş": 25,
        "rol": "admin"
    },
    "kullanici2": {
        "ad": "Ayşe",
        "yaş": 30,
        "rol": "user"
    }
}

# Erişim: veritabani["kullanici1"]["yaş"]
print(veritabani["kullanici1"]["yaş"])  # Çıktı: 25
```

### Sözlük içinde Döngü

```python
for anahtar in kisi:
    print(f"{anahtar}: {kisi[anahtar]}")

# Ya da items ile
for anahtar, değer in kisi.items():
    print(f"{anahtar} -> {değer}")
```

### Sözlük Karşılaştırması

| Özellik | Liste (List) | Sözlük (Dict) |
|---------|-------------|--------------|
| **Erişim Yöntemi** | Indis numarası `[0]` | Anahtar `[ad]` |
| **Sıralı mı?** | ✅ Sıralı (Python 3.7+) | ✅ Sıralı (ekleme sırasına) |
| **Benzersiz mi?** | ❌ Tekrar edilebilir | ✅ Anahtarlar benzersiz |
| **Erişim Hızı** | O(n) | O(1) (genellikle daha hızlı) |
| **Kullanım** | Ordered sequence, sayı listeleri | Anahtar-değer eşlemeleri, JSON gibi |

### Özet

| Konu | Açıklama |
|------|----------|
| **Tanım** | `{anahtar: değer, ...}` ile tanımlanır |
| **Erişim** | `sözlük[anahtar]` ile |
| **Ekleme/Güncelleme** | `sözlük[anahtar] = değer` |
| **Çıkarma** | `pop(anahtar)`, `del sözlük[anahtar]` |
| **Metotlar** | `keys()`, `values()`, `items()`, `get()`, `update()` |
| **Özellik** | Anahtarlar benzersiz, O(1) erişim |

---

**Ödev:** Aşağıdaki kodu yazıp çalıştırmayı deneyin:

```python
# Katalog sistemi oluşturun

katalog = {
    "Ayşe": {"telefon": "555-1111", "eposta": "ayse@test.com"},
    "Mehmet": {"telefon": "555-2222", "eposta": "mehmet@test.com"},
    "Fatma": {"telefon": "555-3333", "eposta": "fatma@test.com"}
}

# 1. Fatma'nın telefon numarasını alın
print("Fatma'nın telefon:", katalog["Fatma"]["telefon"])

# 2. Yeni bir kullanıcı ekleyin
katalog["Kerem"] = {"telefon": "555-4444", "eposta": "kerem@test.com"}

# 3. Katalogdaki tüm isimleri alın
print("Kullanıcı isimleri:", list(katalog.keys()))

# 4. Kerem'in eposta'sini güncelleyin
katalog["Kerem"]["eposta"] = "kerem.yeni@test.com"

# 5. Katalogu yazdırın
for kisi, bilgi in katalog.items():
    print(f"{kisi}: {bilgi['eposta']}")
```