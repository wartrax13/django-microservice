from django.urls import include, path

from .views import index, RandomPizza

urlpatterns = [
    path('<int:pid>', index, name='pizza'),
    path('random', RandomPizza.as_view(), name='random')
]
