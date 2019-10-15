# Central Library and Information Center of PUST

## WARNING!!!

Warning should be considered and should be made resonable decision.

1. In _academic_ app model's has `ForeignKey(settings.AUTH_USER_MODEL)`. But it should (may be) be `OneToOneField(settings.AUTH_USER_MODEL)`.

2. Running migrations:
   D:\Dev\cseai_env\lib\site-packages\django\db\models\fields\_\_init\_\_.py:1421: RuntimeWarning: DateTimeField User.validity received a naive datetime (2019-10-16 10:15:38.094172) while time zone support is active.
   RuntimeWarning)
   Applying account.0004_auto_20191016_0414... OK

## ERROR!!!

1. django.core.exceptions.FieldError: 'validity' cannot be specified for User model form as it is a non-editable field

Fix:

```
    Previous:
    validity = models.DateTimeField(
        auto_now=False, auto_now_add=True)  # need customization

    Fixed:
    validity = models.DateTimeField(
        auto_now=False, auto_now_add=False)  # need customization
```

## Links

- [dateutil - powerful extensions to datetime](https://github.com/dateutil/dateutil)

## Implementation Workflow

It is the step by step implementation activity.

### 1. Create Django Project

```
    django-admin startproject core
```

### 2. Create `account` App

```
    python manage.py startapp account
```

### 3. Make initial migration

```
    python manage.py makemigrations
    python manage.py migrate
```

### 4. Create `academic` App

In _academic_ app several model-class can have, i.e. _department_, _faculty_, _program_, _institute_ etc.

We want to create three model-class in this _academic_ app:

1.  `faculty` : It is the university faculty.
2.  `department` : It is the university department.
3.  `program` : It is the university academic program.

First create _academic_ app

```
    python manage.py startapp academic
```

Then create three models and make a migration on _academic_ app

```
    python manage.py makemigrations academic
    python manage.py migrate academic
```

### 5. Create `member` app

There are six type of member in CLIC and each member type is a model-class in `member` app.
These six member types are:

- Student
- Teacher
- Officer
- Staff
- Othermember
- Librarian

First create `member` app:

```
    python manage.py startapp member
```

Then create various model-class and make migration.

```
    python manage.py makemigrations member
    python manage.py migrate member
```

### 6. Create `resource` App

There are money type of resource, like book, digital document, publication etc.
We want create two model-class.

- Author
- Book
- Resource

```
    python manage.py startapp resource
```

Then create model-class and migrate

```
    python manage.py makemigrations resource
    python manage.py migrate resource
```

### 7. Create `transaction` App

There are two type of transaction currently in CLIC.

- TrxBook
- TrxResource

Firstly create `transaction` app and then add model-class.

```
    python manage.py startapp transaction
```

Then make migrations for `transaction`

```
    python manage.py makemigrations transaction
    python manage.py migrate transaction
```

### 8. Create `service` App

In `service` app can have many type of model-class. Currently have:

- Request
- Report
- Notice

Firstly create `service` app and then add model-class.

```
    python manage.py startapp service
```

Then make a migration:

```
    python manage.py makemigrations service
    python manage.py migrate service
```

### 9. Create `amtd` App

`Activity Monitoring and Threat Detection` ( **AMTD** ) is for monitoring all transaction and user activity and threat dectection.
In this `amtd` App currently have one model-class:

- Activity

Firstly create `amtd` app and then add model-class.

```
    python manage.py startapp amtd
```

Then make a migration:

```
    python manage.py makemigrations amtd
    python manage.py migrate amtd
```

### 10. Create `post` App

In this `post` App currently have one model-class:

- Post

Firstly create `post` app and then add model-class.

```
    python manage.py startapp post
```

Then make a migration:

```
    python manage.py makemigrations post
    python manage.py migrate post
```

### 11. Create `comment` App

In this `comment` App currently have one model-class:

- Comment

Firstly create `comment` app and then add model-class.

```
    python manage.py startapp comment
```

Then make a migration:

```
    python manage.py makemigrations comment
    python manage.py migrate comment
```

### 12. Create `messenger` App

In this `messenger` App currently have one model-class:

- Message

Firstly create `messenger` app and then add model-class.

```
    python manage.py startapp messenger
```

Then make a migration:

```
    python manage.py makemigrations messenger
    python manage.py migrate messenger
```

### 13. Install `django-notifications-hq` (`notifications`) App

[django-notifications-hq](https://pypi.org/project/django-notifications-hq/) is a GitHub notification alike app for Django.

Installation is easy using `pip` and will install all required libraries.

```
    $ pip install django-notifications-hq
```

The app should go somewhere after all the apps that are going to be generating notifications like `django.contrib.auth`

```
    INSTALLED_APPS = (
        'django.contrib.auth',
        ...
        'notifications',
        ...
    )
```

Add the notifications urls to your urlconf:

```
    import notifications.urls

    urlpatterns = [
        ...
        path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
        ...
    ]
```

To run schema migration, execute:

```
    python manage.py migrate notifications
```
