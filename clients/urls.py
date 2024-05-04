from django.urls import path
from .views import *

app_name = 'clients'

urlpatterns = [
    path("", ClientsListView.as_view(), name='clients_list'),
    path("create", ClientCreateView.as_view(), name='client_create'),
    path("<int:pk>", ClientDetailView.as_view(), name='client_detail'),
    path("<int:pk>/update", ClientUpdateView.as_view(), name='client_update'),
    path("<int:pk>/delete", ClientDeleteView.as_view(), name='client_delete'),
]
