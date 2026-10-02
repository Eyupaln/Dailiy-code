# 1 Ekim 2026 - Egzersiz
# Kurallar:
# 1. Önce yorum satırıyla ne yapacağını yaz
# 2. Altına kodu yaz
# 3. Çalıştırıp testlerini print ile kontrol et
# 4. Takılırsan 10 dakika dene, sonra bana yaz

# ============================================================
# Poker Oyunu - OOP Uygulaması
# ============================================================

from enum import Enum  # Enum sınıfını içe aktar (sabit değerler için)
import random  # Rastgele sayı üretmek için (karıştırma)

# ============================================================
# Adım 1: Renkler (Enum)
# ============================================================
# Enum, sabit değerleri gruplandırmak için kullanılır.
# Örneğin: 0 yerine Suite.SPADE kullanmak okunabilirliği artırır.

class Suite(Enum):
    # Renkler (enum)
    # range(4) → 0, 1, 2, 3 değerlerini oluşturur
    # SPADE=0, HEART=1, CLUB=2, DIAMOND=3
    SPADE, HEART, CLUB, DIAMOND = range(4)
    # ♠ Maça → 0
    # ♥ Kupa → 1
    # ♣ Sinek → 2
    # ♦ Karo → 3

# Tüm renkleri yazdır (test için)
for suite in Suite:
    print(f'{suite.name}:{suite.value}')
    # suite.name → "SPADE", "HEART", ...
    # suite.value → 0, 1, 2, 3

# ============================================================
# Adım 2: Kart Sınıfı
# ============================================================
# Her kartın bir rengi ve bir değeri vardır.
# Örneğin: ♠ A (Maça As), ♥ K (Kupa Kral)

class Card:
    # Kart
    def __init__(self, suite, face):
        # self: kartın kendisi
        # suite: kartın reği (Suite.SPADE, Suite.HEART, ...)
        # face: kartın değeri (1-13, 1=A, 11=J, 12=Q, 13=K)
        self.suite = suite  # Renk
        self.face = face    # Değer

    def __repr__(self):
        # Objeyi string olarak gösterir
        # print(card1) → "♠ A"
        suites = '♠♥♣♦'  # Renk sembolleri
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # faces[1] = 'A', faces[11] = 'J', faces[12] = 'Q', faces[13] = 'K'
        return f'{suites[self.suite.value]} {faces[self.face]}'
        # self.suite.value → 0-3 (renk indeksi)
        # self.face → 1-13 (değer indeksi)

    def puan(self):
        # Kartın puanını hesaplar
        # A → 14 puan (en yüksek)
        # K → 13, Q → 12, J → 11
        # Diğer kartlar → kendi değeri (10 → 10, 2 → 2)
        kart_puani = 14 if self.face == 1 else self.face
        # Eğer face == 1 (As) ise 14, değilse face değerini kullan

        # Renk bonusu: ♠=4, ♥=3, ♣=2, ♦=1
        # suite.value: 0 (SPADE), 1 (HEART), 2 (CLUB), 3 (DIAMOND)
        # 4 - 0 = 4 (SPADE), 4 - 1 = 3 (HEART), ...
        bonus = 4 - self.suite.value

        return kart_puani + bonus
        # Toplam puan = kart değeri + renk bonusu

# Test kartları
card1 = Card(Suite.SPADE, 3)   # ♠ 3
card2 = Card(Suite.HEART, 6)   # ♥ 6
print(card1)  # ♠ 3
print(card2)  # ♥ 6
print(f'{card1} puanı: {card1.puan()}')  # ♠ 3 puanı: 7 (3 + 4)
print(f'{card2} puanı: {card2.puan()}')  # ♥ 6 puanı: 9 (6 + 3)

# ============================================================
# Adım 3: Poker Sınıfı
# ============================================================
# 52 kart oluşturur, karıştırır ve dağıtır

class Poker:
    # Poker
    def __init__(self):
        # 52 kart oluştur (4 renk × 13 değer)
        self.cards = [Card(suite, face)
                      for suite in Suite      # 4 renk
                      for face in range(1, 14)]  # 13 değer (1-13)
        self.current = 0  # Sıradaki kartın indeksi

    def shuffle(self):
        # Kartları karıştır
        self.current = 0  # Başa dön
        random.shuffle(self.cards)  # Listeyi rastgele karıştır

    def deal(self):
        # Sıradaki kartı dağıt
        card = self.cards[self.current]  # Mevcut kartı al
        self.current += 1  # Sonraki karta geç
        return card  # Kartı döndür

    @property
    # Metodu özellik gibi kullanır
    # poker.has_next → poker.has_next() yerine
    def has_next(self):
        # Dağıtılacak kart var mı?
        return self.current < len(self.cards)
        # current < 52 ise True, değilse False

# Poker test
poker = Poker()
poker.shuffle()
print(f'Toplam kart: {len(poker.cards)}')  # 52

# ============================================================
# Adım 4: Oyuncu Sınıfı
# ============================================================
# Her oyuncunun bir adı ve bir eli (kart listesi) vardır

class Player:
    def __init__(self, name):
        # Oyuncu oluştur
        self.name = name    # Oyuncunun adı
        self.hand = []      # Oyuncunun elindeki kartlar (boş liste)

    def receive(self, card):
        # Kart al
        self.hand.append(card)  # Kartı ele ekle

    def sort_hand(self):
        # Eli sırala (renge göre, sonra değere göre)
        self.hand.sort(key=lambda card: (card.suite.value, card.face))
        # lambda card: (card.suite.value, card.face)
        # → önce renge, sonra değere göre sırala

    def show_hand(self):
        # Eli göster
        print(f'{self.name}: {" ".join(str(card) for card in self.hand)}')
        # " ".join(...) → kartları boşlukla birleştir

    def skor(self):
        # Skoru hesapla
        return sum(card.puan() for card in self.hand)
        # sum(...) → tüm kartların puanlarını topla

# ============================================================
# Adım 5: Oyunu Oyna
# ============================================================

# Oyuncuları oluştur
players = [Player('Ali'), Player('Ayşe'), Player('Mehmet'), Player('Zeynep')]

# Poker oluştur ve karıştır
poker = Poker()
poker.shuffle()

# Kartları dağıt (her oyuncuya 13 kart)
while poker.has_next:  # Dağıtılacak kart olduğu sürece
    for player in players:  # Her oyuncuya
        if poker.has_next:  # Hala kart varsa
            player.receive(poker.deal())  # Kart dağıt

# Elleri sırala ve göster
for player in players:
    player.sort_hand()  # Eli sırala
    player.show_hand()  # Eli göster

# Skorları hesapla ve göster
print("\n--- Skorlar ---")
for player in players:
    print(f'{player.name}: {player.skor()} puan')

# Kazanani belirle
kazanan = max(players, key=lambda p: p.skor())
print(f'\nKazanan: {kazanan.name} ({kazanan.skor()} puan)!')
