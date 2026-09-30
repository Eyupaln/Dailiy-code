# Karışık Quiz — Tüm Konular

## Soru 1: Binary Search + String

```python
def binary_search_string(dizi, hedef):
    left, right = 0, len(dizi) - 1
    while left <= right:
        mid = (left + right) // 2
        if dizi[mid] == hedef:
            return mid
        elif dizi[mid] < hedef:
            left = mid + 1
        else:
            right = mid - 1
    return -1

dizi = ["ali", "ayse", "fatma", "mehmet", "zeynep"]
print(binary_search_string(dizi, "mehmet"))
```

Bu kodun çıktısı nedir?

- A) `0`
- B) `2`
- C) `3`
- D) `4`

---

## Soru 2: Bitwise + Fonksiyon

```python
def gizli_islem(a, b):
    return (a & b) | (a ^ b)

print(gizli_islem(5, 3))
```

Bu kodun çıktısı nedir?

- A) `1`
- B) `6`
- C) `7`
- D) `8`

---

## Soru 3: BFS + Graf

```python
from collections import deque

def bfs(graf, baslangic):
    ziyaret = set()
    queue = deque([baslangic])
    sira = []
    
    while queue:
        dugum = queue.popleft()
        if dugum not in ziyaret:
            ziyaret.add(dugum)
            sira.append(dugum)
            for komsu in graf[dugum]:
                if komsu not in ziyaret:
                    queue.append(komsu)
    return sira

graf = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
print(bfs(graf, 'A'))
```

Bu kodun çıktısı nedir?

- A) `['A', 'B', 'C', 'D']`
- B) `['A', 'B', 'D', 'C']`
- C) `['A', 'C', 'B', 'D']`
- D) `['A', 'C', 'D', 'B']`

---

## Soru 4: BST + Recursive

```python
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search(node, value):
    if node is None:
        return False
    if node.value == value:
        return True
    if value < node.value:
        return search(node.left, value)
    return search(node.right, value)

root = BSTNode(10)
root.left = BSTNode(5)
root.right = BSTNode(15)
root.left.left = BSTNode(3)
root.left.right = BSTNode(7)

print(search(root, 7))
```

Bu kodun çıktısı nedir?

- A) `True`
- B) `False`
- C) `None`
- D) Hata verir

---

## Soru 5: String + Set

```python
s = "Merhaba Dünya"
kelimeler = s.split()
print(set(kelimeler))
```

Bu kodun çıktısı nedir?

- A) `{'Merhaba', 'Dünya'}`
- B) `['Merhaba', 'Dünya']`
- C) `{'M', 'e', 'r', 'h', 'a', 'b', ' ', 'D', 'ü', 'n', 'y'}`
- D) `('Merhaba', 'Dünya')`

---

## Soru 6: Dict + Fonksiyon

```python
def sayi_sozluk(liste):
    sozluk = {}
    for sayi in liste:
        if sayi in sozluk:
            sozluk[sayi] += 1
        else:
            sozluk[sayi] = 1
    return sozluk

print(sayi_sozluk([1, 2, 2, 3, 3, 3]))
```

Bu kodun çıktısı nedir?

- A) `{1: 1, 2: 2, 3: 3}`
- B) `{1: 1, 2: 1, 3: 1}`
- C) `{1: 3, 2: 2, 3: 1}`
- D) `{1: 1, 2: 2, 3: 3, 4: 4}`

---

## Soru 7: Bitwise + BST

```python
def tek_mi(n):
    return n & 1 == 1

def bst_tek_sayilar(root):
    if root is None:
        return []
    sonuc = []
    if tek_mi(root.value):
        sonuc.append(root.value)
    sonuc += bst_tek_sayilar(root.left)
    sonuc += bst_tek_sayilar(root.right)
    return sonuc

root = BSTNode(10)
root.left = BSTNode(5)
root.right = BSTNode(15)
root.left.left = BSTNode(3)
root.left.right = BSTNode(7)

print(bst_tek_sayilar(root))
```

Bu kodun çıktısı nedir?

- A) `[5, 3, 7, 15]`
- B) `[10, 5, 15, 3, 7]`
- C) `[5, 15, 3, 7]`
- D) `[10, 5, 15]`

---

## Soru 8: Graf + Dict

```python
graf = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def derece(graf, dugum):
    return len(graf[dugum])

print(derece(graf, 'A'))
```

Bu kodun çıktısı nedir?

- A) `1`
- B) `2`
- C) `3`
- D) `4`

---

## Soru 9: String + Bitwise

```python
def tek_harf_mi(s):
    sonuc = 0
    for harf in s:
        sonuc ^= ord(harf)
    return sonuc

print(tek_harf_mi("hello"))
```

Bu kodun çıktısı nedir?

- A) `0`
- B) `104`
- C) `101`
- D) `108`

---

## Soru 10: BFS + String

```python
from collections import deque

def bfs_string(graf, baslangic):
    ziyaret = set()
    queue = deque([baslangic])
    sira = []
    
    while queue:
        dugum = queue.popleft()
        if dugum not in ziyaret:
            ziyaret.add(dugum)
            sira.append(dugum)
            for komsu in graf[dugum]:
                if komsu not in ziyaret:
                    queue.append(komsu)
    return ''.join(sira)

graf = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a', 'd'],
    'd': ['b', 'c']
}
print(bfs_string(graf, 'a'))
```

Bu kodun çıktısı nedir?

- A) `"abcd"`
- B) `"abdc"`
- C) `"acbd"`
- D) `"acdb"`

---

## Cevaplarını Yaz

10 soruya cevaplarını yaz (A, B, C veya D), ben kontrol edeyim!
