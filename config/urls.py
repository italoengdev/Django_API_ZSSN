from django.urls import path
from django.contrib import admin

from zssn.views import SurvivorListCreateView, SurvivorRetrieveUpdateLocation, ItemListCreateView, SurvivorDetailAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('survivors/', SurvivorListCreateView.as_view(),
         name='survivor_list_create'),
    path('survivors/update/<int:pk>/', SurvivorRetrieveUpdateLocation.as_view(),
         name='survivor_retrieve_update'),
    path('survivors/flag/<int:pk>/', SurvivorDetailAPIView.as_view(),
         name='survivor_retrieve_update'),
    path('items/', ItemListCreateView.as_view(), name='item_list_create')
]
