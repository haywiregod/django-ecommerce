from django.urls import path
from .views import index,product,checkout,ItemListView,ItemDetailView
app_name = 'core'
urlpatterns = [
    path('',ItemListView.as_view(),name='home'),
    path('product/<slug>/',ItemDetailView.as_view(),name='product'),
    path('checkout/',checkout,name='checkout'),
]
