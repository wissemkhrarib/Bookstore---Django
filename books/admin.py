from django.contrib import admin
from .models import Book, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'serie_number', 'author')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'email')


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)


