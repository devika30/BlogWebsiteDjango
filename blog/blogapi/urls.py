from django.urls import path
from knox import views as knox_views
from .views import *
urlpatterns = [
  
   path('category/',CategoryAPIView.as_view()),
   path('category_detail/<int:pk>',CategoryDetails.as_view()),
   path('blog/',BlogList.as_view()),
   path('blog_detail/<int:pk>',BlogDetail.as_view()),
   path('api/register/', RegisterAPI.as_view(), name='register'),
   path('api/login/', LoginAPI.as_view(), name='login'),
   path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
   path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
   path('category/blog/<str:category_name>',get_by_category)
]