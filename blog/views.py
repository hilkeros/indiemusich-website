import markdown
from django.shortcuts import get_object_or_404, render

from .models import Post


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    post.formatted_content = markdown.markdown(post.content)  # Convert here
    return render(request, "post_detail.html", {"post": post})


def spotlight_post(request):
    post = Post.objects.filter(status=2).order_by("-created_on").first()
    post.formatted_content = markdown.markdown(post.content)
    return render(request, "about.html", {"post": post})
