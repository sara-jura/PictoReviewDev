from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('mappings', views.defineMappings, name='mappings'),
    path('mappings/<conf_prefix>', views.dumpFile, name='dump'),
    path('callMockup', views.uploadReviews, name='callMockup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)