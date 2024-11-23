from django.shortcuts import render
from cars.models import Car, Brand, Color
from django.db.models import Q
# Create your views here.

from django.shortcuts import render

def dashboard_view(request):

    table = request.GET.get('table', 'cars')
    search_query = request.GET.get('search', '')

    if table == 'cars':
        cars = Car.objects.all()
        brands = []
        colors = []
        if search_query:
            cars = cars.filter(
                Q(name__icontains=search_query) | 
                Q(brand__name__icontains=search_query) |
                Q(model__icontains=search_query)
            )
    elif table == 'brands':
        cars = []
        brands = Brand.objects.all()
        colors = []
        if search_query:
            brands = brands.filter(
                Q(name__icontains=search_query)
            )
    elif table == 'colors':
        cars = []
        brands = []
        colors = Color.objects.all()
        if search_query:
            colors = colors.filter(
                Q(name__icontains=search_query)
            )

    return render(request, 'dashboard/dashboard.html', locals())