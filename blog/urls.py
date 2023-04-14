from django.urls import path
from .views import HomeView, BlogDetailView


urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', HomeView.as_view(), name='home')

]
