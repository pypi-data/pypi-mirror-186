"""
1. Django
2. FastAPI
"""
try:
    from django.conf import settings
except (ModuleNotFoundError, ImportError):
    import settings
