# Python-100-Days: Day 16 — İleri Fonksiyonlar

## Neden "İleri" Fonksiyonlar?

Python'da fonksiyonlar **"birinci sınıf" (first-class)** varlıklardır:
- Değişkene atanabilir
- Fonksiyon parametresi olarak geçilebilir
- Fonksiyon dönüş değeri olabilir

Buna **higher-order functions** denir.

---

## Higher-Order Functions

### Fonksiyonu Parametre Olarak Geçirme

```python
def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

print(calc(0, add, 1, 2, 3, 4, 5))  # 15
print(calc(1, mul, 1, 2, 3, 4, 5))  # 120
```

**Önemli:** Fonksiyonu parametre olarak geçerken **parantez koyma**! `add` yaz, `add()` değil.

---

## Lambda Fonksiyonları

Lambda, **anonim (isimsiz)** fonksiyon oluşturur:

```python
# Normal fonksiyon
def add(x, y):
    return x + y

# Lambda fonksiyonu
add = lambda x, y: x + y

print(add(3, 5))  # 8
```

### Lambda Kullanım Alanları

```python
# Map ile
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums))
print(squares)  # [1, 4, 9, 16, 25]

# Filter ile
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]

# Sorted ile
words = ['apple', 'pie', 'a', 'banana']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # ['a', 'pie', 'apple', 'banana']
```

---

## Map, Filter, Reduce

### Map — Her elemana uygula

```python
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums))
print(squares)  # [1, 4, 9, 16, 25]
```

### Filter — Filtrele

```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6]
```

### Reduce — İndirge

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)  # 120
```

---

## Sorted — Sıralama

```python
words = ['apple', 'pie', 'a', 'banana']

# Alfabetik sıralama
print(sorted(words))  # ['a', 'apple', 'banana', 'pie']

# Uzunluğa göre sıralama
print(sorted(words, key=len))  # ['a', 'pie', 'apple', 'banana']

# Ters sıralama
print(sorted(words, reverse=True))  # ['pie', 'banana', 'apple', 'a']
```

---

## Özet Tablo

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
