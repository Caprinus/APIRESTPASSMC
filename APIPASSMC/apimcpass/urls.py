from django.urls import path
from .views import SeguridadView

urlpatterns=[
    path('seguridad/', SeguridadView.as_view(), name='seguridad_list'),
    path('seguridad/<str:email>', SeguridadView.as_view(), name='seguridad_access'),

]