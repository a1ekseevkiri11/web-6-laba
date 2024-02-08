from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/edit/<int:id>/', views.edit,  name='edit'),
    path('gallery/delete/<int:id>/', views.delete, name='delete')
]