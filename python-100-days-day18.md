# Python-100-Days: Day 18 — OOP Giriş

## OOP Nedir?

**Object-Oriented Programming (Nesne Tabanlı Programlama):**
- **Veri** ve **veri üzerinde işlem yapan fonksiyonlar** bir mantıksal bütündür
- Bu bütüne **nesne (object)** denir
- Nesneler **mesaj** alabilir ve işlem yapabilir

---

## Sınıf ve Nesne

| Kavram | Açıklama | Örnek |
|--------|----------|-------|
| **Sınıf (class)** | Soyut kavram, şablon | `Student` |
| **Nesne (object)** | Somut varlık, örnek | `stu1 = Student()` |

**Basit örnek:**
```python
class Student:
    def study(self, course_name):
        print(f'Öğrenci {course_name} dersi çalışıyor.')

    def play(self):
        print(f'Öğrenci oyun oynuyor.')

# Nesne oluşturma
stu1 = Student()
stu2 = Student()

# Mesaj gönderme (metod çağırma)
stu1.study('Python')  # Öğrenci Python dersi çalışıyor.
stu2.play()           # Öğrenci oyun oynuyor.
```

---

## `__init__` Metodu

Nesneyi **başlatır** ve **özellikler** ekler:

```python
class Student:
    def __init__(self, name, age):
        # self: nesnenin kendisi
        # name, age: parametreler
        self.name = name  # özellik
        self.age = age    # özellik

    def study(self, course_name):
        print(f'{self.name} {course_name} dersi çalışıyor.')

    def play(self):
        print(f'{self.name} oyun oynuyor.')

# Nesne oluşturma
stu1 = Student('Ali', 20)
stu2 = Student('Ayşe', 22)

# Mesaj gönderme
stu1.study('Python')  # Ali Python dersi çalışıyor.
stu2.play()           # Ayşe oyun oynuyor.
```

---

## `self` Nedir?

`self`, **nesnenin kendisini** temsil eder:

```python
class Student:
    def __init__(self, name, age):
        self.name = name  # self.name = nesnenin name özelliği
        self.age = age    # self.age = nesnenin age özelliği

    def study(self, course_name):
        # self.name = nesnenin name özelliğine erişim
        print(f'{self.name} {course_name} dersi çalışıyor.')
```

**Önemli:** `self` parametresi **otomatik** olarak geçirilir, sen göndermezsin.

---

## Özet Tablo

| Kavram | Açıklama | Örnek |
|--------|----------|-------|
| **Sınıf** | Şablon, soyut | `class Student:` |
| **Nesne** | Somut varlık | `stu1 = Student()` |
| **Metod** | Nesnenin davranışı | `def study(self):` |
| **`self`** | Nesnenin kendisi | `self.name` |
| **`__init__`** | Başlatma metodu | `def __init__(self, name):` |
| **Özellik** | Nesnenin verisi | `self.name = name` |

---

## Sıradaki Adım

Day 19: OOP ileri (kalıtım, çok biçimlilik)
