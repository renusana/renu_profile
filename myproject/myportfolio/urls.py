from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("skills/", views.skills, name="skills"),
    path("services/", views.services, name="services"),
    path("projects/", views.projects, name="projects"),
    path("resume/", views.resume, name="resume"),
    path("contact/", views.contact, name="contact"),
]
