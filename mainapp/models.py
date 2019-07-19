from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

from unidecode import unidecode

##    Makaleler, İletisim Talepleri, İs İlanları

class Contact(models.Model):
    iletisim_adsoyad = models.CharField(('Gönderenin Ad-Soyadı'), max_length=100)
    iletisim_telefon = models.CharField(('Ulaşım Bilgileri'), max_length= 100)
    iletisim_mail = models.CharField(('Mail Adresi'), max_length=100)
    iletisim_mesaj = models.TextField(('Mesaj'))
    iletisim_tarihi = models.DateTimeField(('İletişim Formu Gönderilme Tarihi'), auto_now_add=True)

    def __str__(self):
        return self.iletisim_adsoyad


    class Meta:
        verbose_name = ("İletişim Talebi")
        verbose_name_plural = ("İletişim Talepleri")
        ordering = ("-iletisim_tarihi",)



class MakaleTags(models.Model):
    makale_tag_isim = models.CharField(('Makale Tag'), max_length=100)

    def __str__(self):
        return self.makale_tag_isim

    class Meta:
        verbose_name = "Makale Etiketi"
        verbose_name_plural = "Makale Etiketleri"


class Makaleler(models.Model):
    makale_baslik = models.CharField(('Makale Başlığı'), max_length=150)
    makale_yayintarihi = models.DateField(('Makale Yayın Tarihi'))
    makale_mesaj = RichTextField()
    makale_slug = models.SlugField(unique=True)

    KATEGORILER = (
        ('ishukuku', 'İş Hukuku'),
        ('icrahukuku', 'İcra Hukuku'),
        ('ailehukuku', 'Aile Hukuku'),
        ('ticarethukuku', 'Ticaret Hukuku'),
        ('sigortahukuku', 'Sigorta Hukuku'),
        ('saglikhukuku', 'Sağlık Hukuku'),
        ('gayrimenkulhukuku', 'Gayrimenkul Hukuku'),
        ('sozlesmelerhukuku', 'Sözleşmeler Hukuku'),
        ('cezahukuku', 'Ceza Hukuku')
    )

    makale_kategori = models.CharField(('Makale Kategorisi'), max_length=50, choices=KATEGORILER)


    makale_meta_description = models.CharField(('Makale Meta Açıklaması(SEO İÇİN)'), max_length=350)

    tag = models.ManyToManyField(MakaleTags)

    def __str__(self):
        return self.makale_baslik

    def save(self, *args, **kwargs):

        self.makale_slug = slugify(unidecode(self.makale_baslik))
        super(Makaleler, self).save(*args, **kwargs)

    class Meta:
        ordering= ('-makale_yayintarihi',)
        verbose_name = "Makale"
        verbose_name_plural = "Makaleler"
