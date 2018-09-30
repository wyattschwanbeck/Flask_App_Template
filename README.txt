FLASK=1.0.2
PYTHON=3.6.6
SQLITE3=3.25.1

pip install the following packages:
	flask
	flask_bootstrap
	flask_sqlalchemy
	werkzeug.security
	flask_login

To configure, set the app config variables in app.py and create_db.py so they point to the same database with the same secret key
To set up tables in the database:
	run python within current directory
	in interpreter, type the following commands:
		>>from create_db import db
		>>db.create_all()
		>>quit()
	
