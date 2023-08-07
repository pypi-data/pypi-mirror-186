=====
Ecard
=====
Ecard is a Django app to create card. For each user,
 create a card and export it as pdf and docx documents.

Quick start
-----------
1. Add "cardprn" to your INSTALLED_APPS setting like this:
INSTALLED_APPS = [
...
'ecard',
]

2. Include the cardprn URLconf in your project urls.py like this:
path('ecard/', include('ecard.urls')),

3. Run ``python manage.py makemigration`` and ``python manage.py migrate``  to create the ecard models. and ''python manage.py createsuperuser" to login ecard page.

4. Visit http://127.0.0.1:8000/ecard/ to create users and its cards.

first uplaod your template and then print cards.
