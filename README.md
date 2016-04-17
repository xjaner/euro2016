# euro2016
El joc de l'Eurocopa 2016

Per modificar les traduccions d'apps instal.lades he fet servir el que expliquen aquí: http://source.mihelac.org/2010/07/31/handling-i18n-in-django-projects/

Quan canviï qualsevol traducció, s'ha de fer:
python manage.py compilemessages --settings=euro2016.settings.local

Coses que falten per arreglar:
- Al subject del mail d'acceptació del registre hi posa "[example.com]"
- Assegurar-me que el host és correcte al mail d'acceptació del registre
