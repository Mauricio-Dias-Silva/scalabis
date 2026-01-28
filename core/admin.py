from django.contrib import admin
from .models import Product, Lead, SiteSettings, Service

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Herói (Topo do Site)', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_button_text')
        }),
        ('Sobre', {
            'fields': ('about_title', 'about_description', 'about_image')
        }),
        ('Contato', {
            'fields': ('contact_phone', 'contact_email', 'contact_address', 'contact_form_intro')
        }),
        ('Widgets & Elementos', {
            'fields': ('whatsapp_widget_text', 'show_termometro')
        }),
        ('Seção de Ebooks', {
            'fields': ('ebook_section_title', 'ebook_section_subtitle')
        }),
        ('Área de Bônus (Download)', {
            'fields': ('bonus_title', 'bonus_subtitle', 'bonus_button_text', 'bonus_spreadsheet', 'bonus_image')
        }),
    )
    def has_add_permission(self, request):
        # Allow addition only if no settings exist
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order')
    list_editable = ('order',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'price', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'phone')
    date_hierarchy = 'created_at'
