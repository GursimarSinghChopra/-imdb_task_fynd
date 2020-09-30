from django.contrib import admin
from django.urls import path
from rest_framework import routers
from imdb_app import views

router = routers.SimpleRouter()
router.register(r'admin/movies', views.MovieViewSet)
router.register(r'admin/genres', views.GenreViewSet)
router.register(r'movies', views.MovieReadOnly)
router.register(r'genres', views.GenreReadOnly)




urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
