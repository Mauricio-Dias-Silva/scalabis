from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    title = models.CharField("Título", max_length=200)
    subtitle = models.CharField("Subtítulo", max_length=300, blank=True)
    slug = models.SlugField(unique=True, help_text="URL amigável (ex: gestao-360)")
    
    # Preço e Vendas
    price = models.DecimalField("Preço", max_digits=6, decimal_places=2)
    kiwifi_url = models.URLField("Link KiwiFi", help_text="Link do checkout")
    
    # Conteúdo VVisual
    cover_image = models.ImageField("Capa do Ebook", upload_to="ebooks/")
    description = models.TextField("Descrição Curta")
    
    # Detalhes da Página de Vendas
    long_description = models.TextField("Descrição Completa (HTML)", blank=True)
    benefits = models.TextField("Benefícios (Um por linha)", help_text="Liste os benefícios, um por linha")
    
    # Textos Customizáveis
    cta_text = models.CharField("Texto do Botão", max_length=50, default="QUERO GARANTIR MINHA VAGA")
    price_label = models.CharField("Rótulo do Preço", max_length=50, default="Investimento Único")
    benefits_title = models.CharField("Título dos Benefícios", max_length=100, default="O que você vai Aprender?")
    guarantee_text = models.CharField("Texto de Garantia", max_length=100, default="Pagamento 100% Seguro via KiwiFi")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ebook"
        verbose_name_plural = "Ebooks"

    def __str__(self):
        return self.title

    def get_benefits_list(self):
        return [b.strip() for b in self.benefits.split('\n') if b.strip()]

class Lead(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'Novo'),
        ('CONTACTED', 'Em Contato'),
        ('WON', 'Ganho'),
        ('LOST', 'Perdido'),
    ]

    name = models.CharField("Nome", max_length=100)
    email = models.EmailField("E-mail")
    phone = models.CharField("Telefone/WhatsApp", max_length=20, blank=True)
    message = models.TextField("Mensagem", blank=True)
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default='NEW')
    
    # Inteligência Financeira (Capturado do Calculadora)
    company_revenue = models.DecimalField("Faturamento Declarado", max_digits=12, decimal_places=2, null=True, blank=True)
    company_profit = models.DecimalField("Lucro Real Calculado", max_digits=12, decimal_places=2, null=True, blank=True)
    health_status = models.CharField("Saúde Financeira", max_length=20, blank=True, help_text="Diagnóstico automático do site")
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Leads (Clientes)"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"


class SiteSettings(models.Model):
    """
    Singleton model to manage homepage content.
    """
    # Hero Section
    hero_title = models.CharField("Título Herói", max_length=200, default="Estratégia e Liderança\nPara Negócios Reais")
    hero_subtitle = models.TextField("Subtítulo Herói", default="Transformo empresários em líderes de alta performance através de consultoria estratégica e inteligência financeira.")
    hero_button_text = models.CharField("Texto Botão Herói", max_length=50, default="Conheça Meus Materiais")
    hero_background_image = models.ImageField("Imagem de Fundo Herói", upload_to="site/", blank=True, null=True, help_text="Imagem de fundo da seção Hero")
    
    # About Section
    about_title = models.CharField("Título Sobre", max_length=100, default="Olá, sou Dilvania Teixeira")
    about_description = models.TextField("Descrição Sobre", default="Especialista em Educação Financeira e Gestão...")
    about_image = models.ImageField("Foto Sobre", upload_to="site/", blank=True, null=True, help_text="Se deixar em branco, usa a padrão.")

    # Contact Info
    contact_phone = models.CharField("Telefone/WhatsApp", max_length=20, default="(11) 98999-6055")
    contact_email = models.EmailField("Email", default="dillteixeira31@gmail.com")
    contact_address = models.CharField("Endereço", max_length=200, default="Santana de Parnaíba - SP")

    # Whatsapp Widget
    whatsapp_widget_text = models.CharField("Texto Widget WhatsApp", max_length=50, default="Falar comigo no WhatsApp")

    # Ebook Section
    ebook_section_title = models.CharField("Título Seção Ebooks", max_length=100, default="Educação Financeira Consciente")
    ebook_section_subtitle = models.TextField("Subtítulo Seção Ebooks", default="Guias práticos para organizar o dinheiro com clareza, método e decisões mais alinhadas à sua realidade")

    # Contact Section
    contact_form_intro = models.TextField("Texto Intro do Formulário", default="Se fizer sentido para você, este é um espaço para dar o próximo passo com clareza. Entre em contato para agendar uma conversa ou tirar dúvidas. Preencha o formulário abaixo")

    # Toggles
    show_termometro = models.BooleanField("Exibir Termômetro da Riqueza", default=False)

    # Bonus Material
    bonus_title = models.CharField("Título do Bônus", max_length=200, default='O "Pulo do Gato" que Faltava na Sua Gestão')
    bonus_subtitle = models.TextField("Descrição do Bônus", default='Eu preparei algo que você não encontra em lugar nenhum. Não é apenas uma planilha, é o Mapa do Tesouro da sua liberdade financeira.')
    bonus_button_text = models.CharField("Texto do Botão", max_length=100, default='BAIXAR "O MAPA DO TESOURO"')
    bonus_spreadsheet = models.FileField("Planilha Bônus (CSV/Excel)", upload_to="docs/", blank=True, null=True, help_text="Faça upload da planilha que será baixada. Se vazio, usa a padrão.")
    bonus_image = models.ImageField("Imagem/Ícone Personalizado", upload_to="site/", blank=True, null=True, help_text="Opcional. Substitui o ícone de presente.")

    class Meta:
        verbose_name = "Configurações do Site"
        verbose_name_plural = "Configurações do Site"

    def __str__(self):
        return "Configurações Gerais"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteSettings.objects.exists():
            return SiteSettings.objects.first()
        return super(SiteSettings, self).save(*args, **kwargs)


class Service(models.Model):
    """
    Dynamic services for the homepage.
    """
    ICON_CHOICES = [
        ('fas fa-chess-queen', 'Rainha (Xadrez)'),
        ('fas fa-chart-pie', 'Gráfico (Pizza)'),
        ('fas fa-users', 'Pessoas/Equipe'),
        ('fas fa-briefcase', 'Maleta'),
        ('fas fa-lightbulb', 'Lâmpada (Ideia)'),
        ('fas fa-rocket', 'Foguete'),
    ]

    title = models.CharField("Título", max_length=100)
    description = models.TextField("Descrição")
    icon = models.CharField("Ícone", max_length=50, choices=ICON_CHOICES, default='fas fa-briefcase')
    order = models.PositiveIntegerField("Ordem", default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return self.title
