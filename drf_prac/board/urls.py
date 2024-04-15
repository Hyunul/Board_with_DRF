from django.urls import path, include
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

board_router = DefaultRouter()
board_router.register('', PostViewSet)

urlpatterns =[
    path('', include(board_router.urls)),
]