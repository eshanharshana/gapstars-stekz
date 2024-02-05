Python version and database versions are in th docker file [Dockerfile](Dockerfile).
Python libraries [requirements.txt](requirements.txt) will be auto installed when you run the below command 
You can start setup the product with this command docker-compose up -d  
Postgres Integration is in the setting files
To migrate the models to the database please use the commands in django_commands file.
Once the migrations are completed project will run in your localhost:8000
Index page itself will have the APIS.
They are product & orders
You can find the postman export here [Label A.postman_collection.json](Label%20A.postman_collection.json)

Please make sure to use application/json as content type

<h4>Get Products</h4>

![img_2.png](img_2.png)

<h4>Create Products</h4>

![img_1.png](img_1.png)

<h4>View Orders</h4>

![img_6.png](img_6.png)

<h4>Create Initial Order</h4>

![img_7.png](img_7.png)

<h4>Add to Cart</h4>

![img_3.png](img_3.png)

<h4>Remove from Card</h4>

![img_4.png](img_4.png)

<h4>Confirm Order</h4>

![img_5.png](img_5.png)

