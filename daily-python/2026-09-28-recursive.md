# Recursive Binary Search — Adım Adım Anlatım

## Recursive Fonksiyon Nedir?

**Recursive fonksiyon**, kendini çağıran bir fonksiyondur. İki şartı vardır:

1. **Base case (durma koşulu):** Fonksiyonun durması için. Yoksa sonsuz döngüye girer.
2. **Recursive case:** Fonksiyonun kendini çağırması, her seferinde base case'e yaklaşarak.

---

## Basit Örnek: Geri Sayma

```python
def geri_say(n):
    if n == 0:  # Base case: dur!
        print("0!")
        return
    
    print(n)
    geri_say(n - 1)  # Recursive case: kendini çağır

geri_say(3)
```

**Çıktı:**
```
3
2
1
0!
```

**Nasıl çalışır?**
1. `geri_say(3)` → `3` yazdır, `geri_say(2)` çağır
2. `geri_say(2)` → `2` yazdır, `geri_say(1)` çağır
3. `geri_say(1)` → `1` yazdır, `geri_say(0)` çağır
4. `geri_say(0)` → `0!` yazdır, **dur** (base case)
5. Tüm çağrılar geri döner

---

## Recursive Binary Search

### Base Case'ler

1. `left > right` → hedef bulunamadı, `-1` döndür
2. `dizi[mid] == hedef` → hedef bulundu, `mid` döndür

### Recursive Case'ler

- `dizi[mid] < hedef` → sağ yarıya git: `binary_search(dizi, hedef, mid + 1, right)`
- `dizi[mid] > hedef` → sol yarıya git: `binary_search(dizi, hedef, left, mid - 1)`

---

## Kod

```python
def binary_search_recursive(dizi, hedef, left, right):
    # Base case 1: hedef bulunamadı
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # Base case 2: hedef bulundu
    if dizi[mid] == hedef:
        return mid
    
    # Recursive case 1: hedef sağ yarıda
    elif dizi[mid] < hedef:
        return binary_search_recursive(dizi, hedef, mid + 1, right)
    
    # Recursive case 2: hedef sol yarıda
    else:
        return binary_search_recursive(dizi, hedef, left, mid - 1)


# Test
dizi = [3, 5, 8, 9]
hedef = 8
sonuc = binary_search_recursive(dizi, hedef, 0, len(dizi) - 1)
print(f"Hedef {hedef}, indeks: {sonuc}")
```

---

## Adım Adım İzleme

`dizi = [3, 5, 8, 9]`, `hedef = 8`

| Tur | left | right | mid | dizi[mid] | Karar |
|-----|------|-------|-----|-----------|-------|
| 1 | 0 | 3 | 1 | 5 | 5 < 8 → sağa git |
| 2 | 2 | 3 | 2 | 8 | 8 == 8 → bulundu! |

**Sonuç:** `2`

---

## Özet

- **Iteratif:** `while` döngüsü kullanır
- **Recursive:** Fonksiyon kendini çağırır, `left` ve `right` parametre olarak geçirilir

İkisi de aynı mantığı kullanır, sadece farklı yazım biçimleri vardır.
