# world_address_locator

Excel dosyasındaki adreslerden (Dünya bazinda) koordinat (enlem, boylam) bilgisi çıkaran Python paketi.  
OpenStreetMap (Nominatim) altyapısı ile çalışır.

## Kullanım

```python
from world_address_locator import process_excel_file
process_excel_file("adresler.xlsx", "sonuc.xlsx")
yaml
Copy
Edit


Projeyi klonladıktan veya indirdikten sonra:

pip install -e .
