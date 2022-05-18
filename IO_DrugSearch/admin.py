from django.contrib import admin

# Register your models here.
from IO_DrugSearch.models import Lek, SzczegolyRefundacji

admin.site.register(Lek)
admin.site.register(SzczegolyRefundacji)
