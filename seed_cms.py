
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import SiteSettings, Service

# 1. Site Settings
settings, created = SiteSettings.objects.get_or_create(id=1)
if created:
    print("Created Default Site Settings")
else:
    print("Site Settings already exist")

# 2. Services
services_data = [
    {
        'title': 'Mentoria Empresarial',
        'description': 'Diagnóstico completo para identificar gargalos e otimizar a gestão da sua pequena empresa.',
        'icon': 'fas fa-chess-queen',
        'order': 1
    },
    {
        'title': 'Educação Financeira',
        'description': 'Aprenda a organizar suas finanças pessoais e investimentos para conquistar sua independência.',
        'icon': 'fas fa-chart-pie',
        'order': 2
    },
    {
        'title': 'Gestão de Negócios',
        'description': 'Estratégias práticas de liderança e processos para alavancar os resultados do seu negócio.',
        'icon': 'fas fa-users',
        'order': 3
    }
]

for s_data in services_data:
    Service.objects.get_or_create(title=s_data['title'], defaults=s_data)
    print(f"Service {s_data['title']} checked/created.")

print("CMS Data Seeded Successfully!")
