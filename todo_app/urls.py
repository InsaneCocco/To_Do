
from .views import ListListView
from django.urls import path

urlpatterns = [
    path('index', ListListView.as_view(), name= 'viewlist')
]