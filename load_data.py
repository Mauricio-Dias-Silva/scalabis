from core.models import Product
from django.core.files import File

def create_products():
    if Product.objects.count() > 0:
        print("Data already exists.")
        return

    # Produto 1: Gestão 360
    p1 = Product(
        title="Gestão 360º na Prática",
        subtitle="Organize sua empresa",
        slug="gestao-360",
        price=97.90,
        kiwifi_url="https://pay.kiwify.com.br/ipY4f19",
        description="O manual definitivo para organizar e escalar sua empresa.",
        benefits="Processos que funcionam\nControle Financeiro\nGestão de Pessoas"
    )
    # Mock image (assuming file exists in media or we just save without it first and user updates in admin)
    # p1.cover_image.save('gestao.png', File(open('static/img/ebook-financas-cover.png', 'rb'))) # Using finance cover as placeholder
    p1.save()

    # Produto 2: Líder do Futuro
    p2 = Product(
        title="Líder do Futuro",
        subtitle="Inspire equipes",
        slug="lider-do-futuro",
        price=67.00,
        kiwifi_url="https://pay.kiwify.com.br/ipY4f19",
        description="Desenvolva a liderança que retém talentos.",
        benefits="Inteligência Emocional\nFeedback Assertivo\nDelegação Eficaz"
    )
    p2.save()

    # Produto 3: Finanças
    p3 = Product(
        title="Finanças Descomplicadas",
        subtitle="Domine seu dinheiro",
        slug="financas-descomplicadas",
        price=49.90,
        kiwifi_url="https://pay.kiwify.com.br/ipY4f19",
        description="Saia do vermelho e comece a lucrar em 30 dias.",
        benefits="Fluxo de Caixa\nCorte de Custos\nInvestimentos"
    )
    p3.save()
    print("Products created.")

create_products()
