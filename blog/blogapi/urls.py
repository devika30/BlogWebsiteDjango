from django.urls import path
from .views import category_list,category_detail,blog_list,blog_detail
urlpatterns = [
  
   path('category/',category_list),
   path('detail/<int:pk>',category_detail),
   path('blog/',blog_list),
   path('blog_detail/<int:pk>',blog_detail),
   
]