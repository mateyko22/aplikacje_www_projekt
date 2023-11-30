from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(models.Model):
    first_name = models.CharField(
        'First name',
        max_length=255,
    )
    last_name = models.CharField(
        'Last name',
        max_length=255,
    )
    birth_date = models.DateField(
        'Birth date',
    )
    death_date = models.DateField(
        'Death date',
        null=True,
        blank=True,
    )
    biography = models.TextField(
        'Biography',
    )

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Book(models.Model):
    title = models.CharField(
        'Title',
        max_length=255,
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name='Author',
    )
    genre = models.CharField(
        'Genre',
        max_length=100,
        null=True,
        blank=True,
    )
    pub_date = models.DateField(
        'Publication date',
    )
    isbn = models.CharField(
        'ISBN Number',
        max_length=13,
        unique=True,
    )
    availability = models.BooleanField(
        'Availability',
        default=True,
    )

    class Meta:
        ordering = ['author', 'title']

    def __str__(self):
        return f'{self.title}'


class CustomUser(AbstractUser):
    class WhoIsChoices(models.TextChoices):
        """CustomUser role choices."""

        LIBRARIAN = 'Librarian'
        READER = 'Reader'

    who_is = models.CharField(
        choices=WhoIsChoices.choices,
        default=WhoIsChoices.READER,
        verbose_name='Role',
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Loan(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name='Book',
    )
    reader = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Reader',
    )
    borrow_date = models.DateField(
        'Borrow date',
        auto_now_add=True
    )
    return_date = models.DateField(
        'Return date',
        null=True,
        blank=True
    )
    returned = models.BooleanField(
        'Is returned',
        default=False,
    )

    class Meta:
        ordering = ['book', 'borrow_date']

    def __str__(self):
        return f'{self.book} - {self.reader}'


class BookReview(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name='Book',
    )
    reader = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Reader',
    )
    rating = models.IntegerField(
        'Rating',
        choices=zip(range(1, 10), range(1, 10)),
    )
    comment = models.TextField(
        'Comment',
    )
    date_added = models.DateTimeField(
        'Date added',
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.book} - {self.reader} - {self.rating}'
