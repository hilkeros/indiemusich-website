# blog/models.py

from django.contrib.auth.models import (
    User,  # Import User model for linking posts to authors
)
from django.db import models


class Post(models.Model):
    """
    Represents a single blog post.
    """

    title = models.CharField(
        max_length=200, unique=True, help_text="The title of the blog post."
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text="A unique slug for the URL (e.g., 'my-awesome-post').",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # If a user is deleted, their posts are also deleted
        related_name="blog_posts",  # Allows accessing posts from a User object (e.g., user.blog_posts.all())
        help_text="The author of this blog post.",
    )
    # The TextField will store the content. For basic formatting (bold, italics, links),
    # you have options: raw HTML, Markdown, or a rich text editor.
    content = models.TextField(
        help_text="The main content of the blog post. Can contain HTML or Markdown."
    )
    created_on = models.DateTimeField(
        auto_now_add=True, help_text="The date and time the post was created."
    )
    updated_on = models.DateTimeField(
        auto_now=True, help_text="The date and time the post was last updated."
    )

    # Status to differentiate between draft and published posts
    STATUS_CHOICES = ((0, "Draft"), (1, "Publish"), (2, "Spotlight"))
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=0,
        help_text="The publication status of the post (Draft or Publish).",
    )

    class Meta:
        """
        Meta options for the Post model.
        """

        ordering = ["-created_on"]  # Default ordering: most recent posts first
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        """
        String representation of the Post object, used in the Django Admin.
        """
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", args=[self.slug])
