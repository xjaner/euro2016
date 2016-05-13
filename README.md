# euro2016
El joc de l'Eurocopa 2016

Per modificar les traduccions d'apps instal.lades he fet servir el que expliquen aquí: http://source.mihelac.org/2010/07/31/handling-i18n-in-django-projects/

Quan canviï qualsevol traducció, s'ha de fer:
python manage.py compilemessages --settings=euro2016.settings.local

Quan faci deploy, he de configurar el nom i domini del Lloc a través de l'Admin > Llocs.

python manage.py loaddata euro2016full -v 3 --settings=euro2016.settings.local
