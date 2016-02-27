#!venv/bin/python

import os, subprocess

def run():
	superphy.config.start_database()
    os.system("cd superphy/src/main; bash gulp.sh; cd ../../..")
    from app import create_app
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    app.run(host='0.0.0.0', debug=True, use_reloader=False)

def start_database(default="development"):
	os.system("cd superphy/database; bash scripts/start.sh %s" % default)

