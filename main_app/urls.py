from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('fish/', views.fish_index, name='fish'),
	path('fish/<int:fish_id>/', views.fish_detail, name='detail'),
	path('fish/create/', views.FishCreate.as_view(), name='fish_create'),
	path('fish/<int:pk>/update/', views.FishUpdate.as_view(), name='fish_update'),
	path('fish/<int:pk>/delete/', views.FishDelete.as_view(), name='fish_delete'),
	path('fish/<int:fish_id>/add_feeding/', views.add_feeding, name='add_feeding'),
	path('fish/<int:fish_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
	path('fish/<int:fish_id>/remove_toy/<int:toy_id>/', views.remove_toy, name='remove_toy'),
	path('toys/', views.ToyList.as_view(), name='toys_index'),
	path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
	path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
	path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
	path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]