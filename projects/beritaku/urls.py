#type: ignore

from django.urls import path, include
from beritaku import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('anime', views.anime, name='anime'),
    path('characters', views.characters, name='characters'),
    path('storyarc', views.storyarc, name='storyarc'),
    path('manga', views.manga, name='manga'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('detail/<int:berita_id>', views.detail, name='detail'),
    
    path('pengguna', views.pengguna, name='pengguna'),
    path('lihatdata', views.lihatdata, name='lihatdata'),
    path('keloladata', views.keloladata, name='keloladata'),
    path('logout', views.login, name='logout'),
    path('hapusdata/<int:berita_id>', views.hapusdata, name='hapusdata'),
    path('ubahdata/<int:berita_id>', views.editdata, name='ubahdata'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


