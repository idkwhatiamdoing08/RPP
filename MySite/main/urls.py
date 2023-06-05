from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('stock', views.stock, name='stock'),
    path('create', views.create, name='create'),
    path('<int:pk>/update', views.update.as_view(),name='update'),
    path('<int:pk>/delete', views.delete.as_view(),name='delete'),
    path('login', views.login, name='login')
]