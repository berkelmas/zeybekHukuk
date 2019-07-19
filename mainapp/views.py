from django.shortcuts import render
from .models import Makaleler

# Create your views here.
def index(request):
    ucmakale = Makaleler.objects.all().order_by('-makale_yayintarihi')[:3]
    return render(request, 'mainapp/index.html', {'ucmakale' : ucmakale})
