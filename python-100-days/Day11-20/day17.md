# Python-100-Days: Day 17 — Dekoratörler ve Recursion

## Dekoratör Nedir?

Dekoratör, **bir fonksiyonu sarmalayan** fonksiyondur. Fonksiyonu değiştirmeden yeni özellikler ekler.

### Basit Örnek

```python
def dekoratör(func):
    def wrapper():
        print("Başlangıç")
        func()
        print("Bitiş")
    return wrapper

@dekoratör
def selamla():
    print("Merhaba!")

selamla()
# Çıktı:
# Başlangıç
# Merhaba!
# Bitiş
```

**`@dekoratör` ne yapar?**
- `selamla = dekoratör(selamla)` anlamına gelir
- `selamla` artık `wrapper` fonksiyonu olur

---

## Pratik Örnek: Zaman Ölçümü

```python
import time

def record_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} çalıştı: {end - start:.2f} saniye')
        return result
    return wrapper

@record_time
def hesapla():
    time.sleep(1)
    print("Hesaplandı")

hesapla()
# Çıktı:
# Hesaplandı
# hesapla çalıştı: 1.00 saniye
```

---

## Dekoratör Yapısı

```python
def dekoratör(func):
    # func: dekoratörlenen fonksiyon
    
    def wrapper(*args, **kwargs):
        # *args, **kwargs: tüm parametreleri al
        
        # Önce ekstra işlemler
        result = func(*args, **kwargs)
        # Sonra ekstra işlemler
        
        return result
    
    return wrapper
```

**Önemli noktalar:**
- `wrapper` fonksiyonu `*args, **kwargs` ile tüm parametreleri alır
- `func(*args, **kwargs)` ile orijinal fonksiyonu çağırır
- `result` döndürür

---

## Recursion (Özyineleme)

Fonksiyonun **kendini çağırması**.

### Faktoriyel Örneği

```python
def faktoriyel(n):
    if n == 0:  # Durma koşulu
        return 1
    return n * faktoriyel(n - 1)  # Recursive çağrı

print(faktoriyel(5))  # 120
```

**Adım adım:**
```
faktoriyel(5) = 5 * faktoriyel(4)
              = 5 * 4 * faktoriyel(3)
              = 5 * 4 * 3 * faktoriyel(2)
              = 5 * 4 * 3 * 2 * faktoriyel(1)
              = 5 * 4 * 3 * 2 * 1 * faktoriyel(0)
              = 5 * 4 * 3 * 2 * 1 * 1
              = 120
```

---

## Recursion Kuralları

1. **Durma koşulu (base case):** Fonksiyonun durması için
2. **Recursive case:** Fonksiyonun kendini çağırması
3. **İlerleme:** Her çağrıda durma koşuluna yaklaşma

### Örnek: Fibonacci

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # 8
```

---

## Özet Tablo

| Konu | Önemli Noktalar |
|------|-----------------|
| **Dekoratör** | `@dekoratör` → `func = dekoratör(func)` |
| **Wrapper** | `*args, **kwargs` ile tüm parametreleri al |
| **Recursion** | Kendini çağıran fonksiyon |
| **Base case** | Durma koşulu |
| **Recursive case** | Kendini çağıran kısım |

---

## Sıradaki Adım

Day 18: OOP giriş
