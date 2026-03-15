python -m venv venv
venv\Scripts\activate
pip install Django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install django-cors-headers
pip install Pillow
pip install python-dotenv
pip install django-filter
python manage.py makemigrations accounts
python manage.py makemigrations attractions
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
