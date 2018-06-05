from django.contrib import admin
from django.utils.html import format_html
from .models import Time, PrimeiraFase


class TimeAdmin(admin.ModelAdmin):

    list_display = ['nome', 'image_tag', ]

admin.site.register(Time, TimeAdmin)
admin.site.register(PrimeiraFase)
