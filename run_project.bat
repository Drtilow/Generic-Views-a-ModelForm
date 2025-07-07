@echo off
echo === Aktivace virtualniho prostredi ===
call venv\Scripts\activate

echo === Instalace Django ===
pip install django

echo === Spoustim migrace ===
python manage.py migrate

echo === Spoustim server ===
python manage.py runserver

pause

