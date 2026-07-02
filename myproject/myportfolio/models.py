from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)

    profile_image = models.ImageField(upload_to="profile/")

    short_bio = models.TextField()

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    location = models.CharField(max_length=100)

    github = models.URLField(blank=True)

    linkedin = models.URLField(blank=True)

    resume = models.FileField(upload_to="resume/")

    def __str__(self):
        return self.name


class Skill(models.Model):

    CATEGORY_CHOICES = (
        ("Technical", "Technical"),
        ("Professional", "Professional"),
    )

    skill_name = models.CharField(max_length=100)

    description = models.CharField(max_length=150, blank=True)

    skill_image = models.ImageField(upload_to="skills/", blank=True, null=True)

    percentage = models.IntegerField()

    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="Technical"
    )

    def __str__(self):
        return self.skill_name


class Project(models.Model):
    title = models.CharField(max_length=150)

    image = models.ImageField(upload_to="projects/")

    description = models.TextField()

    technology = models.CharField(max_length=200)

    github_link = models.URLField()

    live_link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)

    company = models.CharField(max_length=100)

    review = models.TextField()

    def __str__(self):
        return self.client_name


class About(models.Model):

    title = models.CharField(max_length=200)

    profile_image = models.ImageField(upload_to="about/")

    description = models.TextField()

    age = models.PositiveIntegerField()

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    location = models.CharField(max_length=100)

    experience = models.CharField(max_length=50)

    projects_completed = models.PositiveIntegerField()

    happy_clients = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Technology(models.Model):

    name = models.CharField(max_length=100)

    icon = models.ImageField(upload_to="technologies/")

    def __str__(self):
        return self.name


class Service(models.Model):

    title = models.CharField(max_length=100)

    icon = models.CharField(max_length=50, blank=True, null=True)

    short_description = models.CharField(max_length=200, blank=True, null=True)

    description = models.TextField()

    def __str__(self):
        return self.title


class Education(models.Model):

    degree = models.CharField(max_length=200)

    institution = models.CharField(max_length=200)

    year = models.CharField(max_length=50)

    percentage = models.CharField(max_length=50)

    def __str__(self):
        return self.degree


class ContactMessage(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Certificate(models.Model):

    title = models.CharField(max_length=200)

    organization = models.CharField(max_length=200)

    certificate_file = models.FileField(upload_to="certificates/")

    issue_date = models.DateField()

    def __str__(self):
        return self.title
