from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *
from .filters import ProductFilter


# class IndexPage(ListView):
#     model = Product
#     context_object_name = 'products'
#     template_name = 'main_app/index.html'


def list_products(request):
	myFilter = ProductFilter()
	products = ''
	if request.GET.get('search') == 'search':
		products = Product.objects.all()
		myFilter = ProductFilter(request.GET, queryset=products)
		products = myFilter.qs 
	context = {'products':products, 'myFilter':myFilter}
	return render(request, 'main_app/index.html', context)