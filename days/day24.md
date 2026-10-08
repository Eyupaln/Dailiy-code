# Day 24: Excel Dosyaları

## Excel Dosyaları Nedir?

**Excel** (Microsoft Excel), veri görselleştirme ve analizi için en yaygın kullanılan elektronik tablo yazılımlarından biridir. Python ile Excel dosyaları çalışmak, veritabanı verilerini veya raporları işlemek için oldukça kullanışlıdır.

Python'da Excel dosyaları ile çalışmak için iki ana kütüphane kullanılır:

1. **`openpyxl`** - .xlsx dosyaları üzerinde çalışmak için (daha detaylı kontrol)
2. **`pandas`** - Veri analizi ve hızlı veri dönüşümleri için (`read_excel`, `to_excel`)

---

## 📦 Kütüphaneler Kurulumu

```bash
# openpyxl için
pip install openpyxl

# pandas için (excel destekli)
pip install pandas openpyxl
```

---

## 1. openpyxl ile Çalışma

`openpyxl` ile .xlsx dosyaları üzerinde célula (hucre) bazında işlem yapabilirsiniz.

### Yeni Bir Excel Dosyası Oluşturma

```python
import openpyxl

# Yeni workbook oluştur
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Müşteriler"

# Başlıklar
ws["A1"] = "ID"
ws["B1"] = "İsim"
ws["C1"] = "Yaş"
ws["D1"] = "Şehir"

# Veri ekleme
ws["A2"] = 1
ws["B2"] = "Ayşe"
ws["C2"] = 28
ws["D2"] = "İstanbul"

ws["A3"] = 2
ws["B3"] = "Mehmet"
ws["C3"] = 35
ws["D3"] = "Ankara"

# Dosyayı kaydetme
wb.save("ornek_musteriler.xlsx")
print("✅ Excel dosyası oluşturuldu: ornek_musteriler.xlsx")
```

### Varolan Bir Excel Dosyasını Okuma

```python
import openpyxl

# Varolan dosyayı açma
wb = openpyxl.load_workbook("ornek_musteriler.xlsx")
ws = wb.active

# Satır sayısını alma
print("Satır sayısı:", ws.max_row)

# Sütun sayısını alma
print("Sütun sayısı:", ws.max_column)

# Hücre verilerine erişim
for row in ws.iter_rows(min_row=1, max_row=ws.max_row, values_only=True):
    print(row)
```

### Hücre Biçimlendirme

```python
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

# Yazı rengi
ws["A1"].font = openpyxl.styles.Font(color="FF0000", bold=True)

# Arka plan rengi
ws["A1"].fill = openpyxl.styles.PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")

# Kalın yazı
ws["A1"].font = openpyxl.styles.Font(bold=True)

# Sütun genişliği ayarlama
ws.column_dimensions["A"].width = 20
ws.column_dimensions["B"].width = 30

wb.save("ornek_birim.png")  # (ufak uyarlama)
```

---

## 2. Pandas ile Excel Çalışma

`pandas` ile Excel dosyalarıyla çalışmak daha hızlı ve veri odaklıdır.

### Excel'den Veri Okuma

```python
import pandas as pd

# Tüm sayfalara okuma
df = pd.read_excel("ornek_musteriler.xlsx")

# Belirli sayfaya okuma
df = pd.read_excel("ornek_musteriler.xlsx", sheet_name="Müşteriler")

# İlk 5 satırı görüntüleme
print(df.head())

# Belirtilen sütunları okuma
df = pd.read_excel("ornek_musteriler.xlsx", usecols=["ID", "İsim", "Yaş"])
```

### Veri Bilgisayarına Yazma

```python
import pandas as pd

# DataFrame oluşturma
veri = {
    "ID": [3, 4],
    "İsim": ["Fatma", "Mustafa"],
    "Yaş": [61, 78],
    "Şehir": ["İzmir", "Bursa"]
}

df = pd.DataFrame(veri)

# Excel'e yazma (varsayılan: ilk sayfa)
df.to_excel("yenidata.xlsx", index=False)

# Belirli bir sayfaya yazma
df.to_excel("yenidata.xlsx", sheet_name="Veriler", index=False)

# Aynı dosyaya ekleme (mode='a')
df.to_excel("yenidata.xlsx", sheet_name="EkData", index=False, startrow=5)
```

### Temel Veri İşlemleri

```python
import pandas as pd

df = pd.read_excel("veriler.xlsx")

# Sütun seçme
print(df["İsim"])

# Filtreleme
gençler = df[df["Yaş"] < 30]

# Sütun ekleme
df["Yaş Artırılmış"] = df["Yaş"] + 5

# Gruplama ve ortalama
ortalama_yaş = df.groupby("Şehir")["Yaş"].mean()
print(ortalama_yaş)
```

---

## 📊 Özet: openpyxl vs Pandas

| Özellik | openpyxl | Pandas |
|---------|----------|--------|
| **Kullanım Amacı** | Hücre düzeyinde işler, formatlama | Veri analitiği, toplu işlem |
| **Dosya Formatı** | Sadece .xlsx | .xlsx, .xls ve diğer formatlar |
| **Erişim Yöntemi** | Hücre referansı (A1, B2, vb.) | DataFrame (satır/sütun) |
| **Formatlama** | Geliş renk, font, border | Limited formatting |
| **Hız** | Küçük dosyalar için yeterli | Büyük veri setleri için daha hızlı |
| **Önerilen Kullanım** | Rapolar, formatlı dosyalar, özel layout | Veri analitiği, CSV'den dönüşüm, hesaplamalar |

---

## 💡 Pratik Uygulama

Aşağıdaki örnekte `openpyxl` ve `pandas`ogether kullanarak bir rapor oluşturuyoruz:

```python
import openpyxl
import pandas as pd
from openpyxl.styles import Font

# 1. Pandas ile veriyi işleme
df = pd.DataFrame({
    "Ürün": ["Laptop", "Telefon", "Tablet"],
    "Fiyat": [5000, 3000, 2000],
    "Stok": [10, 25, 15]
})

# 2. Excel'e yazma
df.to_excel("urun_raporu.xlsx", index=False)

# 2. openpyxl ile formatlama
wb = openpyxl.load_workbook("urun_raporu.xlsx")
ws = wb.active

# Başlık satırını bold yap
for cell in ws[1]:
    cell.font = Font(bold=True)

# Sütun genişliklerini ayarla
ws.column_dimensions["A"].width = 25
ws.column_dimensions["B"].width = 15
ws.column_dimensions["C"].width = 15

# Kaydetme
wb.save("urun_raporu_düzenli.xlsx")

print("✅ Rapor oluşturuldu: urun_raporu_düzenli.xlsx")
```

---

## 📝 Ödev

Aşağıdaki işlemleri yapın:

1. **openpyxl** ile aşağıdaki verileri `veriler.xlsx` adlı bir dosyaya yazın:

| ID | Ad | Yaş | Şehir |
|----|-----|-----|-------|
| 1 | Ayşe | 28 | İstanbul |
| 2 | Mehmet | 35 | Ankara |
| 3 | Fatma | 61 | İzmir |

2. **Pandas** ile dosyayı okup, sadece `Ad` ve `Yaş` sütunlarını alın ve ekrana yazdırın.

3. **openpyxl** ile dosyadaki **"Ayşe"** satırının Yaş değerini 29 olarak güncelleyin ve kaydedin.

---

## 🔑 Önemli Hatırlatmalar

1. **openpyxl** sadece **.xlsx** formatını destekler, eski **.xls** için `xlrd` kütüphanesi gerekebilir.
2. **Pandas** `read_excel` ile okurken `engine='openpylex'` hatası alırsanız, `pip install openpyxl` emin olun.
3. **index=False** parametresi ile Excel'e yazarken satır numaralarını (0, 1, 2...) dosyaya yazmamış olursunuz.
4. **Her gün günlük logunuzu** `2026-10-*.md` formatında kaydetmeyi sürdürün!

---