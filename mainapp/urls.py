from django.urls import path
from .views import index, about, ailehukuku, cezahukuku, gayrimenkulhukuku, icrahukuku, \
                ishukuku, mirashukuku, tazminathukuku, ticarethukuku, tiphukuku, iletisim, \
                yayinlar, makaledetay

from django.views.generic import TemplateView

urlpatterns = [
    path('', index, name="index"),
    path('hakkimizda', about, name="about"),
    path('aile-hukuku', ailehukuku, name="ailehukuku"),
    path('ceza-hukuku', cezahukuku, name="cezahukuku"),
    path('gayrimenkul-hukuku', gayrimenkulhukuku, name="gayrimenkulhukuku"),
    path('icra-hukuku', icrahukuku, name="icrahukuku"),
    path('is-hukuku', ishukuku, name="ishukuku"),
    path('miras-hukuku', mirashukuku, name="mirashukuku"),
    path('tazminat-hukuku', tazminathukuku, name="tazminathukuku"),
    path('ticaret-hukuku', ticarethukuku, name="ticarethukuku"),
    path('tip-hukuku', tiphukuku, name="tiphukuku"),
    path('iletisim', iletisim, name="iletisim"),
    path('sitemap.xml/', TemplateView.as_view(template_name='mainapp/sitemap.xml', content_type='text/plain'), name="sitemap" ),
    path('robots.txt/', TemplateView.as_view(template_name='mainapp/robots.txt', content_type='text/plain')),

    path('yayinlar', yayinlar, name="yayinlar"),
    path('yayin/<slug:makaleslug>', makaledetay, name="makaledetay")
]
