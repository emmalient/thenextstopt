from app.database import init_db, lead_ekle, tum_leadler

# Veritabanini ve tabloyu olustur
init_db(None)
print("Veritabani ve tablo olusturuldu.")

# Deneme kaydi ekle
lead_ekle("Test Kullanici", "test@example.com", "Merhaba, bilgi almak istiyorum.", "film")
print("Deneme kaydi eklendi.")

# Tum kayitlari listele
kayitlar = tum_leadler()
print("Kayitli veriler:")
for kayit in kayitlar:
    print(kayit)