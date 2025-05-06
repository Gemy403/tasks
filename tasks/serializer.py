from rest_framework import serializers
from .models import Regions,SubRegions,Kpi,KpiValues




class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions

class SubRegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubRegions


class KpiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kpi

class KpiValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = KpiValues
        fields = '__all__'