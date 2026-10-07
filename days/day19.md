# Python-100-Days: Day 19 — OOP İleri

## Görünürlük ve Özellik Dekoratörleri

### Özel Özellikler (`__`)

```python
class Student:
    def __init__(self, name, age):
        self.__name = name  # Özel özellik
        self.__age = age    # Özel özellik

    def study(self, course_name):
        print(f'{self.__name} {course_name} dersi çalışıyor.')

stu = Student('Ali', 20)
stu.study('Python')  # Ali Python dersi çalışıyor.
print(stu.__name)  # AttributeError: 'Student' object has no attribute '__name'
```

**Not:** `__` ile başlayan özellikler **özel**dir, dışarıdan erişilemez. Ama sınıf içinden `self.__name` ile erişilebilir.

---

## Dinamik Özellikler

Python **dinamik** bir dildir. Nesnelere **dinamik** özellikler ekleyebilirsin:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Student('Ali', 20)
stu.sex = 'Erkek'  # Dinamik özellik ekleme
print(stu.sex)  # Erkek
```

### `__slots__` ile Sınırlama

```python
class Student:
    __slots__ = ('name', 'age')  # Sadece bu özelliklere izin ver

    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Student('Ali', 20)
stu.sex = 'Erkek'  # AttributeError: 'Student' object has no attribute 'sex'
```

---

## Statik Metotlar ve Sınıf Metotları

### Statik Metot (`@staticmethod`)

```python
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """Üçgen oluşturulup oluşturulmayacağını kontrol et"""
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

# Statik metot çağırma (nesne olmadan)
if Triangle.is_valid(3, 4, 5):
    t = Triangle(3, 4, 5)
    print(f'Çevre: {t.perimeter()}')  # 12
    print(f'Alan: {t.area()}')        # 6.0
```

**Önemli:** Statik metotlar `self` kullanmaz, sınıf adıyla çağrılır.

---

## Özet Tablo

| Konu | Açıklama | Örnek |
|------|----------|-------|
| **Özel özellik** | `__` ile başlar, dışarıdan erişilemez | `self.__name` |
| **Dinamik özellik** | Nesneye sonradan eklenebilir | `stu.sex = 'Erkek'` |
| **`__slots__`** | Özellikleri sınırlar | `__slots__ = ('name', 'age')` |
| **Statik metot** | `self` kullanmaz, sınıf adıyla çağrılır | `@staticmethod` |
| **Sınıf metodu** | `cls` kullanır, sınıf adıyla çağrılır | `@classmethod` |

---

## Sıradaki Adım

Day 20: OOP pratiği
