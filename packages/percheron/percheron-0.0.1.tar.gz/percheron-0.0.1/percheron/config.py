from dotenv import load_dotenv
import os
from pathlib import Path
load_dotenv()

CACHE_FOLDER = "cache"
REPORT_FOLDER = "reports"
DATA_FOLDER = "data"



DJANGO_TRAC = "https://code.djangoproject.com/jsonrpc"
DJANGO_PROJECT = "django"
TRANSLATIONS_PROJECT = "django-docs-translations"

DJANGO_REPO = Path(CACHE_FOLDER) / DJANGO_PROJECT
TRANSLATIONS_REPO = Path(CACHE_FOLDER) / TRANSLATIONS_PROJECT


GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", None)

def validate_configuration():
    """Confirm settings before things start."""
    if "GITHUB_TOKEN" not in os.environ.keys():
        return "GITHUB_TOKEN is not defined. You will have problems later."
