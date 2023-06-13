from django.contrib import admin
from .models import Post
from .models import Author
from .models import Book

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author'
    )
    fields = (
        'content',
        'author'
    )
    class Meta:
        model = Post

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'exists',
    )
    class Meta: 
        model = Book

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Book,BookAdmin)


# Register your models here.
