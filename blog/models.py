import uuid
from django.db import models  # noqa: F401

# Create your models here.
class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    published_at = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="posts"
    )