from django.urls import path
from . import views 

app_name = "cars"
urlpatterns = [
    path('new/', views.manage_car_view, name="add_car"),
    path('update/<car_id>/',views.manage_car_view, name="update_car"),
    path('colors/new/', views.manage_color_view, name="add_color"),
    path('colors/update/<color_id>/', views.manage_color_view, name ="update_color"),
]