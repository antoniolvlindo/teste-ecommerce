from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # admin url
    path('admin/', admin.site.urls),

    # store app
    path('', include('store.urls')),

    # cart app
    path('cart/', include('cart.urls')),

    # account app
    path('account/', include('account.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
