from django.urls import path
from django.conf.urls import include,url
from rest_framework import routers
from .import views

router= routers.DefaultRouter()
router.register(r'carreras',views.CarreraViewSet)
router.register(r'paralelos',views.ParaleloViewSet)
router.register(r'estudiantes',views.EstudianteViewSet)

urlpatterns = [
    path('',views.index,name='index'),
    url(r'^',include(router.urls)),
    url(r'^api-auth',include('rest_framework.urls', namespace='rest_framework'))
]