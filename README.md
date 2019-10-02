# Central Library and Information Center of PUST

## Implementation Workflow

1. Create Django Project

```
    django-admin startproject core
```

2. Create `account` App

```
    python manage.py startapp account
```

3. Make initial migration

```
    python manage.py makemigrations
    python manage.py migrate
```

4. Create `academic` App
   In _academic_ app several model-class can have, i.e. _department_, _faculty_, _program_, _institute_ etc.

We want to create three model-class in this _academic_ app:

1. `faculty` : It is the university faculty.
2. `department` : It is the university department.
3. `program` : It is the university academic program.

First create _academic_ app

```
    python manage.py startapp academic
```

Then create three models and make a migration on _academic_ app

```
    python manage.py makemigrations academic
    python manage.py migrate academic
```
