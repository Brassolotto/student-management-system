from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/edit/', views.edit_student, name='edit'),
    path('<int:id>/delete/', views.delete_student, name='delete'),
]