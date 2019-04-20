# Containerised REST API
To leverage the API you will need to follow the following steps:
	
	1) Install docker-ce and docker-compose
	2) Clone the repo and run docker-compose up
	3) Access the django container and create a new user

Prediction API endpoint: localhost:8080/restapp/predict/
You can use various ways like Postman or a script using Request library of Python to check the condition of API. I have attached screenshots of Postman application usage.

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
