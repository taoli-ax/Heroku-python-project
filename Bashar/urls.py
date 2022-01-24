from django.urls import path, include
from Bashar.views import index_bashar,ship_detail
urlpatterns = [
    path('', index_bashar, name='index_bashar'),
    path('<int:pk>/',ship_detail,name='ship_detail')
]
