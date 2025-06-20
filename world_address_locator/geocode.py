import time
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
import pandas as pd

# Read Excel File (Excel dosyasını oku)
veri = pd.read_excel("D:/PHD/dunya-koordinatlari.xlsx")

# Start to get location information from Nominatim service (Nominatim servisinden konum bilgisi almak için başlat)
arama_motoru = Nominatim(user_agent="benim_uygulamam")

# Special function to get coordinates(Koordinatları almak için özel fonksiyon)
def koordinat_al(satir):
    adres_secenekleri = [
        ['mahalle', 'köy', 'ilçe', 'il', 'ülke'],
        ['köy', 'ilçe', 'il', 'ülke'],
        ['ilçe', 'il', 'ülke'],
        ['il', 'ülke'],
        ['ülke']
    ]

    for alanlar in adres_secenekleri:
        adres_bolumleri = []
        for alan in alanlar:
            if alan in satir and pd.notna(satir[alan]):
                deger = str(satir[alan]).strip()
                if deger:
                    adres_bolumleri.append(deger)
        tam_adres = ', '.join(adres_bolumleri)
        print(f"Adres deneniyor: {tam_adres}")
        try:
            konum =arama_motoru.geocode(tam_adres, timeout=10)
            if konum:
                return pd.Series([konum.latitude, konum.longitude])
        except GeocoderTimedOut:
            print("tekrar deneniyor...")
            time.sleep(2)
            return koordinat_al(satir)
        except Exception as e:
            print(f"Hata: {e}")
            return pd.Series([None, None])

    print("sonuç vermedi")
    return pd.Series([None, None])

def process_excel_file(input_file, output_file):
    veri = pd.read_excel(input_file)
    #veri[['enlem', 'boylam']] = veri.apply(koordinat_al, axis=1)
    #veri.to_excel(output_file, index=False)
    #print(f"işlem başarılı. Dosya: {output_file}")

veri[['enlem', 'boylam']] = veri.apply(koordinat_al, axis=1)

veri.to_excel("dunya-koordinatlari.xlsx", index=False)
print("işlem başarılı. Dosya: dunya_koordinatli.xlsx")
