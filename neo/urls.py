from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# admin_soft.__name__="
# admin_soft.

admin.site.site_title = 'Neo'
admin.site.index_title = 'Admin'
admin.site.site_header = 'Neo Admin Portal'

urlpatterns = [

    path('jet/',  include('jet.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('order.urls')),
    path('profiles/', include('billing.urls')),
]

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
