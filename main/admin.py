from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.IHCDatabase)
admin.site.register(models.FHCDatabase)
admin.site.register(models.FCDatabase)
admin.site.register(models.RDDatabase)
admin.site.register(models.NTWDatabase)
admin.site.register(models.ICDatabase)