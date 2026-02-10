
import os
import django
from django.urls import get_resolver

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

resolver = get_resolver()

def print_urls(urlpatterns, prefix=''):
    for pattern in urlpatterns:
        if hasattr(pattern, 'url_patterns'):
            # It's an include
            new_prefix = prefix + str(pattern.pattern)
            print_urls(pattern.url_patterns, new_prefix)
        else:
            # It's a view
            print(f"{prefix}{pattern.pattern} -> {pattern.callback.__name__}")

print("Printing all URL patterns:")
print_urls(resolver.url_patterns)
