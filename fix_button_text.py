
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import SiteSettings

def fix():
    settings = SiteSettings.objects.first()
    if settings:
        if "{{" in settings.hero_button_text:
            print(f"Detectado literal tag no banco: {settings.hero_button_text}")
            settings.hero_button_text = "CONHEÇA NOSSOS PRODUTOS"
            settings.save()
            print("✅ Texto do botão corrigido no banco de dados!")
        else:
            print("ℹ️ O texto do botão no banco parece estar correto.")
    else:
        print("❌ SiteSettings não encontrado.")

if __name__ == "__main__":
    fix()
