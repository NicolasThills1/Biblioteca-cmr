import os
from pathlib import Path
import dj_database_url

# Configurações de caminho
BASE_DIR = Path(__file__).resolve().parent.parent

# Segurança (substituir no Render)
SECRET_KEY = os.environ.get('SECRET_KEY', '836ee7dfb40d20796a62d9bd22a88f25')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Hosts permitidos
ALLOWED_HOSTS = ['*']

# Aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'biblioteca',
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuração de banco de dados
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('postgresql://postgres:bCznXRuIFtDpkEgiqkQePPOLCOxwhleA@postgres.railway.internal:5432/railway'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Modelo de usuário customizado
AUTH_USER_MODEL = 'biblioteca.Usuario'

# CORS (substituir com seu domínio do Neocities)
CORS_ALLOWED_ORIGINS = [
    "https://bibliotecacmr.neocities.org/",
]

# Configurações de internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Recife'
USE_I18N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# URL principal
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'