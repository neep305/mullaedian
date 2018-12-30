from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /places/1/
    path('<int:shop_id>/', views.detail, name='detail'),
]