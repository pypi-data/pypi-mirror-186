from django.urls import path
from .views import AlastriaAuthView
from django.conf import settings
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

router.register(r"alastria-auth", AlastriaAuthView, "Alastria Auth")

urlpatterns = router.urls
