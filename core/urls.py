from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from products.views import img_view

urlpatterns = [
    # path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('img/',img_view, name='controle_list'),
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
