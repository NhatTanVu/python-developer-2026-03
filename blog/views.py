from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    posts = (
        Post.objects
        .select_related("author")
        .filter(
            published_at__isnull=False,
        )
        .order_by("-published_at"))
    return render(
        request, 
        "blog/index.html",
        {
            "posts": posts
        })


def welcome(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/welcome.html")

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )