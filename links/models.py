# links/models.py

from django.db import models

LINK_CATEGORIES = {
    "ATProto": 0,
    "Fediverse": 1,
    "Open Web": 2,
}


class Link(models.Model):
    """
    Represents an external or internal link with associated text and an optional description.
    """

    url = models.URLField(
        max_length=500,  # URLs can be quite long
        unique=True,  # Ensure each URL is unique in your list
        help_text="The actual URL to which the link points (e.g., https://www.example.com).",
    )
    link_text = models.CharField(
        max_length=255,
        help_text="The text that will be displayed for the link (e.g., 'Visit Example Website').",
    )
    description = models.TextField(
        blank=True,  # Make this field optional
        null=True,  # Allow NULL in the database for optional fields
        help_text="An optional, brief description of what the link is about.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="The date and time when this link was added."
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="The date and time when this link was last updated."
    )
    category = models.IntegerField(
        choices=[(v, k) for k, v in LINK_CATEGORIES.items()],
        default=LINK_CATEGORIES["ATProto"],
        help_text="The category of the link (e.g., ATProto, Fediverse, Open Web).",
    )

    class Meta:
        """
        Meta options for the Link model.
        """

        ordering = ["link_text"]  # Order links alphabetically by their display text
        verbose_name = "Link"
        verbose_name_plural = "Links"

    def __str__(self):
        """
        String representation of the Link object, used in the Django Admin.
        """
        return self.link_text
