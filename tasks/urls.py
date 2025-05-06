from django.urls import path,include
from.views import failed_food_safety_inspection
from .api import resturant_warning_or_fine


app_name = 'tasks'

urlpatterns = [
    path('failed_food_safety_inspection/',failed_food_safety_inspection,name='failed_food_safety_inspection'),
    
    ## API ##
    path ('api/resturant_warning_or_fine/',resturant_warning_or_fine,name='resturant_warning_or_fine')
]