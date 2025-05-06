from rest_framework.response import Response
from .serializer import RegionsSerializer,SubRegionsSerializer,KpiSerializer,KpiValuesSerializer
from .models import KpiValues
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes


@api_view(['POST'])  
@permission_classes([IsAuthenticated])  
def resturant_warning_or_fine(request):
    required_month = request.POST['month']
    required_year = request.POST['year']
    required_region_id = request.POST['region_id']

    ## if we made restaurant_fines_count ID Kpi id : 71884

    required_kpi_values = KpiValues.objects.filter(month=required_month,year=required_year,kpi__kpi_id=71884)
    if required_region_id :
        required_kpi_values=required_kpi_values.filter(sub_region__amana__region_id =required_region_id)
    required_kpi_count = required_kpi_values.count()
    return Response({'success:':True,'month':required_month,'year':required_year,'failed_inspections':required_kpi_count})

