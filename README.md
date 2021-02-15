# Blog Website using Django RestFramework
###### To get the below APIs working, clone the repository
###### Install the requirements.txt file with command: pip install -r requirements.txt
###### Createsuper user and run the server : python manage.py runserver
###### Check the following links in Postman or on browser
#### APIs List
[Search Blog by Category API](http://127.0.0.1:8000/blog/?q=Horror)\
[Register API](http://127.0.0.1:8000/api/register/)\
[Login API](http://127.0.0.1:8000/api/login/)
##### CRUD API Category Table
[Get all categories](http://127.0.0.1:8000/category/)\
[Create update delete](http://127.0.0.1:8000/category_detail/<int:pk>)\
[example](http://127.0.0.1:8000/category_detail/3)
##### CRUD API for Blog Table
[Get all blogs](http://127.0.0.1:8000/blog/)\
[Create update delete](http://127.0.0.1:8000/blog_detail/<int:pk>)\
[example](http://127.0.0.1:8000/blog_detail/5)
