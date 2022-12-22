from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('fish/', views.fish_index, name='fish'),
	path('fish/<int:f_id>', views.fish_detail, name='detail'),
]