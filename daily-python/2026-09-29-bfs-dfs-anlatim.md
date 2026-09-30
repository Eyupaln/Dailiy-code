# BFS ve DFS — Detaylı Anlatım

## Ağaç Yapısı Nedir?

Ağaç, **düğümler (nodes)** ve **kenarlar (edges)** ile bağlanan bir veri yapısıdır.

```
    1      ← Kök (root)
   / \
  2   3    ← Çocuklar (children)
 / \
4   5      ← Yapraklar (leaves)
```

- **Kök (root):** En üstteki düğüm (`1`)
- **Çocuk (child):** Bir düğümün altındaki düğümler (`2` ve `3`, `1`'in çocukları)
- **Yaprak (leaf):** Çocuğu olmayan düğüm (`4` ve `5`)

---

## Python'da Ağaç Oluşturma

### Node Sınıfı

```python
class Node:
    def __init__(self, value):
        self.value = value      # Düğümün değeri
        self.children = []      # Çocukların listesi
```

**Açıklama:**
- `value`: Düğümün sakladığı değer (örn: `1`, `2`, `3`)
- `children`: Bu düğümün çocuklarının listesi (boş liste = yaprak)

### Ağaç Oluşturma

```python
# Kök düğüm
root = Node(1)

# Kök'ün çocukları
root.children = [Node(2), Node(3)]

# 2'nin çocukları
root.children[0].children = [Node(4), Node(5)]
```

**Adım adım:**

1. `root = Node(1)` → `1` değerinde bir düğüm oluştur
2. `root.children = [Node(2), Node(3)]` → `1`'in çocukları `2` ve `3`
3. `root.children[0].children = [Node(4), Node(5)]` → `2`'nin çocukları `4` ve `5`

**Not:** `root.children[0]` → `2` düğümüne erişir

---

## BFS (Breadth-First Search) — Genişlik Öncelikli

### Nasıl Çalışır?

BFS, **seviyeye seviye** ilerler:

1. Önce kökü ziyaret et
2. Sonra kökün tüm çocuklarını ziyaret et
3. Sonra onların çocuklarını ziyaret et
4. Bu şekilde devam et

### Sıralama

```
    1
   / \
  2   3
 / \
4   5
```

**BFS Sırası:** `1 → 2 → 3 → 4 → 5`

### Hangi Veri Yapısı?

BFS **Queue (kuyruk)** kullanır.

**Queue nasıl çalışır?**
- **FIFO** (First In, First Out) — İlk giren, ilk çıkar
- Banka sırası gibi: Ahmet önce geldi, Ahmet önce çıkar

### Kod

```python
from collections import deque

def bfs(root):
    queue = deque([root])  # Queue'ya kökü ekle
    
    while queue:  # Queue boş olana kadar
        node = queue.popleft()  # Queue'dan çıkar (önce gelen)
        print(node.value, end=" ")  # Değeri yazdır
        
        for child in node.children:
            queue.append(child)  # Çocukları queue'ya ekle
```

### Adım Adım İzleme

| Adım | Queue | Çıkarılan | Yazdırılan |
|------|-------|-----------|------------|
| 1 | `[1]` | `1` | `1` |
| 2 | `[2, 3]` | `2` | `2` |
| 3 | `[3, 4, 5]` | `3` | `3` |
| 4 | `[4, 5]` | `4` | `4` |
| 5 | `[5]` | `5` | `5` |
| 6 | `[]` | — | biter |

**Çıktı:** `1 2 3 4 5`

---

## DFS (Depth-First Search) — Derinlik Öncelikli

### Nasıl Çalışır?

DFS, **bir dalı sonuna kadar** izler, sonra diğer dala geçer:

1. Kökü ziyaret et
2. İlk çocuğa git
3. Onun ilk çocuğuna git
4. Yapulağa ulaşınca geri dön
5. Diğer dala geç

### Sıralama

```
    1
   / \
  2   3
 / \
4   5
```

**DFS Sırası:** `1 → 2 → 4 → 5 → 3`

### Hangi Veri Yapısı?

DFS **Stack (yığın)** kullanır.

**Stack nasıl çalışır?**
- **LIFO** (Last In, First Out) — Son giren, ilk çıkar
- Tabak yığını gibi: Son gelen tabak, alınır

### Kod

```python
def dfs(root):
    stack = [root]  # Stack'e kökü ekle
    
    while stack:  # Stack boş olana kadar
        node = stack.pop()  # Stack'ten çıkar (son gelen)
        print(node.value, end=" ")  # Değeri yazdır
        
        for child in reversed(node.children):
            stack.append(child)  # Çocukları stack'e ekle
```

### Adım Adım İzleme

| Adım | Stack | Çıkarılan | Yazdırılan |
|------|-------|-----------|------------|
| 1 | `[1]` | `1` | `1` |
| 2 | `[2, 3]` | `2` | `2` |
| 3 | `[4, 5, 3]` | `4` | `4` |
| 4 | `[5, 3]` | `5` | `5` |
| 5 | `[3]` | `3` | `3` |
| 6 | `[]` | — | biter |

**Çıktı:** `1 2 4 5 3`

---

## BFS vs DFS Karşılaştırma

| Özellik | BFS | DFS |
|---------|-----|-----|
| **Yöntem** | Seviye seviye | Derinlik öncelikli |
| **Veri yapısı** | Queue (FIFO) | Stack (LIFO) |
| **Sıra** | `1 2 3 4 5` | `1 2 4 5 3` |
| **Kullanım** | En kısa yol, seviye bulma | Yol bulma, labirent çözme |

---

## Özet

- **Ağaç:** Düğümler ve kenarlar ile bağlanan veri yapısı
- **BFS:** Queue kullanır, seviyeye seviye ilerler
- **DFS:** Stack kullanır, derinlik öncelikli ilerler
- **Queue:** FIFO (ilk giren, ilk çıkar)
- **Stack:** LIFO (son giren, ilk çıkar)

---

## Sıradaki Adım

Binary Search Trees (BST) — Ağaçların özel bir türü, sıralı veri saklar.
