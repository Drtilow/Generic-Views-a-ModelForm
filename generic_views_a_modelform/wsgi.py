import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'generic_views_a_modelform.settings')

application = get_wsgi_application()

