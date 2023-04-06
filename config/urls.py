from django.urls import path, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from zssn.views import SurvivorListCreateView, SurvivorRetrieveUpdateView, ItemListCreateView, TradeCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/survivors/', SurvivorListCreateView.as_view(),
         name='survivor_list_create'),
    path('api/survivors/<int:pk>/', SurvivorRetrieveUpdateView.as_view(),
         name='survivor_retrieve_update'),
    path('api/items/', ItemListCreateView.as_view(), name='item_list_create')
]
