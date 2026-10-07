# Python-100-Days: Day 22 — JSON ve API Kullanımı

## JSON Nedir?

**JSON (JavaScript Object Notation):** İnsan tarafından okunabilir, hafif bir **veri değişim formatı**.

- Anahtar-değer çiftlerinden oluşur
- Web API'lerinin çoğunda veri bu formatta gelir/gider
- Python'da `json` modülü ile çalışılır (ekstra kurulum gerekmez, yerleşiktir)

```json
{
  "isim": "Eyüp",
  "yas": 25,
  "diller": ["Python", "JavaScript"],
  "aktif": true
}
```

---

## JSON ↔ Python Dönüşümü

### JSON → Python: `json.loads()`

```python
import json

json_metni = '{"isim": "Eyüp", "yas": 25}'
veri = json.loads(json_metni)   # JSON string → Python dict
print(veri["isim"])             # Eyüp
```

### Python → JSON: `json.dumps()`

```python
import json

veri = {"isim": "Eyüp", "yas": 25}
json_metni = json.dumps(veri)   # Python dict → JSON string
print(json_metni)               # {"isim": "Eyüp", "yas": 25}
```

### Güzel yazdırma: `indent`

```python
print(json.dumps(veri, indent=4, ensure_ascii=False))
```

### Dosyadan okuma/yazma

```python
# Dosyaya yaz
with open('veri.json', 'w', encoding='utf-8') as f:
    json.dump(veri, f, indent=4, ensure_ascii=False)

# Dosyadan oku
with open('veri.json', 'r', encoding='utf-8') as f:
    veri = json.load(f)
```

### JSON ↔ Python tip eşleşmesi

| JSON | Python |
|------|--------|
| object | dict |
| array | list |
| string | str |
| number | int / float |
| true / false | True / False |
| null | None |

---

## API Nedir?

**API (Application Programming Interface):** İki yazılımın birbiriyle konuşmasını sağlayan arayüz.

- Web'de genelde **REST API** kullanılır
- İstek atınca sana genelde **JSON** döner
- Örnek: hava durumu, döviz kuru, GitHub bilgileri

---

## `requests` ile API Kullanımı

Kurulum (bir kere):
```bash
pip install requests
```

### GET isteği

```python
import requests

url = "https://api.github.com/users/Eyupaln"
cevap = requests.get(url)

print(cevap.status_code)   # 200 → başarılı
veri = cevap.json()        # JSON'u Python dict'e çevirir
print(veri["login"])
```

### Status code'lar

| Kod | Anlam |
|-----|-------|
| 200 | OK — başarılı |
| 404 | Not Found — bulunamadı |
| 500 | Server Error — sunucu hatası |

### Hata yönetimi ile

```python
import requests

try:
    cevap = requests.get("https://api.github.com/users/Eyupaln", timeout=10)
    cevap.raise_for_status()   # Hata kodunda exception fırlatır
    veri = cevap.json()
    print(veri["login"])
except requests.exceptions.RequestException as e:
    print(f"Hata: {e}")
```

---

## Özet Tablo

| İşlem | Kod |
|-------|-----|
| JSON string → dict | `json.loads()` |
| dict → JSON string | `json.dumps()` |
| Dosyaya yaz | `json.dump(veri, f)` |
| Dosyadan oku | `json.load(f)` |
| API isteği | `requests.get(url)` |
| Cevabı dict'e çevir | `cevap.json()` |

---

## Sıradaki Adım

Day 23: CSV dosyaları
