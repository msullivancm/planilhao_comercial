from django.contrib import admin
from .models import Impressora
from .models import Multifuncional
from .models import Multifuncional_Producao

# Register your models here.

admin.site.register(Impressora)
admin.site.register(Multifuncional)
admin.site.register(Multifuncional_Producao)
