from django.urls import path
# from . import views
from .views import ExampleCreateView

urlpatterns =[
    # path('hello/', views.say_hallo()),
    path('api/', ExampleCreateView.as_view(), name='example-create'),
]