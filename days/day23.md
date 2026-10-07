# Day 23: CSV Dosyaları

CSV (Comma Separated Values) dosyaları, uygulama之间 (veritabanı, elektronik tablo) veri içeri ve dışa aktarımı için kullanılan basit ve yaygın bir dosya biçimidir. CSV dosyaları metin dosyaları olduğundan, hangi işletim sistemde veya hangi programlama dilindeyse işlenebilir.

CSV dosyalarının özellikleri:

1. **Metin dosyası**: [ASCII](https://tr.wikipedia.org/wiki/ASCII), [Unicode](https://tr.wikipedia.org/wiki/Unicode) veya [GB2312](https://tr.wikipedia.org/wiki/GB2312) gibi bir karakter kümesi kullanır.
2. **Kayıtlar**: Typic olarak her satır bir kayıttır.
3. **Alanlar (Sütunlar)**: Her kayıt, bölücü (adaylı olarak virgül, noktalı virgül, sekme gibi) ile alanlara ayrılır.
4. **Aynı Sıralı Alanlar**: Her kayıt aynı sütun sırasına sahiptir.

CSV dosyaları metin düzenleyicisi veya Excel gibi elektronik tablo araçları ile açılabilir ve düzenlenebilir. Çok sayıda veri tabanı sistemi CSV dosyalarına veri aktarma ve veri tabanına aktarma desteği verir.

## CSV Dosyasına Veri Yazma

Beş öğrenci üç sınav puanı verisini bir CSV dosyasına kaydetmek istiyoruz. Bunu Python'un standart `csv` kütüphanesiyle yapabiliriz.

```python
import csv
import random

with open('scores.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['İsim', 'Türkçe', 'Matematik', 'İngilizce'])
    names = ['Ayşe', 'Mehmet', 'Fatma', 'Mustafa', 'Kemal']
    for name in names:
        scores = [random.randrange(50, 101) for _ in range(3)]
        scores.insert(0, name)
        writer.writerow(scores)
```

Oluşan `scores.csv` dosyası içeriği:

```
İsim,Türkçe,Matematik,İngilizce
Ayşe,72,85,68
Mehmet,88,92,75
Fatma,61,70,83
Mustafa,90,78,64
Kemal,55,62,77
```

**Not**: `writer` fonksiyonu `dialect` parametresi ile CSV dosyalarının dialect'ini (örneğin `excel` vb.) belirleyebilir. `delimiter` (Ayırıcı), `quotechar` (Tırnak karakter) ve `quoting` (Tırnaklama şekli) ile ayırıcı ve tırnaklama özelleştirebilirsiniz. Örneğin:

```python
writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_ALL)
```

Bu durumda çıktı şu olur:

```
"İsim"|"Türkçe"|"Matematik"|"İngilizce"
"Ayşe"|"72"|"85"|"68"
"Mehmet"|"88"|"92"|"75"
```

## CSV Dosyasından Veri Okuma

Oluşturduğumuz `scores.csv` dosyasını okumak için `csv.reader` fonksiyonunu kullanabiliriz.

```python
import csv

with open('scores.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for data_list in reader:
        print(reader.line_num, end='\t')
        for elem in data_list:
            print(elem, end='\t')
        print()
```

**Not**: `csvreader` nesnesi üzerinde `for` döngüsü yaparken, her seferinde listedeki tüm alanları içeren bir liste alırsınız.

## `csv.DictReader` ile Dict Formatında Okuma

CSV sütun başlıklarını kullanarak veri okumanın daha kolay yolu `csv.DictReader`dır:

```python
import csv

with open('scores.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"İsim: {row['İsim']}, Notlar: {row['Türkçe']}, {row['Matematik']}, {row['İngilizce']}")
```

## Özet

Python ile veri çalışırken CSV dosyaları sıkça rastlanan bir durumdur. Gelecekte veri analizi yaparken `pandas` kütüphanesini kullanmak isteyebilirsiniz. `pandas` ile:

- `read_csv`: CSV dosyasını okuttur ve verileri bir `DataFrame` objesine dönüştürür.
- `to_csv`: `DataFrame` verisini CSV dosyasına yazar.

`read_csv` ve `to_csv` fonksiyonları, yerel `csv.reader` ve `csv.writer` fonksiyonlarından çok daha güçlüdür ve veri temizleme, dönüştürme ve birleştirme gibi birçok yöntem içerir.

---

**Ödev**: Yukarıdaki örnekleri kendi bilgisayarınızda deneyin. `scores.csv` dosyasını oluşturup, içeriğini okumayı ve `pandas` ile okumasını deneyin (eğer pandas kuruluysa).