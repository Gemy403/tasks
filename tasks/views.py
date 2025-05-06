from django.shortcuts import render
from .models import Regions,SubRegions,Kpi,KpiValues 
# Create your views here.



# this is a function shows showcasing number of restaurants that failed food safety inspection across last months that is chosen:

def failed_food_safety_inspection(request):
    if request.method == 'POST':
        pass
    context = {
    }
    return render ('tasks/tasks.html',request,context)