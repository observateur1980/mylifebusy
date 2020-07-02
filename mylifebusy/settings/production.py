
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEBUG = False
ALLOWED_HOSTS = ['www.mylifebusy.com', 'mylifebusy.com']
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


GOOGLE_RECAPTCHA_SECRET_KEY ='6LcMnsYUAAAAANthW4SPyaGaeBkXFci6ywWfos-C'

