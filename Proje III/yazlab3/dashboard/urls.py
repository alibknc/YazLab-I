from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('upload/', views.upload, name='upload'),
    path('table/', views.Table, name='table'),
    path('details/<str:id>', views.details_view, name='details'),
    path('logout/', views.logOut, name='logout'),
]