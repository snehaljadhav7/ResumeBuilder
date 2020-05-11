from django.urls import path
#from .views import HomePageView
from django.urls import reverse
from django.urls import path
from .views.views import HomePageView
from .views.list import ListPageView
from .views import views
from django.views.generic import RedirectView
urlpatterns  =[
    path('', HomePageView.as_view(), name='home'),
    path('list/', ListPageView.as_view(), name='list'),
    path('pdf/<resume_id>/', ListPageView.pdf, name='pdf'),
    ]
