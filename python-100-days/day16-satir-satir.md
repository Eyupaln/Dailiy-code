# Day 16 — Satır Satır Açıklama

## Örnek 1: Higher-Order Function

```python
def calc(init_value, op_func, *args, **kwargs):
    # init_value: başlangıç değeri (örn: 0 veya 1)
    # op_func: işlem fonksiyonu (örn: add veya mul)
    # *args: pozisyonel parametreler
    # **kwargs: keyword parametreler
    
    items = list(args) + list(kwargs.values())
    # args: (1, 2, 3, 4, 5) → list(args) → [1, 2, 3, 4, 5]
    # kwargs: {} → list(kwargs.values()) → []
    # items: [1, 2, 3, 4, 5]
    
    result = init_value
    # result: 0 (başlangıç değeri)
    
    for item in items:
        # item: 1, 2, 3, 4, 5 (sırayla)
        
        if type(item) in (int, float):
            # item int veya float mı? Evet!
            
            result = op_func(result, item)
            # op_func: add ise → result = add(result, item)
            # op_func: mul ise → result = mul(result, item)
    
    return result
    # Sonucu döndür

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

print(calc(0, add, 1, 2, 3, 4, 5))  # 15
# calc(0, add, 1, 2, 3, 4, 5)
# result = 0
# result = add(0, 1) = 1
# result = add(1, 2) = 3
# result = add(3, 3) = 6
# result = add(6, 4) = 10
# result = add(10, 5) = 15

print(calc(1, mul, 1, 2, 3, 4, 5))  # 120
# calc(1, mul, 1, 2, 3, 4, 5)
# result = 1
# result = mul(1, 1) = 1
# result = mul(1, 2) = 2
# result = mul(2, 3) = 6
# result = mul(6, 4) = 24
# result = mul(24, 5) = 120
```

---

## Örnek 2: Lambda Fonksiyonları

```python
# Normal fonksiyon
def add(x, y):
    return x + y

# Lambda fonksiyonu (aynı şey)
add = lambda x, y: x + y
# lambda x, y: x + y
# │      │    │
# │      │    └─ dönüş değeri
# │      └────── parametreler
# └───────────── lambda anahtar kelimesi

print(add(3, 5))  # 8
```

---

## Örnek 3: Map

```python
nums = [1, 2, 3, 4, 5]

# Map: Her elemana fonksiyon uygular
squares = list(map(lambda x: x ** 2, nums))
# map(lambda x: x ** 2, nums)
# │   │               │
# │   │               └─ iterable (üzerinde dolaşılacak)
# │   └───────────────── her elemana uygulanacak fonksiyon
# └───────────────────── map fonksiyonu

# Adım adım:
# 1 → 1² = 1
# 2 → 2² = 4
# 3 → 3² = 9
# 4 → 4² = 16
# 5 → 5² = 25

print(squares)  # [1, 4, 9, 16, 25]
```

---

## Örnek 4: Filter

```python
nums = [1, 2, 3, 4, 5, 6]

# Filter: Koşulu sağlayan elemanları filtreler
evens = list(filter(lambda x: x % 2 == 0, nums))
# filter(lambda x: x % 2 == 0, nums)
# │      │                   │
# │      │                   └─ iterable
# │      └───────────────────── koşul fonksiyonu
# └──────────────────────────── filter fonksiyonu

# Adım adım:
# 1 → 1 % 2 == 0? False → elenir
# 2 → 2 % 2 == 0? True → kalır
# 3 → 3 % 2 == 0? False → elenir
# 4 → 4 % 2 == 0? True → kalır
# 5 → 5 % 2 == 0? False → elenir
# 6 → 6 % 2 == 0? True → kalır

print(evens)  # [2, 4, 6]
```

---

## Örnek 5: Reduce

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]

# Reduce: İndirger (iki elemanı al, işlem yap, sonraki elemanla devam et)
product = reduce(lambda x, y: x * y, nums)
# reduce(lambda x, y: x * y, nums)
# │       │                   │
# │       │                   └─ iterable
# │       └───────────────────── işlem fonksiyonu
# └───────────────────────────── reduce fonksiyonu

# Adım adım:
# x=1, y=2 → 1*2 = 2
# x=2, y=3 → 2*3 = 6
# x=6, y=4 → 6*4 = 24
# x=24, y=5 → 24*5 = 120

print(product)  # 120
```

---

## Örnek 6: Sorted

```python
words = ['apple', 'pie', 'a', 'banana']

# Sorted: Sıralar
print(sorted(words))
# ['a', 'apple', 'banana', 'pie'] (alfabetik)

# key=len: Uzunluğa göre sırala
print(sorted(words, key=len))
# key=len → her elemanın uzunluğunu hesapla
# 'a' → 1
# 'pie' → 3
# 'apple' → 5
# 'banana' → 6
# Sırala: ['a', 'pie', 'apple', 'banana']

# reverse=True: Ters sırala
print(sorted(words, reverse=True))
# ['pie', 'banana', 'apple', 'a']
```

---

## Özet

| Fonksiyon | Ne Yapar | Örnek |
|-----------|----------|-------|
| `map(f, iterable)` | Her elemana `f` uygular | `map(lambda x: x**2, nums)` |
| `filter(f, iterable)` | `f` koşulunu sağlayanları filtreler | `filter(lambda x: x%2==0, nums)` |
| `reduce(f, iterable)` | İndirger | `reduce(lambda x, y: x*y, nums)` |
| `sorted(iterable, key=f)` | Sıralar | `sorted(words, key=len)` |
| `lambda x: x**2` | Anonim fonksiyon | `lambda x: x + 1` |

---

## Sıradaki Adım

Day 17: Dekoratörler ve recursion
