from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/",views.about,name="about"),
    path("contact/", views.contact, name="contact"),
    path("portfolio/",views.portfolio,name="portfolio"),
    path("update/",views.update,name="update"),
    path("service/",views.service,name="service")
]