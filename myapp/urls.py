from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.BlogNewsView.as_view(), name='blog'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blog/<int:pk>/update/', views.UpdateNewsView.as_view(), name='blog-update'),
    path('blog/<int:pk>/del/', views.DelNewsView.as_view(), name='blog-del'),
    path('blog/add', views.CreateNews.as_view(), name='blog-add'),
    path('contact/', views.contact, name='contact')
]
