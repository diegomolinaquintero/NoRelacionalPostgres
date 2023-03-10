from django.urls import path, include
from rest_framework.routers import DefaultRouter
from test1 import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'test1', views.UserViewSet,basename="usaerjsonb")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]