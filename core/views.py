from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, SiteSettings, Service
from .forms import LeadForm, ProductForm

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
