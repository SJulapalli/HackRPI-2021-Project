# HackRPI-2021-Project

## How to run the application

Make account with https://auth0.com/
Create a new application.

run on shell
```
touch .env
nano .env
```
Copy&Paste from Auth0 application credentials:

```
APP_CLIENT_ID=<Your Auth0 Client ID>
APP_DOMAIN=<Your Auth0 Domain>
APP_CLIENT_SECRET=<Your Auth0 Client Secret>
```
save file


Create your virtual environment and install dependencies with

```
pip install -r requirements.txt
```

Create your database with
```
python manage.py migrate
```

Run app with 
```
python manage.py runserver
```

