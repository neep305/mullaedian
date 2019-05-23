# from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='index'),
    # ex: /places/1/
    url('<int:shop_id>/', views.detail, name='detail'),
]