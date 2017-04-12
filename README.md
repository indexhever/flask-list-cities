The project was configured as follows:

	set DATABASE_URL=sqlite:///testDb.db

	set APP_SETTINGS="config.DevelopmentConfig"

	Initialize manage: python manage.py db init

	Migrate database: python manage.py db migrate

	Update database: python manage.py db upgrade

	Start server: python manage.py runserver


To start the application, the DATABASE_URL must be set, and then, run the command from root folder:

python manage.py runserver

The application will already start with the database and data on it.

Access: http://localhost:5000/getcities