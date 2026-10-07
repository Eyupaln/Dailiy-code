# Day 05: Şart İfadeleri (if-elif-else)

## Karar Mekanizması

Programlarda farklı koşullara göre farklı işlemler yapmak için `if`, `elif`, `else` yapıları kullanılır.

### Temel Yapı

```python
if koşul1:
    # koşul1 doğruysa çalışır
    print("Koşul 1 sağlandı")
elif koşul2:
    # koşul1 yanlış ve koşul2 doğruysa çalışır
    print("Koşul 2 sağlandı")
else:
    # Hiçbir koşul sağlanmadıysa çalışır
    print("Hiçbir koşul sağlanmadı")
```

### Örnek: Yaşa Göre Kategori Belirleme

```python
yaş = int(input("Yaşınızı girin: "))

if yaş < 0:
    print("Yaş negatif olamaz!")
elif yaş < 18:
    print("Gençsiniz")
elif yaş < 65:
    print("işgüçlisiniz")
else:
    print("Elder"  
```

### Koşullu İfadeler ( ternary operator )

Tek satırda if-else yazmak için kullanılır:

```python
yaş = 20
status = "Yetişkin" if yaş >= 18 else "Genç"
print(status)  # Çıktı: Yetişkin
```

### Birden Fazla Koşul

```python
puan = int(input("Puanınızı girin: "))

if puan >= 90:
    print("AA")
elif puan >= 80:
    print("BA")
elif puan >= 70:
    print("BB")
elif puan >= 60:
    print("CB")
elif puan >= 50:
    print("CC")
else:
    print("FF")
```

### İç İçe Koşullar

```python
yaş = int(input("Yaşınızı girin: "))
ehliyet_var = input("Ehliyetiniz var mı? (e/h): ")

if yaş >= 18:
    if ehliyet_var.lower() == "e":
        print("Ehliyet alabilirsiniz")
    else:
        print("Öncelikle ehliyet alın")
else:
    print("Yaşınız henüz 18'i geçmedi")
```

## Özet

| Konu | Açıklama |
|------|----------|
| **if** | Koşul gerçekleşirse çalışır |
| **elif** | Başka bir koşulu test et |
| **else** | Hiçbir koşul sağlanmazsa |
| **Ternary** | Tek satır if-else |
| **İç içe** | Bir if'in içinde başka if |

---

**Ödev:** Aşağıdaki kodu yazıp çalıştırmayı deneyin:

```python
print("=== Sınav Geçme Sistemi ===")
puan = int(input("Dönem puanınızı girin: "))

if puan >= 50:
    print("Tebrikler! Sınavı geçtiniz.")
    print("ortalama", puan)
    
    # Başarı seviyesi
    if puan >= 80:
        print("Başarıyla geçtiniz!")
    elif puan >= 70:
        print("Orta geçtiniz")
    else:
        print("Başarı geçtim ama çok iyi değil")
else:
    print("Üzülüceksiniz, sınavı tuttunuz.")
    print("Tekrar deneyin!")
```