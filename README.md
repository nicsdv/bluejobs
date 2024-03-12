# bluejobs

BlueJobs is a schedule creator website that aims to provide ADMU students with possible schedules of their classes according to the preferences that they input with regard to class times and instructor traits. This will help the students in planning for their enlistment and make the process more efficient, as well as for departments to post their offered courses. Bluejobs showcases the following features:

1) Professor Select
2) Schedule Maker
3) Rate a Professor
4) Department Schedule Upload

Prepared by <br>
Lex Chan <br>
Eldon Dagdag <br>
Nics De Vega <br>
Neil Ocampo <br>
Tanya Yotoko <br>

CSCI 42 O - Descendants of the Chan

This project has been created by our group to the best of our own abilities.
Any outside source will be properly credited in their respective code fragments. 


To run the project: 
(Open command prompt for directory where project folder is located first)

Prerequisites: Python 3 and PIP

1. Create and activate a python virtual environment in the same folder/directory as the project folder, README.txt, and requirements.txt
	- py -m venv [env_name]
	- [env_name]\Scripts\activate
2. Install requirements
	- pip install -r requirements.txt
3. Go inside the bluejobs where the manage.py and bluejobs app are located.
4. Run the manage.py using the 'python manage.py runserver' command
5. Copy the given address in the terminal (or use localhost:8000 or whatever port is specified) to the browser
	- For the bluejobs application - bluejobs/ 
		- localhost:8000/bluejobs
	- For the django admin panel - admin/ (username: admin password: admin): 
		- localhost:8000/admin
