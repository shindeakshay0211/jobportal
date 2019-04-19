from django.contrib import admin
from testapp.models import hydjobs,mumbaijobs,punejobs

# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email']

class mumbaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email']


class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email']



admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(mumbaijobs,mumbaijobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
