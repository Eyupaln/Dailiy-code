# Day 10: Demetler (Tuples)

## Demetler (Tuples) Nedir?

Demetler, sıralı ve **değiştirilemez** (immutable) koleksiyonlardır. Listeler `[ ]` ile tanımlanırken, demetler `( )` ile tanımlanır.

### Demet Tanımı

```python
# Boş bir demet
boş_demet = ()

# Elemanlar ile birlikte oluşturulmuş demet
renkler = ("Kırmızı", "Yeşil", "Mavi")

# Farklı veri tiplerine sahip demet
karisik = (1, "Ali", 3.14, True)
```

### Demetlere Erişim

Demetlere indisi ile erişilir, aynı şekilde listelerde kullanılır:

```python
renkler = ("Kırmızı", "Yeşil", "Mavi")

# İlk elemana erişme
print(renkler[0])  # Çıktı: Kırmızı

# Son elemana erişme
print(renkler[-1])  # Çıktı: Mavi

# Dilimleme (slicing)
print(renkler[1:3])  # Çıktı: ('Yeşil', 'Mavi')
```

### Demet Özellikleri

| Özellik | Demet (Tuple) | Liste (List) |
|---------|--------------|--------------|
| **Değiştirilebilirlik** | ❌ Değiştirilemez (immutable) | ✅ Değiştirilebilir (mutable) |
| **Sözdizimi** | `(eleman1, eleman2)` | `[eleman1, eleman2]` |
| **Erişim** | Indis numarası ile | Indis numarası ile |
| **Ölçek** | Listeye göre daha az bellek kullanır | Daha fazla bellek kullanır |

### Demetlerde Döngü

```python
for renk in renkler:
    print(renk)
```

### Demet Metotları

Demetler çok az metot içerir çünkü değiştirilemezler:

| Metot | Açıklama |
|-------|----------|
| `count(x)` | Demette x'ın kaç kez tekrarlandığını döndürür |
| `index(x)` | x'ın ilk indeksini döndürür |

```python
sayilar = (1, 2, 3, 2, 4, 2)
print(sayilar.count(2))  # Çıktı: 3 (iki üç kez var)
print(sayilar.index(3))  # Çıktı: 2 (3' ün ilk indeksi)
```

### Demet ve Fonksiyonlar

Fonksiyonlara demet geçirilebilir ve fonksiyonundan demet döndürilebilir:

```python
def nokta_olustur(x, y):
    """Nokta demeti oluşturur"""
    return (x, y)

# Kullanım
nokta = nokta_olustur(5, 10)
print(nokta)  # Çıktı: (5, 10)

# Demetin elemanlarına erişim
print("X koordinatı:", nokta[0])  # Çıktı: 5
print("Y koordinatı:", nokta[1])  # Çıktı: 10
```

### Demetin Avantajları

1. **Bellek Verimliliği**: Listeye göre daha az bellek kullanır
2. **Veri Koruması**: Değiştirilemez olduğu verinin kodu kırılmasını önler
3. **Anahtar Olarak Kullanılabilir**: Listeler anahtar olarak kullanılamaz, demetler kullanılabilir

```python
# List anahtar olarak kullanılamaz (hata!)
# mapping = {[1, 2]: "değer"}  # TypeError

# Demet anahtar olarak kullanılamaz
mapping = {(1, 2): "değer"}  # ✅ Çalışır
print(mapping)  # {(1, 2): "değer"}
```

### Demet Veya Liste - Ne Zaman Hangisini Kullanmalı?

| Durum | Tercih Edilen |
|-------|--------------|
| Değişecek veriler | `list` |
| Değişmeyecek, sabit veriler | `tuple` |
| Fonksiyon çıktısı | `tuple` (değiştirilmemeli) |
| Anahtar (dictionary key) | `tuple` |
| Döngüde değiştirme ihtiyacı | `list` |

### Özet

| Konu | Açıklama |
|------|----------|
| **Tanım** | `( )` ile tanımlanır |
| **Değiştirilebilirlik** | Değiştirilemez (immutable) |
| **Erişim** | Indis numarası ile `[0]`, `[-1]` |
| **Slicing** | `[başlangıç:bitiş]` ile |
| **Metotlar** | `count()`, `index()` |
| **Kullanım Alanı** | Sabit veriler, anahtarlar, döngü verileri |

---

**Ödev:** Aşağıdaki kodu yazıp çalıştırmayı deneyin:

```python
# Demet örnekleri

# 1. Bir demet oluşturun
ogrenciler = ("Ali", "Ayşe", "Mehmet", "Fatma")

# 2. Listenin uzunluğunu alın
print("Öğrenci sayısı:", len(ogrenciler))

# 3. İlk öğrenciyi alın
print("Sıra başı:", ogrenciler[0])

# 3. Sondaki öğrenciyi alın
print("Sıra sonu:", ogrenciler[-1])

# 4. Belirli aralıktaki öğrencileri alın
print("İki ile beş arası:", ogrenciler[1:4])

# 5. Demette bir eleman arayın
if "Mehmet" in ogrenciler:
    print("Mehmet listededir")

# 6. Count kullanın
print("Ali'nın sayısı:", ogrenciler.count("Ali"))

# 7. Index kullanın
print("Ayşe'nin indeksi:", ogrenciler.index("Ayşe"))

# 8. Demetle fonksiyon kullanın
def ortalamayı_hesapla(notlar):
    return sum(notlar) / len(notlar)

notlar = (85, 90, 78, 92)
print("Sınıf ortalaması:", ortalamayı_hesapla(notlar))
```