# Python-100-Days: Day 20 — OOP Uygulaması

## Örnek: Poker Oyunu

OOP'yi öğrenmenin en iyi yolu **gerçek dünya projeleri**. Poker oyunu, OOP kavramlarını bir araya getirir.

---

## Adım 1: Enum (Sabit Değerler)

```python
from enum import Enum

class Suite(Enum):
    """Renkler (enum)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)
    # 0: ♠ Maça
    # 1: ♥ Kupa
    # 2: ♣ Sinek
    # 3: ♦ Karo

# Enum kullanımı
for suite in Suite:
    print(f'{suite.name}: {suite.value}')
# SPADE: 0
# HEART: 1
# CLUB: 2
# DIAMOND: 3
```

**Neden Enum?**
- `0` yerine `Suite.SPADE` kullanmak **okunabilirliği** artırır
- Sabit değerleri **gruplandırır**

---

## Adım 2: Kart Sınıfı

```python
class Card:
    """Kart"""
    
    def __init__(self, suite, face):
        self.suite = suite  # Renk
        self.face = face    # Değer (1-13)
    
    def __repr__(self):
        """Kartı string olarak göster"""
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

# Test
card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1)  # ♠5
print(card2)  # ♥K
```

**`__repr__` ne yapar?**
- Objeyi **string** olarak gösterir
- `print(card1)` → `♠5`

---

## Adım 3: Poker Sınıfı

```python
import random

class Poker:
    """Poker"""
    
    def __init__(self):
        # 52 kart oluştur
        self.cards = [Card(suite, face) 
                      for suite in Suite
                      for face in range(1, 14)]
        self.current = 0  # Sıradaki kartın indeksi
    
    def shuffle(self):
        """Karıştır"""
        self.current = 0
        random.shuffle(self.cards)
    
    def deal(self):
        """Kart dağıt"""
        card = self.cards[self.current]
        self.current += 1
        return card
    
    @property
    def has_next(self):
        """Dağıtılacak kart var mı?"""
        return self.current < len(self.cards)

# Test
poker = Poker()
poker.shuffle()
print(poker.cards)  # Karıştırılmış kartlar
```

**`@property` ne yapar?**
- Metodu **özellik** gibi kullanır
- `poker.has_next` → `poker.has_next()` yerine

---

## Adım 4: Oyuncu Sınıfı

```python
class Player:
    """Oyuncu"""
    
    def __init__(self, name):
        self.name = name
        self.hand = []  # Oyuncunun elindeki kartlar
    
    def receive(self, card):
        """Kart al"""
        self.hand.append(card)
    
    def sort_hand(self):
        """Eli sırala"""
        self.hand.sort(key=lambda card: (card.suite.value, card.face))
    
    def show_hand(self):
        """Eli göster"""
        print(f'{self.name}: {" ".join(str(card) for card in self.hand)}')

# Test
player1 = Player('Ali')
player1.receive(Card(Suite.SPADE, 5))
player1.receive(Card(Suite.HEART, 13))
player1.show_hand()  # Ali: ♠5 ♥K
```

---

## Adım 5: Oyunu Birleştirme

```python
# Oyuncular
players = [Player('Ali'), Player('Ayşe'), Player('Mehmet'), Player('Zeynep')]

# Poker
poker = Poker()
poker.shuffle()

# Kartları dağıt
while poker.has_next:
    for player in players:
        if poker.has_next:
            player.receive(poker.deal())

# Elleri göster
for player in players:
    player.sort_hand()
    player.show_hand()
```

---

## Özet Tablo

| Sınıf | Görev | Önemli Metodlar |
|-------|-------|-----------------|
| `Suite` | Renk sabitleri | `Enum` |
| `Card` | Tek kart | `__repr__` |
| `Poker` | 52 kart | `shuffle()`, `deal()`, `has_next` |
| `Player` | Oyuncu | `receive()`, `sort_hand()`, `show_hand()` |

---

## OOP İlişkileri

| İlişki | Açıklama | Örnek |
|--------|----------|-------|
| **is-a** | Kalıtım | `Dog` is-a `Animal` |
| **has-a** | Kompozisyon | `Poker` has-a `Card` |
| **use-a** | Bağımlılık | `Player` use-a `Card` |

---

## Sıradaki Adım

Day 21: Dosya okuma/yazma ve hata yönetimi
