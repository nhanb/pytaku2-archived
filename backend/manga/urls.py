from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^search/', views.ListSearchResults.as_view()),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
