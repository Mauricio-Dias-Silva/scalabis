from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, SiteSettings, Service
from .forms import LeadForm, ProductForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
import decimal

def home(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso! Entraremos em contato em breve.')
            return redirect('home')
    else:
        form = LeadForm()

    
    # CMS Content
    site_settings = SiteSettings.objects.first()
    services = Service.objects.all()
    products = Product.objects.all()

    context = {
        'products': products, 
        'lead_form': form,
        'site_settings': site_settings,
        'services': services
    }
    return render(request, 'home.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    # Convert newline benefits to list if needed, or handle in template
    benefits_list = product.get_benefits_list()
    return render(request, 'product_detail.html', {'product': product, 'benefits': benefits_list})

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from .forms import ProductForm

@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', slug=product.slug)
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {'form': form})
@require_POST
def api_save_lead(request):
    try:
        data = json.loads(request.body)
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email', '')
        revenue = data.get('revenue', 0)
        profit = data.get('profit', 0)
        health = data.get('health', '')

        lead = Lead.objects.create(
            name=name,
            phone=phone,
            email=email,
            company_revenue=decimal.Decimal(str(revenue)),
            company_profit=decimal.Decimal(str(profit)),
            health_status=health,
            message=f"Capturado via Termômetro da Riqueza. Status: {health}"
        )

        return JsonResponse({'success': True, 'lead_id': lead.id})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)
