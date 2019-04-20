# Containerised REST API
To leverage the API you will need to follow the following steps:
	
	1) Install docker-ce and docker-compose
	2) Clone the repo and run docker-compose up
	3) Access the django container and create a new user

Prediction API endpoint: localhost:8080/restapp/predict/ <br>
You can use various ways like Postman or a script using Request library of Python to check the condition of API. 
## USE OF PYTHON SCRIPT WITH JSON INPUT
![script_images](https://github.com/Udit107710/ContainerisedRestApp/blob/master/images/test_script.png)

Use auth('<username>','<password>') in your script.

## USE OF POSTMAN
You should comment line 27 and 28 from restapp/views.py and uncomment line 29 to use Postman since it is only able to send data in form format
### Specify the auth details here
![auth_image](https://github.com/Udit107710/ContainerisedRestApp/blob/master/images/Auth_empty.png)

### Use the following headers
![header_image](https://github.com/Udit107710/ContainerisedRestApp/blob/master/images/header.png)

### Sample body
![body_image](https://github.com/Udit107710/ContainerisedRestApp/blob/master/images/body.png)

### Sample result
![result_image](https://github.com/Udit107710/ContainerisedRestApp/blob/master/images/result.png)

### /users/ endpoint sample
![get_users](https://github.com/Udit107710/ContainerisedRestApp/blob/master/images/get_users.png)
