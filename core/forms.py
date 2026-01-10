from django import forms
from .models import Product, Lead

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'subtitle', 'slug', 'price', 'kiwifi_url', 'description', 'benefits', 'cover_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Líder do Futuro'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex: lider-do-futuro'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'kiwifi_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://pay.kiwify.com.br/...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'benefits': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Um benefício por linha'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu Nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu E-mail'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu WhatsApp'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Como posso te ajudar?'}),
        }
