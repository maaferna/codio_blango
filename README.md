# Blango — Blog with Django & Django REST Framework

Blog application built through the **Advanced Django: Mastering Django and Django
REST Framework** specialization (Coursera). This repository holds the course
project as completed; an adapted version of it runs **live inside my portfolio**:

**▶ [portfolio-mparraf.herokuapp.com/blog](https://portfolio-mparraf.herokuapp.com/blog/)**
(re-integrated as a Django app with its own API and request throttling)

## What it demonstrates

- Blog domain model: posts with slugs, tags, generic-relation comments,
  `published_at` visibility and hero images (`django-versatileimagefield`)
- REST API with Django REST Framework: serializers, viewsets and dedicated
  `api/` module, plus **API test suites** (`test_post_api.py`, `test_tag_api.py`)
- Authentication with `django-allauth` (sign-up/sign-in) and JWT for the API
- Server-rendered UI with Django templates, custom template tags,
  Bootstrap 5 and crispy-forms

## Stack

Python · Django · Django REST Framework · django-allauth · JWT ·
Bootstrap 5 · crispy-forms · Pipenv

## Running locally

```bash
pipenv install            # or: pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Author

Marco Antonio Parra F. — [portfolio](https://portfolio-mparraf.herokuapp.com) ·
[LinkedIn](https://www.linkedin.com/in/marco-antonio-parra-82999337/)

*Course project from the Advanced Django specialization — the certificate is
listed in the [education section](https://portfolio-mparraf.herokuapp.com/education/)
of my portfolio.*
