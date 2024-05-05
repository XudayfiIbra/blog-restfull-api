from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'blogs', views.Blog, 'blog')

urlpatterns = [
   path('api/', include(router.urls))
]

