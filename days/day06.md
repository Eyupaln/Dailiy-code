# Day 05: Döngüler (Loops)

## Döngüler Neden Gerekli?

Tek tek tekrarlayan işlemleri otomatikleştirmek için döngüler kullanılır. Python'da iki ana döngü türü vardır: `for` ve `while`.

### 1. For Döngüsü

Bir sequence (sıra dizisi) üzerinde dönemek için kullanılır. Genellikle listeler, dizgeler (strings) veya `range()` fonksiyonu ile kullanılır.

```python
# Listenin her elemanını yazdırma
liste = ["elma", "armut", "kiwi"]

for urun in liste:
    print(urun)
```

#### `range()` Fonksiyonu

```python
# 0'dan 4'e kadar (5' dahil değil)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Belirli bir baslangic ve bitis
for i in range(2, 6):  # 2, 3, 4, 5
    print(i)

# Stap (artış miktarı)
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)
```

#### For Döngüsü ile Listeler

```python
notlar = [85, 90, 78, 92, 88]

# Her notu yazdırma ve geçme/kalma durumunu kontrol etme
for not in notlar:
    if not >= 60:
        print(f"Geçti: {not}")
    else:
        print(f"Kaldı: {not}")
```

### 2. While Döngüsü

Belirtilen koşul doğru olduğu sürece çalışan sonsuz döngü olabilecek için dikkatli kullanılmalı koşul her zaman değiştirilmelidir.

```python
i = 0
while i < 5:
    print(i)
    i += 1  # i = i + 1 (artırma) - KOŞULU DEĞIŞTİRMELİSİZ DÖNGÜ SONSUZ OLUR!
```

#### `break` ve `continue` Komutları

```python
# break: Döngüyü anında sonlandır
for i in range(10):
    if i == 5:
        break  # Döngüyü kes, 5'ten sonra hiçbir şey yazmaz
    print(i)

# continue: Şu iterasyonu atla, sonraki iterasyona geç
for i in range(5):
    if i == 2:
        continue  # 2'yi atla, 1, 3, 4 yaz
    print(i)
```

### Örnek: 1'den 100'e Kadar Sayıların Toplamı

```python
toplam = 0
i = 1

while i <= 100:
    toplam += i  # toplam = toplam + i
    i += 1       # i = i + 1

print("1'den 100'e kadar toplam:", toplam)
```

### Örnek: Kullanıcıdan Girdi Alınkya Çıkma

```python
print("=== Sayı Tahmin Oyunu ===")
bilgi_secret = 7
tahmin = None

while tahmin != bilgi_secret:
    tahmin = int(input("1 ile 10 arasında bir sayı tahmin et: "))
    
    if tahmin < bilgi_secret:
        print("Daha büyük bir sayı dene!")
    elif tahmin > bilgi_secret:
        print("Daha küçük bir sayı dene!")
    else:
        print("Tebrikler! Doğru tahmin ettiniz!")
```

## Özet

| Konu | Açıklama |
|------|----------|
| **For Döngüsü** | Sequence'ler üzerinde iteration |
| **Range()** | 0-aralıklı sayı dizisi oluşturma |
| **While Döngüsü** | Koşul doğru olduğu sürece |
| **Break** | Döngüyü anında sonlandır |
| **Continue** | Şu iterasyonu atla |

---

**Ödev:** Aşağıdaki kodu yazıp çalıştırmayı deneyin:

```python
print("1'den 10'a kadar çift sayılar:")

# for döngüsü ile çift sayıları yazdırma
for i in range(2, 11, 2):  # 2'den 10'a kadar 2'şer artarak
    print(i, end=" ")  # Satır sonu boşlukla bitir

print()  # Yeni satır atla

# while döngüsü ile 1-10 arasındaki tek sayıların toplamı
toplam = 0
i = 1
while i <= 10:
    if i % 2 == 1:  # Tek sayı kontrolü
        toplam += i
    i += 1
print("1-10 arasındaki tek sayıların toplamı:", toplam)
```