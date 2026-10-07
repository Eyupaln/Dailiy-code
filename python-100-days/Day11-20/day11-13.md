# Python-100-Days: Day 11-13 Toplu Anlatım

## Day 11: Stringler (Karakter Dizileri)

### Temel Kavramlar

```python
s1 = 'hello, world!'
s2 = "你好，世界！"
s3 = '''çok satırlı
string'''
```

### Kaçış Karakterleri

| Karakter | Anlam |
|----------|-------|
| `\n` | Yeni satır |
| `\t` | Tab |
| `\\` | Ters slash |
| `\'` | Tek tırnak |
| `\"` | Çift tırnak |

### Raw String

```python
s1 = 'hello\n'      # \n = yeni satır
s2 = r'hello\n'     # \n = \ ve n (raw string)
```

### String Operatörleri

```python
s1 = 'hello' + ', ' + 'world'   # Birleştirme
s2 = '!' * 3                     # Tekrarlama
s3 = 'hello' in s1               # Arama (True/False)
s4 = s1[0]                       # İndeksleme (h)
s5 = s1[0:5]                     # Dilimleme (hello)
```

### Önemli String Metodları

```python
s = 'Hello, World!'

s.upper()        # 'HELLO, WORLD!'
s.lower()        # 'hello, world!'
s.find('World')  # 7 (indeks)
s.replace('World', 'Python')  # 'Hello, Python!'
s.split(', ')     # ['Hello', 'World!']
s.strip()        # Baş/son boşlukları temizler
```

---

## Day 12: Set'ler (Kümeler)

### Temel Kavramlar

Set, **sırasız ve benzersiz** elemanlardan oluşan koleksiyon.

```python
s1 = {1, 2, 3, 4, 5}
s2 = set([1, 2, 3, 4, 5])
s3 = set()  # Boş set
```

### Set Operatörleri

```python
a = {1, 2, 3}
b = {2, 3, 4}

a | b  # Birleşim: {1, 2, 3, 4}
a & b  # Kesişim: {2, 3}
a - b  # Fark: {1}
a ^ b  # Simetrik fark: {1, 4}
```

### Set Metodları

```python
s = {1, 2, 3}

s.add(4)           # Eleman ekle
s.remove(2)        # Eleman sil (hata verir yoksa)
s.discard(5)       # Eleman sil (hata vermez yoksa)
s.pop()            # Rastgele eleman sil
s.clear()          # Tüm elemanları sil
```

### Set Kullanım Alanları

- **Benzersiz elemanlar:** `list(set(liste))`
- **Üyelik testi:** `x in s` (O(1) hızı)
- **Küme işlemleri:** Birleşim, kesişim, fark

---

## Day 13: Dict'ler (Sözlükler)

### Temel Kavramlar

Dict, **anahtar-değer (key-value)** çiftlerinden oluşan koleksiyon.

```python
d1 = {'name': 'Ali', 'age': 25}
d2 = dict(name='Ali', age=25)
d3 = {}  # Boş dict
```

### Dict Operatörleri

```python
d = {'name': 'Ali', 'age': 25}

d['name']          # 'Ali' (değer erişim)
d['city'] = 'İstanbul'  # Yeni anahtar-değer ekle
d['age'] = 26       # Değer güncelle
del d['age']        # Anahtar-değer sil
```

### Dict Metodları

```python
d = {'name': 'Ali', 'age': 25}

d.keys()      # Tüm anahtarlar
d.values()    # Tüm değerler
d.items()     # Tüm anahtar-değer çiftleri
d.get('name') # 'Ali' (anahtar yoksa None döner)
d.get('city', 'Yok')  # 'Yok' (varsayılan değer)
d.pop('age')  # 'age' anahtarını sil ve değerini döndür
d.clear()     # Tüm elemanları sil
```

### Dict Kullanım Alanları

- **Hızlı arama:** `d[key]` — O(1) hızı
- **Veri yapısı:** JSON, veritabanı kayıtları
- **Sayma:** `{'a': 1, 'b': 2, 'a': 3}` → `{'a': 3, 'b': 2}`

---

## Karşılaştırma Tablosu

| Özellik | List | Set | Dict |
|---------|------|-----|------|
| **Sıralı** | ✅ | ❌ | ✅ (Python 3.7+) |
| **Benzersiz** | ❌ | ✅ | ✅ (anahtarlar) |
| **Değiştirilebilir** | ✅ | ✅ | ✅ |
| **Arama hızı** | O(n) | O(1) | O(1) |
| **Kullanım** | Genel | Benzersiz elemanlar | Anahtar-değer |

---

## Özet

- **String:** Karakter dizileri, metin işleme
- **Set:** Benzersiz elemanlar, küme işlemleri
- **Dict:** Anahtar-değer çiftleri, hızlı arama

---

## Sıradaki Adım

Day 14: Fonksiyonlar ve modüller
