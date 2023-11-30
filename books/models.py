from django.db import models
from django.contrib.auth.models import AbstractUser


class Department(models.Model):
    class DepartmentChoices(models.TextChoices):
        FANTASY = 'Fantasy'
        SCIFY = 'Sci-fy'
        HISTORY = 'History'
        ADVENTURE = 'Adventure'
        CHILDREN = 'Children'
        SCIENCE = 'Science'
        OTHER = 'Other'

    name = models.CharField(
        'Name',
        max_length=20,
        choices=DepartmentChoices.choices,
    )
    is_active = models.BooleanField(
        'Is Active',
        default=True,
    )


class Book(models.Model):
    name = models.CharField(
        'Name',
        max_length=255,
    )
    author = models.CharField(
        'Author',
        max_length=100,
    )
    pub_date = models.DateField(
        'Publication date',
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        verbose_name='Department',
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['author']


class Magazine(models.Model):
    name = models.CharField(
        'Name',
        max_length=255,
    )
    author = models.CharField(
        'Author',
        max_length=100,
    )
    pub_date = models.DateField(
        'Publication date',
    )
    edition = models.CharField(
        'Edition',
        max_length=50,
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        verbose_name='Department',
        blank=True,
        null=True,
    )


class Movie(models.Model):
    class MovieMediaTypes(models.TextChoices):
        DVD = 'DVD'
        ONLINE = 'online'

    name = models.CharField(
        'Name',
        max_length=255,
    )
    director = models.CharField(
        'Author',
        max_length=100,
    )
    pub_date = models.DateField(
        'Publication date',
    )
    media_type = models.CharField(
        'Type',
        max_length=25,
        choices=MovieMediaTypes.choices,
    )


class CustomUser(AbstractUser):
    class WhoIsChoices(models.TextChoices):
        """CustomUser role choices."""

        LIBRARIAN = 'Librarian'
        CUSTOMER = 'Customer'

    who_is = models.CharField(
        choices=WhoIsChoices.choices,
        default=WhoIsChoices.CUSTOMER,
        verbose_name='Role',
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        verbose_name='Department',
        blank=True,
        null=True,
    )
