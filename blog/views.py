import markdown
from django.shortcuts import get_object_or_404, render

from .models import STATUS_CODES, Post


def post_detail(request, slug):
    post = get_object_or_404(
        Post, slug=slug, status__in=[STATUS_CODES["Publish"], STATUS_CODES["Listed"]]
    )
    post.formatted_content = markdown.markdown(post.content)  # Convert here
    return render(request, "post_detail.html", {"post": post})


def post_list(request):
    posts = Post.objects.filter(status=STATUS_CODES["Listed"]).order_by("-created_on")
    for post in posts:
        post.preview = get_preview(post.content)  # Convert here
    return render(request, "post_list.html", {"posts": posts})


def spotlight_post(request):
    post = (
        Post.objects.filter(status=STATUS_CODES["Spotlight"])
        .order_by("-created_on")
        .first()
    )
    post.formatted_content = markdown.markdown(post.content)
    return render(request, "about.html", {"post": post})


def get_preview(content, word_limit=50):
    words = content.split()
    preview_text = " ".join(words[:word_limit])
    return markdown.markdown(preview_text)
