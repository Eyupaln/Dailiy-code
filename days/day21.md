# Python-100-Days: Day 21 — Dosya Okuma/Yazma ve Hata Yönetimi

## Dosya İşlemleri Nedir?

**Kalıcılık (Persistence):** Veriyi bellekten (geçici) diske (kalıcı) kaydetme işlemi.

---

## Dosya Açma ve Kapatma

### `open()` Fonksiyonu

```python
file = open('dosya.txt', 'r', encoding='utf-8')
#      │          │      │
#      │          │      └─ karakter kodlaması
#      │          └──────── işlem modu
#      └─────────────────── dosya adı
```

### İşlem Modları

| Mod | Anlam |
|-----|-------|
| `'r'` | Okuma (varsayılan) |
| `'w'` | Yazma (önceki içeriği siler) |
| `'x'` | Yazma (dosya varsa hata verir) |
| `'a'` | Ekleme (sonuna ekle) |
| `'b'` | Binary mod |
| `'t'` | Metin mod (varsayılan) |
| `'+'` | Güncelleme (okuma + yazma) |

---

## Dosya Okuma

### 1. `read()` — Tüm içeriği oku

```python
file = open('dosya.txt', 'r', encoding='utf-8')
print(file.read())  # Tüm içeriği string olarak döndürür
file.close()
```

### 2. `for-in` ile satır satır oku

```python
file = open('dosya.txt', 'r', encoding='utf-8')
for line in file:
    print(line, end='')  # Her satırı yazdır
file.close()
```

### 3. `readlines()` — Satırları listeye al

```python
file = open('dosya.txt', 'r', encoding='utf-8')
lines = file.readlines()  # ['satır1\n', 'satır2\n', ...]
for line in lines:
    print(line, end='')
file.close()
```

---

## Dosya Yazma

### 1. `'w'` modu — Yaz (önceki içeriği siler)

```python
file = open('dosya.txt', 'w', encoding='utf-8')
file.write('Merhaba Dünya!\n')
file.write('Python öğreniyorum.\n')
file.close()
```

### 2. `'a'` modu — Ekle (sonuna ekle)

```python
file = open('dosya.txt', 'a', encoding='utf-8')
file.write('Yeni satır.\n')
file.close()
```

---

## `with` İfadesi (Önerilen)

**Neden?** Dosyayı otomatik kapatır, hata olsa bile.

```python
# with ile (otomatik kapanır)
with open('dosya.txt', 'r', encoding='utf-8') as file:
    print(file.read())
# file.close() gerekmez!
```

---

## Hata Yönetimi

### `try/except` Yapısı

```python
try:
    file = open('dosya.txt', 'r', encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print("Dosya bulunamadı!")
except PermissionError:
    print("Dosya erişim izni yok!")
finally:
    file.close()  # Her durumda kapat
```

### `try/except/else/finally`

```python
try:
    # Hata oluşturabilecek kod
    file = open('dosya.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    # Hata olursa
    print("Dosya bulunamadı!")
else:
    # Hata olmazsa
    print(file.read())
finally:
    # Her durumda
    file.close()
```

---

## Özet Tablo

| İşlem | Kod | Not |
|-------|-----|-----|
| **Okuma** | `open('f.txt', 'r')` | Varsayılan mod |
| **Yazma** | `open('f.txt', 'w')` | Önceki içeriği siler |
| **Ekleme** | `open('f.txt', 'a')` | Sonuna ekle |
| **with** | `with open(...) as f:` | Otomatik kapanır |
| **Hata** | `try/except` | Hata yönetimi |

---

## Sıradaki Adım

Day 22: JSON ve API kullanımı
