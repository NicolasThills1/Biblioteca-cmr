import dj_database_url
INSTALLED_APPS = [
    'biblioteca',
]


DATABASES = {
    'default': dj_database_url.config(default=os.getenv('postgresql://postgres:bCznXRuIFtDpkEgiqkQePPOLCOxwhleA@postgres.railway.internal:5432/railway'))
}

CORS_ALLOWED_ORIGINS = [
    "https://bibliotecacmr.neocities.org/",
]