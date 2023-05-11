REM This file can be run by task scheduler when the user logs in, for example.

REM Switch to project directory
CD "C:\Users\p_teg\dev\python\prod\win-server-utils\"

REM Run Flask application
START /min pipenv run flask run