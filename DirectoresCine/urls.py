from django.urls import path
from . import views
#from .views import index


#from django.conf.urls import url
#from . import views


urlpatterns = [
    path('DirectoresCine/',views.index, name = 'index'),
    path('Director/',views.Director),
    path('Película/',views.Película),

]