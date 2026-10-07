# Python-100-Days: Day 15 — Fonksiyon Pratikleri

## Örnek 1: Rastgele Doğrulama Kodu

```python
import random
import string

ALL_CHARS = string.digits + string.ascii_letters

def generate_code(*, code_len=4):
    """
    Belirtilen uzunlukta rastgele doğrulama kodu üretir
    :param code_len: Kod uzunluğu (varsayılan 4)
    :return: Rastgele kod string'i
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))

# Test
for _ in range(5):
    print(generate_code())
```

**Önemli noktalar:**
- `string.digits` → `'0123456789'`
- `string.ascii_letters` → `'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'`
- `random.choices()` → **tekrarlı** örnekleme (aynı eleman birden kez seçilebilir)
- `random.sample()` → **tekrarsız** örnekleme
- `*, code_len=4` → **sadece keyword** parametre (pozisyonel olarak geçilemez)

---

## Örnek 2: Asal Sayı Kontrolü

```python
def is_prime(num: int) -> bool:
    """
    Bir sayının asal olup olmadığını kontrol eder
    :param num: 1'den büyük pozitif tam sayı
    :return: Asal ise True, değilse False
    """
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test
print(is_prime(7))   # True
print(is_prime(10))  # False
```

**Önemli noktalar:**
- `num: int` → parametre tipi **type hint** (kod okunabilirliği için)
- `-> bool` → dönüş değeri tipi
- `int(num ** 0.5) + 1` → kareköküne kadar kontrol yeterli
- Neden? Eğer `n = a × b` ise, `a` veya `b` mutlaka `√n`'den küçük veya eşit olmalı.

---

## Örnek 3: EBOB ve EKOK

```python
def gcd(x: int, y: int) -> int:
    """
    İki sayının en büyük ortak bölenini hesaplar (Euclidean algoritması)
    """
    while y % x != 0:
        x, y = y % x, x
    return x

def lcm(x: int, y: int) -> int:
    """
    İki sayının en küçük ortak katını hesaplar
    """
    return x * y // gcd(x, y)

# Test
print(gcd(12, 8))   # 4
print(lcm(12, 8))   # 24
```

**Önemli noktalar:**
- **Euclidean algoritması:** `gcd(x, y) = gcd(y % x, x)`
- **EKOK formülü:** `lcm(x, y) = x * y // gcd(x, y)`
- İki fonksiyon **ayrı** tasarlanmalı (tek fonksiyon yapmaz)

---

## Özet Tablo

| Özellik | Açıklama |
|---------|----------|
| `*, param` | Sadece keyword parametre |
| `param: int` | Type hint (okunabilirlik) |
| `-> bool` | Dönüş değeri tipi |
| `random.choices()` | Tekrarlı örnekleme |
| `random.sample()` | Tekrarsız örnekleme |
| `gcd` | Euclidean algoritması |
| `lcm` | `x * y // gcd(x, y)` |

---

## Sıradaki Adım

Day 16: İleri fonksiyonlar (lambda, map, filter)
