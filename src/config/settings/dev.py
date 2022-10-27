from config.settings.base import *  # NOQA:

CURRENT_ENV = "DEV"
print(CURRENT_ENV)

DEBUG = True

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static/")]

if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "github_actions",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        },
    }
else:
    DATABASES = {
        "default_sql": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        },
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("POSTGRES_DB"),
            "USER": 'admin',
            "PASSWORD": 'admin',
            "HOST": os.environ.get("POSTGRES_HOST"),
            "PORT": os.environ.get("POSTGRES_PORT"),
        },
        "non-rel": {
            "ENGINE": "djongo",
            "NAME": os.environ.get('MONGO_DB_NAME'),
            "CLIENT": {
                "host": os.environ.get('MONGO_DB_HOST'),
                "port": os.environ.get('MONGO_DB_PORT'),
                "username": os.environ.get('MONGO_DB_USERNAME'),
                "password": os.environ.get('MONGO_DB_PASSWORD'),
            },
            'TEST': {
                'MIRROR': 'default',
            },
        }
    }

ALLOWED_HOSTS = []
