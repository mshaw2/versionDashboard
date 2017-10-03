from django.conf.urls import url
from versionDashboard import views

urlpatterns = [
    url(r'^$', views.index,name="index"),
]