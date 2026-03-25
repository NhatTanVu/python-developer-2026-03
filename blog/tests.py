
from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from blog.models import Author, Post  # noqa: F401

# Create your tests here.


class WelcomeViewTests(TestCase):
    def test_default_page(self):
        # Act
        response = self.client.get("/")
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/welcome.html")


class IndexViewTests(TestCase):
    def setUp(self):
        # Arrange
        Post.objects.all().delete()  # Delete all 10 seeded posts
        self.author = Author.objects.create(
            full_name="Test Author",
            created_at=timezone.now(),
            modified_at=timezone.now()
        )

    def test_index_returns_200_and_uses_template(self):
        # Act
        response = self.client.get("/posts/")
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/index.html")

    def test_index_shows_only_published_posts(self):
        # Arrange
        published_post = Post.objects.create(
            title="Published",
            body="Body",
            author=self.author,
            created_at=timezone.now(),
            modified_at=timezone.now(),
            published_at=timezone.now(),
        )
        not_published_post = Post.objects.create(
            title="Draft",
            body="Body",
            author=self.author,
            created_at=timezone.now(),
            modified_at=timezone.now(),
            published_at=None,
        )
        # Act
        response = self.client.get("/posts/")
        posts = list(response.context["posts"])
        # Assert
        self.assertIn(published_post, posts)
        self.assertEqual(len(posts), 1)

    def test_index_orders_posts_by_published_date_desc(self):
        # Arrange
        older = Post.objects.create(
            title="Older",
            body="Body",
            author=self.author,
            created_at=timezone.now(),
            modified_at=timezone.now(),
            published_at=timezone.now() - timedelta(days=1),
        )
        newer = Post.objects.create(
            title="Newer",
            body="Body",
            author=self.author,
            created_at=timezone.now(),
            modified_at=timezone.now(),
            published_at=timezone.now(),
        )
        # Act
        response = self.client.get("/posts/")
        posts = list(response.context["posts"])
        # Assert
        self.assertEqual(posts, [newer, older])


class PostDetailViewTests(TestCase):
    def setUp(self):
        # Arrange
        self.author = Author.objects.create(
            full_name="Test Author",
            created_at=timezone.now(),
            modified_at=timezone.now()
        )
        self.post = Post.objects.create(
            title="Markdown Post",
            body="# Hello\n\nThis is **bold**.",
            author=self.author,
            created_at=timezone.now(),
            modified_at=timezone.now(),
            published_at=timezone.now(),
        )

    def test_index_returns_200_and_uses_template(self):
        # Act
        response = self.client.get(reverse("post_detail", args=[self.post.id]))
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_detail.html")

    def test_post_detail_returns_404_for_missing_post(self):
        import uuid
        response = self.client.get(reverse("post_detail", args=[uuid.uuid4()]))
        self.assertEqual(response.status_code, 404)

    def test_post_detail_renders_markdown_to_html(self):
        response = self.client.get(reverse("post_detail", args=[self.post.id]))

        self.assertContains(response, "<h1>Hello</h1>", html=True)
        self.assertContains(response, "<strong>bold</strong>", html=True)
