from django.contrib import admin

from .models import Makaleler, MakaleTags, Contact
from django.contrib.auth.models import User, Group


class MakalelerAdmin(admin.ModelAdmin):
    exclude = ('makale_slug',)
admin.site.register(Makaleler, MakalelerAdmin)


class MakaleTagsAdmin(admin.ModelAdmin):
    pass
admin.site.register(MakaleTags, MakaleTagsAdmin)


class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False

    list_display = ['iletisim_adsoyad', 'iletisim_tarihi']

admin.site.register(Contact, ContactAdmin)



admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.site_header = 'Zeybek Hukuk Yönetim Paneli'
