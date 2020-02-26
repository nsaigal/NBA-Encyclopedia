from rest_framework import routers
from django.conf.urls import url
from django.urls import path
from players.api import PlayerViewSet
from .views import PlayerView

# router = routers.DefaultRouter()
# router.register('api/players', PlayerViewSet, 'players')

#urlpatterns = router.urls

urlpatterns = [
    path('', PlayerView.as_view()),
]
