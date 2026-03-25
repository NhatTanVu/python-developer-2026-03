from django.contrib import admin  # noqa: F401

# Register your models here.
from .models import Author, Post

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("full_name", "created_at", "modified_at")
    search_fields = ("full_name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_at")
    search_fields = ("title", "body", "author__full_name")
    list_filter = ("published_at",)