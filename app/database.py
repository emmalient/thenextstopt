import sqlite3
from config import Config


def get_db():
    """Veritabanina baglanti acar."""
    conn = sqlite3.connect(Config.DATABASE_URL)
    conn.row_factory = sqlite3.Row  # satirlara sutun adiyla erisim saglar
    return conn


def init_db(app):
    """leads tablosunu olusturur (yoksa)."""
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            eposta TEXT NOT NULL,
            mesaj TEXT,
            ilgi_alani TEXT,
            tarih TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()


def lead_ekle(isim, eposta, mesaj, ilgi_alani):
    """Yeni bir kayit (lead) ekler."""
    conn = get_db()
    conn.execute(
        'INSERT INTO leads (isim, eposta, mesaj, ilgi_alani) VALUES (?, ?, ?, ?)',
        (isim, eposta, mesaj, ilgi_alani)
    )
    conn.commit()
    conn.close()


def tum_leadler():
    """Tum kayitlari en yeniden eskiye getirir."""
    conn = get_db()
    kayitlar = conn.execute(
        'SELECT * FROM leads ORDER BY tarih DESC'
    ).fetchall()
    conn.close()
    # Her kaydi sozluge cevirip liste olarak donduruyoruz
    return [dict(kayit) for kayit in kayitlar]