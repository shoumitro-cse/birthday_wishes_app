### Birthday Wishes App

This system has been developed to automate the process of sending 
birthday emails to customers. It utilizes a Restful API framework 
such as Django Rest Framework (DRF) and incorporates task 
scheduling and background task management for seamless operation. 
The system sends customers a personalized birthday message on 
their special day, ensuring a hassle-free and efficient birthday 
greeting process.

### Features
* Automatic birthday reminder emails: The project automatically sends birthday greetings to your customers on their special day.
* Customizable email templates: You can customize the email template to add a personal touch to your birthday messages.
* Django Admin integration: Easily manage customer records and birthdays through the Django Admin interface.
* Scalable and easy to extend: Built with Django and Celery, this project is highly extensible and can be integrated into your existing Django applications.

### Installation

* Project clone & run the development server
```
    # Python version 3.xx
    git clone https://github.com/shoumitro-cse/birthday_wishes_app.git
    cd birthday_wishes_app
    cp env.example .env
    python -m venv venv
    source ./venv/bin/activate
    pip install -r requirments.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic
    rm -rf static
    mv staticfiles static
    python manage.py runserver
```

* Start the Celery worker and beat processes for scheduling tasks:
```
    # Another terminal (Here, we can use either Redis or Rabbitmq.)
    docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=rb1234 rabbitmq:3.8-management
    docker run --restart always --name redis_container -p 6379:6379 -d redis
   
    celery -A birthday_reminder worker -B -l INFO
    or
    celery -A birthday_reminder worker --loglevel=info
    celery -A birthday_reminder beat --loglevel=info
```

### Installation (using docker compose)
```
    git clone https://github.com/shoumitro-cse/birthday_wishes_app.git
    cd birthday_wishes_app
    cp env.example .env
    docker-compose up --build -d
    or
    docker-compose up --build 
```
Now, your Birthday Wishes Project should be up and running.


### Usage

* Access the Django Admin interface (usually at http://localhost:8000/admin/) to manage customer records and birthdays.
* Customize the birthday greeting email template to fit your needs.
* Let the project automatically send birthday greetings to your customers on their special day.

