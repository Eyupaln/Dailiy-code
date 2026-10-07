# Day 08: Diziler (Lists)

## Diziler (Lists) Nedir?

Diziler, sıralı bir koleksiyon veriyi tutmak için kullanılır. Python'da diziler `[ ]` köşeli parantezlerle tanımlanır ve listedeki öğelere indis (index) numarası ile erişilir.

### Dizinin Oluşturulması

```python
# Boş bir liste
liste = []

# Elemanlar ile birlikte oluşturulmuş liste
günler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]

# Farklı veri tiplerine sahip liste
karisik = [1, "Ali", 3.14, True, "Python"]
```

### Diziye Eleman Ekleme

```python
# Eleman ekle (sonsa)
günler.append("Cumartesi")

# Belirli bir indekse ekle
günler.insert(1, "Pazar")

# Belirli sayıda eleman ekle (liste ile)
extra = ["Ödev", "Sınav"]
günler.extend(extra)
```

### Diziden Eleman Çıkarma

```python
# Belirli indekden çıkar
çıkalan = günler.pop(2)  # 2. indek'ten çıkar ve değişkene at

# Belirli değeri çıkar (ilk eşleşme)
günler.remove("Pazartesi")

# Slicing ile bölümleme
alt_kısma = günler[1:3]  # İndeks 1 ve 2'yi al (Salı, Çarşamba)
```

### Dizinin Uzunluğu ve Elemanlarına Erişim

```python
print("Liste uzunluğu:", len(günler))

# İlk elemana erişme (indis 0)
ilk = günler[0]

# Son elemana erişme (indis -1)
son = günler[-1]

# Belirli bir indeks
üçüncü = günler[2]
```

### Döngüyle Diziyi Gezinme

```python
for gün in günler:
    print("Bugün", gün, "çalışıyor")
```

### Dizideki Eleman Sıralama ve Arama

```python
# Sıralama (küçükten büyüğe)
siralı = sorted(günler)

# Ters sıralama
ters = sorted(günler, reverse=True)

# Belirli bir elemanın indeksi
index = günler.index("Pazartesi")

# Elemanın var olup olmadığı kontrolü
if "Cuma" in günler:
    print("Cuma günü mevcut")
```

### Liste Listesi (İç İçe Diziler)

```python
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# İç içe dizilere erişim
print("Matrisin 2. satırı, 3. sütunu:", matris[1][2])
```

### Liste Metotlarının Özeti

| Metot | Açıklama |
|-------|----------|
| `append(x)` | Liste sonuna x ekler |
| `extend(L)` | Listenin sonuna Llistenin tüm elemanlarını ekler |
| `insert(i, x)` | i. indekse x ekler |
| `pop(i)` | i. indek'ten eleman çıkarır ve döndürür (i belirtilmezse son eleman) |
| `remove(x)` | Listenin ilk occurrences'ını x siler |
| `clear()` | Listenin tüm elemanlarını sil |
| `count(x)` | x'ın listenede kaç kez tekrarlandığını döndürür |
| `index(x)` | x'ın ilk indeksini döndürür |
| `sort()` | Listeyi sıralar (varsayılan: artan) |
| `reverse()` | Listenin terini tersine döndürür |
| `copy()` | Listenin kopyasını döndürür |

## Özet

| Konu | Açıklama |
|------|----------|
| **Liste Tanımı** | `[ ]` ile tanımlanır |
| **Erişim** | Indis numarası ile `[0]`, `[-1]` gibi |
| **Eleman Ekleme** | `append()`, `insert()`, `extend()` |
| **Eleman Çıkarma** | `pop()`, `remove()`, `clear()` |
| **Döngü** | `for` ile iterate etme |
| **Slicing** | `[başlangıç:bitiş]` ile bölümleme |
| **Sıralama** | `sort()`, `sorted()` |

---

**Ödev:** Aşağıdaki kodu yazıp çalıştırmayı deneyin:

```python
# Bir ürün listedesi oluşturun
ürünler = ["Laptop", "Telefon", "Tablet", "Saat"]

# 1. Ürünü listeye ekleyin
ürünler.append("Buzdolabı")

# 2. Listenin 2. elemanını (index 1) alın
print("2. Ürün:", ürünler[1])

# 3. Listenin sonundaki öğeyi çıkarıp yazdırın
çıkaran = ürünler.pop()
print("Çıkarılan:", çıkaran)

# 3. Listenin elemanlarını yazdırın
print("Güncel Liste:", ürünler)

# 4. Listenin uzunluğunu yazdırın
print("Toplam ürün sayısı:", len(ürünler))

# 5. Ters sıralı liste oluşturun
tersListe = ürünler[::-1]
print("Ters Liste:", tersListe)
```