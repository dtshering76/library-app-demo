from django.contrib import admin
from .models import Book,BookInstance,Language,Genre,Author
# Register your models here.

admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Author)
