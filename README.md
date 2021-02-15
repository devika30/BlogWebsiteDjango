# Blog Website using Django RestFramework
###### To get the below APIs working, clone the repository
###### Install the requirements.txt file with command: pip install -r requirements.txt
###### Createsuper user and run the server : python manage.py runserver
###### Check the following links in Postman or on browser
#### APIs List
#### [Search Blog by Category API](http://127.0.0.1:8000/blog/?q=Horror)
![search_blog_by_category](https://user-images.githubusercontent.com/37765578/107975203-c7794080-6fdd-11eb-9b50-1beee1e78aac.PNG)
#### [Register API](http://127.0.0.1:8000/api/register/)
![register](https://user-images.githubusercontent.com/37765578/107978221-67d16400-6fe2-11eb-97ba-fabb63565e9b.PNG)
![registerafter](https://user-images.githubusercontent.com/37765578/107978222-69029100-6fe2-11eb-813e-6e1c284c811c.PNG)

#### [Login API](http://127.0.0.1:8000/api/login/)
![login](https://user-images.githubusercontent.com/37765578/107978489-dca49e00-6fe2-11eb-8eb9-d35efaaf01f3.PNG)
![afterlogin](https://user-images.githubusercontent.com/37765578/107978202-62741980-6fe2-11eb-8da2-60d8e66e8367.PNG)

##### CRUD API Category Table
#### [Get all categories](http://127.0.0.1:8000/category/)
#### [Create update delete](http://127.0.0.1:8000/category_detail/<int:pk>)
[example](http://127.0.0.1:8000/category_detail/3)/
![categoryget](https://user-images.githubusercontent.com/37765578/107978208-64d67380-6fe2-11eb-8bab-86858dc6b47a.PNG)
![categorygetbyobject](https://user-images.githubusercontent.com/37765578/107978209-64d67380-6fe2-11eb-88a6-b06b4ce1c6b5.PNG)

##### CRUD API for Blog Table
#### [Get all blogs](http://127.0.0.1:8000/blog/)
#### [Create update delete](http://127.0.0.1:8000/blog_detail/<int:pk>)
[example](http://127.0.0.1:8000/blog_detail/5)/
![blogall](https://user-images.githubusercontent.com/37765578/107978205-63a54680-6fe2-11eb-9943-0f589290e6f4.PNG)
![blogdetail](https://user-images.githubusercontent.com/37765578/107978206-643ddd00-6fe2-11eb-951e-47a8ac3fe1e1.PNG)

