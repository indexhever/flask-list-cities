set DATABASE_URL=sqlite:///testDb.db

set APP_SETTINGS="config.DevelopmentConfig"

Initialize manage: python manage.py db init
Migrate database: python manage.py db migrate
Update database: python manage.py db upgrade
Start server: python manage.py runserver