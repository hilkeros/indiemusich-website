from django.db import models
from django.utils.text import slugify


class Member(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=80, unique=True, blank=True)
    website = models.URLField(blank=True, null=True)
    mastodon = models.CharField(max_length=50, blank=True, null=True)
    bluesky = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        counter = 1

        while Member.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug}-{counter}"
            counter += 1

        return unique_slug

    def clean_social_handle(self, handle):
        """Remove @ from the beginning of a social media handle if present."""
        if handle and handle.startswith("@"):
            return handle[1:]
        return handle

    def bluesky_url(self):
        return f"https://bsky.app/profile/{self.clean_social_handle(self.bluesky)}"

    def mastodon_url(self):
        return f"https://{(self.mastodon)}"

    def instagram_url(self):
        return f"https://www.instagram.com/{self.clean_social_handle(self.instagram)}"
