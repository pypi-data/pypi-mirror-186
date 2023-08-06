**Alastria ID authentication**

- Descripción: Librería para poder autenticarse con alastria ID
- URL: [https://pypi.org/project/alastria-auth/](https://pypi.org/project/alastria-auth/)
- Requisitos: Django
- Instalar: alastria-auth==0.0.9
- Cómo usar:

Añadir en settings.py:

```python
INSTALLED_APPS = [
....
"alastria_auth.apps.AlastriaAuthConfig"
]
# ALASTRIA AUTH VARS
BACKEND_DOMAIN = os.environ.get("BACKEND_DOMAIN", "http://localhost:8000")
NETWORK_SERVICE_HOST = os.environ.get("NETWORK_SERVICE_HOST", "http://host.docker.internal:8001")
ISSUER_PRIVATE_KEY = os.environ.get("ISSUER_PRIVATE_KEY", "")
ISSUER_PUBLIC_KEY = os.environ.get(
    "ISSUER_PUBLIC_KEY",
    "",
)
ISSUER_ADDRESS = os.environ.get("ISSUER_ADDRESS", "")
ALASTRIA_T_NETWORK_ID = os.environ.get("ALASTRIA_T_NETWORK_ID", "redT")
ALASTRIA_AUTH_SECRET = os.environ.get("ALASTRIA_AUTH_SECRET", "")
ALASTRIA_SERVICE_HOST = os.environ.get("ALASTRIA_SERVICE_HOST", "http://host.docker.internal:5000")
#####################
```

Añadir en [url.py](http://url.py) las urls:

```python
from alastria_auth.views import AlastriaAuthView

....
urlpatterns = [
	path("alastria/", include("alastria_auth.urls")),
....
]
```
