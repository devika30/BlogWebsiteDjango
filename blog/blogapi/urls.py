from django.urls import path
from knox import views as knox_views
from .views import *
urlpatterns = [
  
   path('category/',category_list),
   path('detail/<int:pk>',category_detail),
   path('blog/',blog_list),
   path('blog_detail/<int:pk>',blog_detail),
   path('api/register/', RegisterAPI.as_view(), name='register'),
   path('api/login/', LoginAPI.as_view(), name='login'),
   path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
   path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]