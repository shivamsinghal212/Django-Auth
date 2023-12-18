
# Django Auth 

A project to demostrate Authentication APIs built using Django Rest Framework and JWT




## Installation



```bash
  1. create virtual env using requirements.txt
  2. Activate virtual env
  3. Run: python manage.py migrate
  4. Run: python manage.py runserver
  
```
    
## API Reference

#### Login
##### Returns access token and refresh token

```http
  POST /api/user/login/
```

| Body param | Type     | Description                       |
| :-------- | :------- |:-------------------------------- |
| `username` | `string` | **Required**.  |
| `password` | `string` | **Required**.|

#### Get profile
##### Returns firstname and lastname of the user

```http
  GET /api/user/profile/
```

| Header | format     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`     | `Bearer <token>` | **Required**. |

#### Get all users
##### Returns all users / user by id

```http
  GET /api/user/<id>
```






## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```

