from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatSessionViewSet, signup, login_view, logout_view, check_auth, hello_world

router = DefaultRouter()
router.register(r'sessions', ChatSessionViewSet, basename='chat-session')

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('check-auth/', check_auth, name='check-auth'),
    path('hello/', hello_world, name='hello'),
]