import os

import django

import sys




PACKAGE_PARENT = '..'

APP_DIR = os.path.join(PACKAGE_PARENT, 'backend')

SCRIPT_DIR = os.path.dirname(

    os.path.realpath(

        os.path.join(os.getcwd(), os.path.expanduser(__file__))

    )

)

APP_DIR_PATH = os.path.normpath(os.path.join(SCRIPT_DIR, APP_DIR))

sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

sys.path.append(APP_DIR_PATH)




os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

django.setup()

TOKEN = '5625718175:AAFzhJsKOhAudBPtymDcm4xws1umITaNphs'