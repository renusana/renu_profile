from django.shortcuts import render
from django.contrib import messages
from .models import *
from django.core.mail import send_mail
from django.conf import settings


def home(request):

    profile = Profile.objects.first()

    skills = Skill.objects.all()

    services = Service.objects.all()

    projects = Project.objects.all()[:6]

    testimonials = Testimonial.objects.all()

    context = {
        "profile": profile,
        "skills": skills,
        "services": services,
        "projects": projects,
        "testimonials": testimonials,
    }

    return render(request, "portfolio/home.html", context)


def about(request):

    about = About.objects.first()

    context = {"about": about}

    return render(request, "portfolio/about.html", context)


def skills(request):

    technical_skills = Skill.objects.filter(category="Technical")

    professional_skills = Skill.objects.filter(category="Professional")
    technologies = Technology.objects.all()

    context = {
        "technical_skills": technical_skills,
        "professional_skills": professional_skills,
        "technologies": technologies,
    }

    return render(request, "portfolio/skills.html", context)


def services(request):

    services = Service.objects.all()

    context = {"services": services}

    return render(request, "portfolio/services.html", context)


def projects(request):

    projects = Project.objects.all()

    context = {"projects": projects}

    return render(request, "portfolio/projects.html", context)


def resume(request):

    profile = Profile.objects.first()

    about = About.objects.first()

    educations = Education.objects.all()

    skills = Skill.objects.filter(category="Technical")

    projects = Project.objects.all()[:4]
    certificates = Certificate.objects.all().order_by("-issue_date")

    context = {
        "profile": profile,
        "about": about,
        "educations": educations,
        "skills": skills,
        "projects": projects,
        "certificates": certificates,
    }

    return render(request, "portfolio/resume.html", context)


def contact(request):
    profile = Profile.objects.first()

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save into database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        # Email to the user
        send_mail(
            subject="Thank You for Contacting Me",
            message=f"""
Hi {name},

Thank you for contacting me.

I have received your message.

Subject:
{subject}

Your Message:
{message}

I'll get back to you as soon as possible.

Regards,
{profile.name}
            """,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        messages.success(request, "Message sent successfully 🎉")

    context = {"profile": profile}

    return render(request, "portfolio/contact.html", context)
