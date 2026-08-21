from flask import Flask
from flask_cors import CORS
from config import config
from app.database import init_db
from app.routes import sayfa_bp, api_bp


def create_app(ortam='default'):
    app = Flask(__name__)

    # 1. Ayarlari yukle
    app.config.from_object(config[ortam])

    # 2. CORS ac (Wix sitenin backend'e istek atabilmesi icin)
    CORS(app, origins=app.config['CORS_ORIGINS'])

    # 3. Veritabanini baslat
    with app.app_context():
        init_db(app)

    # 4. Blueprint'leri kaydet
    app.register_blueprint(sayfa_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    # 5. Sunucunun canli olup olmadigini kontrol etmek icin basit bir uc nokta
    @app.route('/health')
    def health():
        return {'durum': 'aktif'}, 200

    return app