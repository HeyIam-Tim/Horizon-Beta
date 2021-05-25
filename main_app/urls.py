from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.IndexPage.as_view(), name='index'),
    path('', views.list_products, name='index'),
]