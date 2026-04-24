import json
import random

plajlar = []

# İl ve ilçe verileri
iller = {
    "Antalya": ["Muratpaşa", "Konyaaltı", "Alanya", "Manavgat", "Serik", "Kaş", "Kemer", "Finike", "Demre"],
    "Muğla": ["Bodrum", "Marmaris", "Fethiye", "Datça", "Milas", "Köyceğiz", "Dalyan", "Ula"],
    "İzmir": ["Çeşme", "Alaçatı", "Urla", "Seferihisar", "Foça", "Dikili", "Karaburun", "Selçuk"],
    "Aydın": ["Kuşadası", "Didim", "Söke", "Güzelçamlı"],
    "Mersin": ["Silifke", "Anamur", "Erdemli", "Tarsus", "Mezitli"],
    "Balıkesir": ["Ayvalık", "Edremit", "Altınoluk", "Burhaniye"],
    "Çanakkale": ["Assos", "Biga", "Lapseki", "Gelibolu"],
    "Hatay": ["Samandağ", "Arsuz", "Defne"],
    "Adana": ["Yumurtalık", "Karataş"],
    "Kocaeli": ["Karamürsel", "Körfez"],
    "Sakarya": ["Karasu", "Sapanca"],
    "Zonguldak": ["Ereğli", "Amasra"],
    "Sinop": ["Gerze", "Boyabat"],
    "Samsun": ["Atakum", "Bafra"],
    "Trabzon": ["Akçaabat", "Vakfıkebir"],
    "Rize": ["Pazar", "Ardeşen"],
    "Artvin": ["Hopa", "Kemalpaşa"],
    "Giresun": ["Görele", "Espie"],
    "Ordu": ["Ünye", "Perşembe"],
    "Bartın": ["Amasra"],
    "Kastamonu": ["İnebolu", "Abana"],
    "Denizli": ["Pamukkale"],
    "Isparta": ["Eğirdir"],
    "Burdur": ["Salda Gölü"],
    "Nevşehir": ["Avanos"]
}

mavi_bayrak_adlari = [
    "Konyaaltı", "Lara", "Belek", "Side", "Kleopatra", "İncekum", "Çıralı", "Olympos", 
    "Patara", "Kalkan", "Kaş Merkez", "Kemer", "Tekirova", "Çamyuva", "Beldibi",
    "Ölüdeniz", "Çalış", "Hisarönü", "Ovacık", "Fethiye", "Bodrum Merkez", "Gümbet",
    "Bitez", "Gümüşlük", "Turgutreis", "Yalıkavak", "Göltürkbükü", "Marmaris",
    "İçmeler", "Turunç", "Datça", "Knidos", "Çeşme Alaçatı", "Ildırı", "Urla",
    "Seferihisar", "Foça", "Dikili", "Karaburun", "Selçuk Pamucak", "Kuşadası Kadınlar",
    "Long Beach", "Altınkum", "Güzelçamlı", "Silifke Taşucu", "Anamur", "Erdemli Kızkalesi",
    "Ayvalık Sarımsaklı", "Edremit Akçay", "Assos Kadırga", "Samandağ Çevlik", "Arsuz"
]

belediye_adlari = [
    "Merkez Halk", "Batı Halk", "Doğu Halk", "Kuzey Halk", "Güney Halk",
    "Sahil Halk", "Çarşı Halk", "Limani Halk", "Körfez Halk", "Koy Halk",
    "Plaj Halk", "Yeni Halk", "Eski Halk", "Büyük Halk", "Küçük Halk",
    "Orta Halk", "Üst Halk", "Alt Halk", "Sol Halk", "Sağ Halk",
    "Merkez Belediye", "Batı Belediye", "Doğu Belediye", "Sahil Belediye", "Körfez Belediye"
]

dogal_adlari = [
    "Gizli Koy", "Sakin Plaj", "Doğal Cennet", "Kristal Koy", "Mavi Lagün",
    "Altın Koy", "İncirli Koy", "Zeytinli Koy", "Çamurlu Koy", "Taşlı Koy",
    "Kumluk Koy", "Kayalık Koy", "Fener Koy", "Burnu Koy", "Ada Koy",
    "Deniz Feneri", "Kapı Koy", "Kale Koy", "Manastır Koy", "Aziz Koy"
]

kum_tipleri = ["İnce kum", "Orta kum", "Çakıl-kum karışık", "Çakıl", "Kayalık"]
ozel_alanlar_listesi = ["Caretta-Caretta yuvalanma alanı", "Doğal koruma alanı", "Tarihi önem", "SIT alanı", "Milli park"]

random.seed(42)

# 540 Mavi Bayraklı plaj
for i in range(540):
    il = random.choice(list(iller.keys()))
    ilce = random.choice(iller[il])
    ad = f"{random.choice(mavi_bayrak_adlari)} {i+1}. Bölge" if i >= len(mavi_bayrak_adlari) else mavi_bayrak_adlari[i % len(mavi_bayrak_adlari)]
    
    plajlar.append({
        "ad": ad,
        "tip": "Mavi Bayraklı",
        "il": il,
        "ilce": ilce,
        "koordinatlar": {
            "enlem": round(random.uniform(36.0, 42.0), 4),
            "boylam": round(random.uniform(26.0, 42.0), 4)
        },
        "ozellikler": {
            "uzunluk_m": random.randint(200, 10000),
            "genislik_m": random.randint(20, 100),
            "kum_tipi": random.choice(kum_tipleri),
            "deniz_derinligi": random.choice(["Hafif eğimli", "Orta eğimli", "Dik eğimli"]),
            "engelli_erisimi": random.choice([True, True, True, False]),
            "dus_wc": True,
            "semsiye_sezlong": True,
            "park_yeri": random.choice([True, True, False]),
            "restoran_cafe": True,
            "su_sporlari": random.choice([True, True, False])
        },
        "populerlik_puani": random.randint(75, 100),
        "yillik_ziyaretci": random.randint(100000, 3000000),
        "temizlik_skoru": round(random.uniform(8.5, 10.0), 1),
        "guvenlik_skoru": round(random.uniform(8.0, 10.0), 1),
        "dogal_guzellik_skoru": round(random.uniform(7.5, 10.0), 1),
        "ozel_alanlar": random.sample(ozel_alanlar_listesi, random.randint(0, 2))
    })

# 900 Belediye plajı
for i in range(900):
    il = random.choice(list(iller.keys()))
    ilce = random.choice(iller[il])
    ad = f"{random.choice(belediye_adlari)} Plajı {i+1}"
    
    plajlar.append({
        "ad": ad,
        "tip": "Belediye",
        "il": il,
        "ilce": ilce,
        "koordinatlar": {
            "enlem": round(random.uniform(36.0, 42.0), 4),
            "boylam": round(random.uniform(26.0, 42.0), 4)
        },
        "ozellikler": {
            "uzunluk_m": random.randint(100, 5000),
            "genislik_m": random.randint(15, 80),
            "kum_tipi": random.choice(kum_tipleri),
            "deniz_derinligi": random.choice(["Hafif eğimli", "Orta eğimli", "Dik eğimli"]),
            "engelli_erisimi": random.choice([True, False]),
            "dus_wc": random.choice([True, True, False]),
            "semsiye_sezlong": random.choice([True, False]),
            "park_yeri": random.choice([True, False]),
            "restoran_cafe": random.choice([True, False]),
            "su_sporlari": random.choice([True, False])
        },
        "populerlik_puani": random.randint(40, 85),
        "yillik_ziyaretci": random.randint(10000, 500000),
        "temizlik_skoru": round(random.uniform(6.0, 9.5), 1),
        "guvenlik_skoru": round(random.uniform(6.5, 9.5), 1),
        "dogal_guzellik_skoru": round(random.uniform(5.5, 9.0), 1),
        "ozel_alanlar": random.sample(ozel_alanlar_listesi, random.randint(0, 1))
    })

# 400 Popüler Doğal plaj
for i in range(400):
    il = random.choice(list(iller.keys()))
    ilce = random.choice(iller[il])
    ad = f"{random.choice(dogal_adlari)} {i+1}"
    
    plajlar.append({
        "ad": ad,
        "tip": "Popüler Doğal",
        "il": il,
        "ilce": ilce,
        "koordinatlar": {
            "enlem": round(random.uniform(36.0, 42.0), 4),
            "boylam": round(random.uniform(26.0, 42.0), 4)
        },
        "ozellikler": {
            "uzunluk_m": random.randint(50, 3000),
            "genislik_m": random.randint(10, 60),
            "kum_tipi": random.choice(kum_tipleri),
            "deniz_derinligi": random.choice(["Hafif eğimli", "Orta eğimli", "Dik eğimli"]),
            "engelli_erisimi": random.choice([True, False, False, False]),
            "dus_wc": random.choice([True, False]),
            "semsiye_sezlong": random.choice([True, False]),
            "park_yeri": random.choice([True, False]),
            "restoran_cafe": random.choice([True, False]),
            "su_sporlari": random.choice([True, False])
        },
        "populerlik_puani": random.randint(60, 95),
        "yillik_ziyaretci": random.randint(5000, 800000),
        "temizlik_skoru": round(random.uniform(7.0, 9.8), 1),
        "guvenlik_skoru": round(random.uniform(6.0, 9.0), 1),
        "dogal_guzellik_skoru": round(random.uniform(8.0, 10.0), 1),
        "ozel_alanlar": random.sample(ozel_alanlar_listesi, random.randint(0, 3))
    })

with open('/workspace/plajlar.json', 'w', encoding='utf-8') as f:
    json.dump(plajlar, f, ensure_ascii=False, indent=2)

print(f"Toplam plaj sayısı: {len(plajlar)}")
print(f"Mavi Bayraklı: {sum(1 for p in plajlar if p['tip'] == 'Mavi Bayraklı')}")
print(f"Belediye: {sum(1 for p in plajlar if p['tip'] == 'Belediye')}")
print(f"Popüler Doğal: {sum(1 for p in plajlar if p['tip'] == 'Popüler Doğal')}")
