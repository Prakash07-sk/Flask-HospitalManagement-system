# Flask-HospitalManagement-system
Its an web application made on python flask.
After downloading this code then commit the database using the following commands
open command prompt then go to the vaidate file location
-> python
-> from database import db
-> db.commit_all()
-> exit()
 after commit  database then install sqlite3 software based on your system version(https://www.sqlite.org/download.html).
Then open the sqlite using below  commands
-> sqlite3 hpmanagement.db
->.tables
(after enter that line that show User table, if it doesn't shows your database creation may be wrong!)

if SQLALCHEMY_TRACK_MODIFICATIONS error shows, Enter your first quary mannualy then run the application.
