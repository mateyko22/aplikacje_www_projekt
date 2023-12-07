from django.contrib import admin

from .models import Author
from .models import Book
from .models import BookReview
from .models import CustomUser
from .models import Loan


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'who_is']
    list_filter = ('who_is', 'last_name')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'biography', 'birth_date']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'pub_date', 'availability', 'isbn']
    list_filter = ('author', 'availability')
    actions = ['set_as_available']

    @admin.action(description='Set as available')
    def set_as_available(self, request, queryset):
        queryset.update(availability=True)


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['book', 'reader', 'borrow_date', 'return_date', 'returned']
    list_filter = ('book', 'returned')


@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'reader', 'rating', 'comment', 'date_added']
    list_filter = ('book', 'reader', 'rating')
