from django.contrib import admin

# Register your models here.

from Labels.models import Label

class LabelAdmin(admin.ModelAdmin):

    list_display=['id','name','user']


admin.site.register(Label,LabelAdmin)

