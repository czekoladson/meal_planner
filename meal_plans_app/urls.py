from django.urls import path
from . import views

app_name = 'meal_plans_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('days/', views.days, name='days'),  # Dodaj ścieżkę URL dla widoku `days`
    path('days/<int:day_id>/', views.day, name='day'),
]
