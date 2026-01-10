from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import home, product_detail, add_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add-product/', add_product, name='add_product'),
    path('<slug:slug>/', product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Force media serving in production (since we are not using GCS)
from django.conf import settings
from django.views.static import serve
from django.urls import re_path

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
