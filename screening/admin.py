from django.contrib import admin
from screening.models import Screening
from screening.forms import ScreeningForm


# Register your models here.


class ScreeningFormAdmin(admin.ModelAdmin):
    form = ScreeningForm


admin.site.register(Screening, ScreeningFormAdmin)
