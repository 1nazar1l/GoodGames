from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('game_page/<int:game_id>', views.game_page, name='game_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)