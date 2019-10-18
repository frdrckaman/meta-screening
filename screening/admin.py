from django.contrib import admin
from screening.models import Screening
from screening.forms import ScreeningCrf


# Register your models here.

class ScreeningFormAdmin(admin.ModelAdmin):
    pass


admin.site.register(Screening, ScreeningFormAdmin)
