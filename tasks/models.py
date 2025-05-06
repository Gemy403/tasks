from django.db import models
 
 
# Table with regions of a country
class Regions(models.Model):
   region_id = models.BigIntegerField(primary_key=True)
   name = models.CharField(max_length=200)
 
   def __str__(self):
       return str(f"{self.region_id} - {self.name}")
   


# Table with subregions of a country
class SubRegions(models.Model):
   sub_region_id = models.BigIntegerField(primary_key=True)
   amana = models.ForeignKey(Regions, models.DO_NOTHING, db_column="region_id")
   name = models.CharField(max_length=200)
 
   def __str__(self):
       return str(f"{self.amana} - {self.name}")
 
# Table holding unique KPI names, we have 2 KPIs:
# - restaurants_count - number of open restaurants
# - visited_restaurants_count - number of restaurants that have been visited by food safety inspector
# - restaurant_warnings_count - number of restaurants that have received wanrning from food safety inspector
# - restaurant_fines_count - number of restaurants that have received fine from food safety inspector


class Kpi(models.Model):
   kpi_id = models.BigIntegerField(primary_key=True)
   kpi_name = models.CharField(max_length=64)
 
   def __str__(self):
       return str(self.kpi_name)
 
   class Meta:
       managed = True
       db_table = "dim_kpi"
 
 
# Table holding KPI values
# KPIs are recorded for each sub_region on monthly frequency
class KpiValues(models.Model):
   id = models.BigIntegerField(primary_key=True)
   year = models.IntegerField()
   month = models.IntegerField()
   sub_region = models.ForeignKey(
       SubRegions,
       on_delete=models.DO_NOTHING,
       db_column="sub_region_id",
   )
 
   kpi = models.ForeignKey(Kpi, models.DO_NOTHING, db_column="kpi_id")
   kpi_value = models.BigIntegerField(null=True)
 
   class Meta:
       abstract = False # i edited that just to create db and start project .
