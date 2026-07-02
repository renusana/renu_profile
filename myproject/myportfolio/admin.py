from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "designation", "email"]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = ("skill_name", "percentage", "category")

    list_filter = ("category",)

    search_fields = ("skill_name",)


admin.site.register(Technology)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = ("title",)

    search_fields = ("title",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "technology"]
    search_fields = (
        "title",
        "technology",
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["client_name", "company"]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    list_display = ["title", "email", "phone", "location"]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):

    list_display = (
        "degree",
        "institution",
        "year",
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = ("name", "email", "subject", "created_at")

    readonly_fields = ("created_at",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "organization",
        "issue_date",
    )

    search_fields = (
        "title",
        "organization",
    )

    list_filter = (
        "organization",
        "issue_date",
    )

    ordering = ("-issue_date",)
