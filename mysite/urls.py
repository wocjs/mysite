
from django.contrib import admin
from django.urls import path, include
from polls.views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', index),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)