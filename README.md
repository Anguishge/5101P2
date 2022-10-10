# 5101P2

# Create and activate virtual environment
virtualenv -p python3 env1
. ./env1/bin/activate

# Install Python dependencies
pip install -r requirements.txt
## 
django-admin startproject moviesite

python manage.py runserver

python manage.py startapp movies

## copy paste movies/tempates,admin.py, models.py, urls.py, views.py
## Modify moviesite/settings and urls 

python manage.py 

python manage.py makemigrations

python manage.py migrate
python manage.py createsuperuser 


# Run Django dev server
python manage.py runserver

