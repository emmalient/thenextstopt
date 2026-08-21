from flask import Blueprint, request, jsonify, render_template
from app.database import lead_ekle, tum_leadler
from app.services.ai_service import ai_service, AIServiceError

# Sayfalari gosteren rotalar (index, dashboard)
sayfa_bp = Blueprint('sayfalar', __name__)

# API rotalari (/api on ekiyle kullanilacak)
api_bp = Blueprint('api', __name__)


@sayfa_bp.route('/')
def anasayfa():
    return render_template('index.html')


@sayfa_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@api_bp.route('/sohbet', methods=['POST'])
def sohbet():
    veri = request.get_json()

    if not veri or 'mesaj' not in veri:
        return jsonify({'basari': False, 'hata': 'Mesaj alani zorunlu.'}), 400

    mesaj = veri['mesaj']
    gecmis = veri.get('gecmis', [])

    try:
        cevap = ai_service.yanit_uret(mesaj, gecmis)
        return jsonify({'basari': True, 'cevap': cevap}), 200
    except AIServiceError as hata:
        return jsonify({'basari': False, 'hata': str(hata)}), 503


@api_bp.route('/leads', methods=['POST'])
def yeni_lead():
    veri = request.get_json()

    if not veri or not veri.get('isim') or not veri.get('eposta'):
        return jsonify({'basari': False, 'hata': 'Isim ve eposta alanlari zorunlu.'}), 400

    isim = veri['isim']
    eposta = veri['eposta']
    mesaj = veri.get('mesaj', '')
    ilgi_alani = veri.get('ilgi_alani', 'genel')

    lead_ekle(isim, eposta, mesaj, ilgi_alani)
    return jsonify({'basari': True, 'mesaj': 'Kayit basariyla eklendi.'}), 201


@api_bp.route('/leads', methods=['GET'])
def leadleri_listele():
    kayitlar = tum_leadler()
    return jsonify({'basari': True, 'kayitlar': kayitlar}), 200