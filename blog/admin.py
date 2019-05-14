from django.contrib import admin
from blog import  models
# Register your models here.

admin.site.register(models.Reporter)
admin.site.register(models.Article)
admin.site.register(models.Question)
admin.site.register(models.Choice)

