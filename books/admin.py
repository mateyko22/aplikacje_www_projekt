from django.contrib import admin

from .models import CustomUser
from .models import Book, Magazine, Department, Movie
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'who_is', 'department']
    list_filter = ('who_is', 'department',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'pub_date', 'department']