"""Day 23: Python CSV Dosyaları - Pratik Uygulamalar"""

import csv
import random
import os

print("=" * 50)
print("Day 23: Python CSV Dosyaları")
print("=" * 50)

# ==========================================
# 1. CSV Dosyası Oluşturma Örneği
# ==========================================
print("\n--- 1. CSV Dosyası Oluşturma ---")

with open('ornek_scores.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['İsim', 'Türkçe', 'Matematik', 'İngilizce'])
    names = ['Ayşe', 'Mehmet', 'Fatma', 'Mustafa', 'Kemal']
    for name in names:
        scores = [random.randrange(50, 101) for _ in range(3)]
        scores.insert(0, name)
        writer.writerow(scores)

print("✅ 'ornek_scores.csv' dosyası oluşturuldu.")
print("\nDosya içeriği:")
with open('ornek_scores.csv', 'r', encoding='utf-8') as f:
    print(f.read())

# ==========================================
# 2. CSV Dosyasını Okuma Örneği (csv.reader)
# ==========================================
print("\n--- 2. CSV Dosyasını Okuma (csv.reader) ---")

with open('ornek_scores.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    print("Satır numarası ve içerikleri:")
    for data_list in reader:
        print(f"Satır {reader.line_num}: {data_list}")

# ==========================================
# 3. CSV Dosyasını Okuma Örneği (csv.DictReader)
# ==========================================
print("\n--- 3. CSV Dosyasını Okuma (csv.DictReader) ---")

with open('ornek_scores.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    print("Dict formatında okuma:")
    for row in reader:
        print(f"İsim: {row['İsim']}, Notlar: {row['Türkçe']}, {row['Matematik']}, {row['İngilizce']}")

# ==========================================
# 4. CSV Dosyasına Satır Ekleme
# ==========================================
print("\n--- 4. CSV Dosyasına Satır Ekleme ---")

# Mevcut dosyaya veri ekleme (append mode)
with open('ornek_scores.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Sali', 70, 80, 75])

print("✅ 'Sali' ekli.")
print("\nGüncellenmiş dosya içeriği:")
with open('ornek_scores.csv', 'r', encoding='utf-8') as f:
    print(f.read())

# ==========================================
# 5. Pandas ile CSV İşlemleri (İsteğe bağlı)
# ==========================================
print("\n--- 5. Pandas ile CSV Okuma (Özelliğe bağlı) ---")

try:
    import pandas as pd
    df = pd.read_csv('ornek_scores.csv')
    print("DataFrame ile okuma başarılı!")
    print(df)
    print("\nOrtalama notlar:")
    print(df.mean(numeric_only=True))
except ImportError:
    print("⚠️ Pandas kütüphanesi yüklü değil. Atlanıyor.")
    print("Yüklemek için: pip install pandas")

# ==========================================
# Temizlik
# ==========================================
print("\n" + "=" * 50)
print("Day 23 işlemleri tamamlandı.")
print("Oluşan dosyalar: ornek_scores.csv")
print("=" * 50)