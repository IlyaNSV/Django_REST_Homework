from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DefaultUserCustomModelViewSet

router = DefaultRouter()
router.register('', DefaultUserCustomModelViewSet)
app_name = 'userapp'
urlpatterns = [
    path('', include(router.urls)),
]
