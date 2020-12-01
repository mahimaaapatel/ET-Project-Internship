from django.contrib import admin
from . import models

admin.site.register(models.Company)
admin.site.register(models.CustomUser)
admin.site.register(models.Application)
admin.site.register(models.Resume)

