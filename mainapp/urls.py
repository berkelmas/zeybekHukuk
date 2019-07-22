from django.urls import path
from .views import index, about, ailehukuku, cezahukuku, gayrimenkulhukuku, icrahukuku, \
                ishukuku, mirashukuku, tazminathukuku, ticarethukuku, tiphukuku, iletisim, \
                yayinlar, makaledetay


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

    path('yayinlar', yayinlar, name="yayinlar"),
    path('yayin/<slug:makaleslug>', makaledetay, name="makaledetay")
]
