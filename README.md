# Tech Stack

## Tech Stack
1. Python 
2. Django 


## Django Packages
#### (for installation - pip install virtualenv)
`/candidate $ virtualenv venv`

#### activate venv
`/candidate $ source venv/bin/activate`


#### Install Django & required packages
`sh
(venv) $ pip install -r requirements.txt
`
#### Freeze requirement
`(venv) /django $ pip freeze > requirements.txt`

#### Migrate models & create superuser 
`sh
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
(venv) $ python manage.py createsuperuser
`

#### Run dev server in port 8002
`sh
(venv) $ python manage.py runserver 8002
`
#### For admin access use below url in browser
`sh
http://127.0.0.1:8002/admin/  (or)  http://yourip:8002/admin  
`

#### For HTML webpage
`sh
http://127.0.0.1:8002/candidates/  
`


#### To Run fake data
`sh
(venv) $ python manage.py generate_fake_data 10
`
#### To  delete all the fake data
`sh
(venv) $ python manage.py flush
`