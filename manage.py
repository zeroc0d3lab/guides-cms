#!/usr/bin/env python

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

if 'APP_SETTINGS' not in os.environ:
    os.environ['APP_SETTINGS'] = 'config.DevelopmentConfig'

if 'DATABASE_URL' not in os.environ:
    os.environ['DATABASE_URL'] = 'postgresql://localhost/pskb_dev'

from pskb_website import app
from pskb_website import db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.run()