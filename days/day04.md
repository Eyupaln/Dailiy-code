# Day 04: İşlem ve Veri Tipleri

## Aritmetik İşlemler

Python'da temel aritmetik işlemler şunlardır:

| İşlem | İşleci | Örnek | Sonuç |
|-------|--------|-------|-------|
| Toplama | `+` | `2 + 3` | `5` |
| Çıkarma | `-` | `5 - 2` | `3` |
| Çarpım | `*` | `3 * 4` | `12` |
| Bölüm | `/` | `7 / 2` | `3.5` (float) |
| Tam Bölüm | `//` | `7 // 2` | `3` (int) |
| Mod (Kalan) | `%` | `7 % 2` | `1` |
| Üs alma | `**` | `2 ** 3` | `8` |

```python
a = 10
b = 3

print("Toplama:", a + b)
print("Çıkarma:", a - b)
print("Çarpım:", a * b)
print("Bölüm (float):", a / b)
print("Bölüm (int):", a // b)
print("Kalan:", a % b)
print("Üs:", a ** b)
```

## Karşılaştırma İşlemleri (Comparison Operators)

Değerleri karşılaştırmak için kullanılır, sonuç her zaman `True` veya `False` olur.

| İşlem | İşleci | Açıklama | Örnek | Sonuç |
|-------|--------|----------|-------|-------|
| Eşit | `==` | Eşitlik kontrolü | `2 == 2` | `True` |
| Farklı | `!=` | Farklı kontrolü | `2 != 3` | `True` |
| Küçük | `<` | Küçük kontrolü | `2 < 3` | `True` |
| Büyük | `>` | Büyük kontrolü | `3 > 2` | `True` |
| Küçük eşit | `<=` | Küçük eşit kontrolü | `2 <= 2` | `True` |
| Büyük eşit | `>=` | Büyük eşit kontrolü | `3 >= 2` | `True` |

```python
x = 5
y = 10

print("x < y:", x < y)  # True
print("x > y:", x > y)  # False
print("x == y:", x == y)  # False
print("x != y:", x != y)  # True
print("x <= y:", x <= y)  # True
```

## Mantıksal İşlemler (Logical Operators)

Birden fazla koşulu bir arada test etmek için kullanılır.

| İşlem | İşleci | Açıklama | Örnek | Sonuç |
|-------|--------|----------|-------|-------|
| Ve | `and` | Her iki şart da true ise | `True and True` | `True` |
| Veya | `or` | En az biri true ise | `True or False` | `True` |
| Değil | `not` | Mantıksızını tersine çevirir | `not True` | `False` |

```python
yaş = 20
egitimi_var = True

# Koşullu ifade
if yaş >= 18 and egitimi_var:
    print("Yetişkin ve eğitim gören")
elif yaş < 18 or not egitimi_var:
    print("Yetişkin değil veya eğitim yok")
else:
    print("Diğer durum")
```

## Atama İşlemleri

Değişkene değer atamak ve aynı anda işlem yapmak için kullanılır.

| İşlem | İşleci | Açıklama | Örnek | Sonuç |
|-------|--------|----------|-------|-------|
| Atama | `=` | Değer atama | `x = 5` | `x = 5` |
| Toplama atama | `+=` | Artırma | `x += 3` | `x = x + 3` (x = 8) |
| Çıkarma atama | `-=` | Azaltma | `x -= 3` | `x = x - 3` |
| Çarpma atama | `*=` | Çarpma | `x *= 3` | `x = x * 3` |
| Bölme atama | `/=` | Bölme | `x /= 3` | `x = x / 3` |

```python
x = 10

x += 5  # x = x + 5 -> x = 15
print("x += 5 sonrası:", x)

x *= 2  # x = x * 2 -> x = 30
print("x *= 2 sonrası:", x)
```

## Özet

| Konu | Açıklama |
|------|----------|
| **Aritmetik** | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| **Karşılaştırma** | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| **Mantıksal** | `and`, `or`, `not` |
| **Atama** | `=`, `+=`, `-=`, `*=`, `/=` |
| **Öncelik** | `**` > `*`/`/` > `+`/`-` > `and`/`or` |

---

**Ödev:** Aşağıdaki kodu yazıp çalıştırmayı deneyin ve sonucu tahmin edin:

```python
x = 15
y = 4

print("Bölüm:", x / y)
print("Tam bölüm:", x // y)
print("Kalan:", x % y)
print("Üs:", x ** y)

# Koşul kontrolü
if x > y and x % y == 0:
    print("x, y' ye tam bölunüyor ve x büyüktür")
else:
    print("Koşul sağlanmadı")
```