from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ecommerce.views import home_page, register_page, login_page, contact_page
import products.urls
import search.urls


urlpatterns = [
    path('', home_page, name='home_page'),
    path('register', register_page, name='register'),
    path('login', login_page, name='login_page'),
    path('contact', contact_page, name='contact_page'),
    path('products/', include(products.urls)),
    path('search/', include(search.urls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)