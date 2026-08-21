import requests

BASE_URL = "http://127.0.0.1:5000"

print("1) /api/sohbet test ediliyor...")
cevap = requests.post(f"{BASE_URL}/api/sohbet", json={
    "mesaj": "The Next Stopt platformunda neler yapabilirim?"
})
print("Durum kodu:", cevap.status_code)
print("Yanit:", cevap.json())

print("\n2) /api/leads (POST) test ediliyor...")
cevap = requests.post(f"{BASE_URL}/api/leads", json={
    "isim": "Ayse Yilmaz",
    "eposta": "ayse@example.com",
    "mesaj": "Erken erisim istiyorum.",
    "ilgi_alani": "mimari"
})
print("Durum kodu:", cevap.status_code)
print("Yanit:", cevap.json())

print("\n3) /api/leads (GET) test ediliyor...")
cevap = requests.get(f"{BASE_URL}/api/leads")
print("Durum kodu:", cevap.status_code)
print("Yanit:", cevap.json())