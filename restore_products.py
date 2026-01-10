
import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Product

def create_products():
    # Clear existing to avoid duplicates during this restore
    Product.objects.all().delete()
    print("Old products cleared.")

    # Product 1: Líder do Futuro
    p1 = Product.objects.create(
        title="Líder do Futuro",
        subtitle="O Guia Definitivo para Liderança",
        slug="lider-do-futuro",
        price=47.90,
        kiwifi_url="https://pay.kiwify.com.br/ExampleLink1",
        description="Domine as competências essenciais para liderar com confiança e impacto. Um guia prático para gestores modernos.",
        benefits="Liderança Situacional\nGestão de Conflitos\nComunicação Assertiva\nMotivação de Equipes",
        long_description="<p>Este ebook é o resultado de anos de experiência...</p>"
    )
    print(f"Created: {p1.title}")

    # Product 2: Finanças Descomplicadas
    p2 = Product.objects.create(
        title="Finanças Descomplicadas",
        subtitle="Organize sua Vida Financeira",
        slug="financas-descomplicadas",
        price=29.90,
        kiwifi_url="https://pay.kiwify.com.br/ExampleLink2",
        description="Simples, direto e prático. Aprenda a sair das dívidas e começar a investir ainda hoje.",
        benefits="Controle de Gastos\nEliminação de Dívidas\nPrimeiros Investimentos\nMindset Financeiro",
        long_description="<p>Transforme sua relação com o dinheiro...</p>"
    )
    print(f"Created: {p2.title}")

    # Product 3: Gestão 360
    p3 = Product.objects.create(
        title="Gestão 360º na Prática",
        subtitle="Domine todos os pilares do seu negócio",
        slug="gestao-360",
        price=97.00,
        kiwifi_url="https://pay.kiwify.com.br/ExampleLink3",
        description="Uma visão completa sobre gestão de pessoas, processos, finanças e vendas para pequenas e médias empresas.",
        benefits="Gestão de Pessoas\nProcessos Eficientes\nFluxo de Caixa\nEstratégias de Venda",
        long_description="<p>O manual completo para o empresário...</p>"
    )
    print(f"Created: {p3.title}")

if __name__ == "__main__":
    create_products()
