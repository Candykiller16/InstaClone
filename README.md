## HOW TO RUN IT? :hear_no_evil:

1) clone this project 
2) create venv, activate it and save packages from requirements.txt to your venv (``` pip install -r requirements.txt ```) 
3) create docker image (``` sudo docker build . ``` )
4) collect and up images (django + postgresql ) using one command by docker-compose  (``` sudo docker-compose up ```)
5) to add dummy users for project use command in separate terminal 
(``` sudo docker-compose run web python manage.py add_users count_of_users ```)
