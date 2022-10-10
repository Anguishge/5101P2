from django.contrib import admin

# Register your models here.
from.models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display=['name','duration','grade',]


admin.site.register(Movie,MovieAdmin)