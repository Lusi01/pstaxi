from django.contrib import admin
#from motorpool import models - абсолютный импорт - указывает на папку
from . import models # относительный импорт, т.к. из своей же папки

# Register your models here.
@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


