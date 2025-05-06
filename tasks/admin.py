from django.contrib import admin
from .models import Regions,SubRegions,Kpi,KpiValues


# Register your models here.





class SubRegionslInline(admin.TabularInline):
    model = SubRegions
    extra = 1  

class RegionAdmin(admin.ModelAdmin):
    inlines = [SubRegionslInline]


admin.site.register(Regions,RegionAdmin)
admin.site.register(SubRegions)
admin.site.register(Kpi)

admin.site.register(KpiValues)