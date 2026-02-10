import os
import django
from django.urls import resolve, reverse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

try:
    url = '/api/voice/action/create/'
    resolved = resolve(url)
    print(f"URL '{url}' resolves to: {resolved.func.view_class.__name__}")
except Exception as e:
    print(f"Error resolving '{url}': {e}")
