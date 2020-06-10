sudo pip install virtualenv
python3 -m venv myvenv
source myvenv/bin/activate
pip install Django==1.10
cd library
python manage.py makemigrations
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
