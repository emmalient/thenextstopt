import requests
from config import Config


class AIServiceError(Exception):
    """Yapay zeka servisinde bir sorun olursa bu hata firlatilir."""
    pass


class AIService:
    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.business_context = Config.BUSINESS_CONTEXT
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"

    def yanit_uret(self, mesaj, gecmis=None):
        """Kullanicinin mesajina yapay zekadan yanit alir."""

        if not self.api_key:
            return "Demo modundayiz: Groq API anahtari tanimlanmamis."

        if gecmis is None:
            gecmis = []

        mesajlar = [{"role": "system", "content": self.business_context}]
        mesajlar.extend(gecmis)
        mesajlar.append({"role": "user", "content": mesaj})

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        veri = {
            "model": "openai/gpt-oss-20b",
            "messages": mesajlar
        }

        try:
            cevap = requests.post(self.api_url, headers=headers, json=veri, timeout=15)
            cevap.raise_for_status()
            sonuc = cevap.json()
            return sonuc["choices"][0]["message"]["content"]
        except Exception as hata:
            raise AIServiceError(f"Yapay zeka servisine ulasilamadi: {hata}")


ai_service = AIService()


