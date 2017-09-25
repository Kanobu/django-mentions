SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "mentions",
    "tests"
]
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}
ROOT_URLCONF = 'mentions.urls'