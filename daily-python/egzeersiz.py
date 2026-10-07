import csv

with open('puanlar.csv', 'r', encoding='utf-8-sig',newline='') as file:
    ayirici = csv.Sniffer().sniff(file.readline()).delimiter
    file.seek(0)
    reader = csv.DictReader(file,delimiter=ayirici)
    for row in reader:
      print(f"İsim: {row['İsim']}, Notlar: {row['Türkçe']}, {row['Matematik']}, {row['İngilizce']}")