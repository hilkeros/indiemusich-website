from django import forms

from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["name", "website", "mastodon", "bluesky", "instagram"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "w-full p-2 my-4 border rounded-md"}
            ),
            "website": forms.URLInput(attrs={"class": "w-full p-2 border rounded-md"}),
            "mastodon": forms.TextInput(
                attrs={"class": "w-full p-2 my-4 border rounded-md"}
            ),
            "bluesky": forms.TextInput(attrs={"class": "w-full p-2 border rounded-md"}),
            "instagram": forms.TextInput(
                attrs={"class": "w-full p-2 my-4 border rounded-md"}
            ),
        }
        help_texts = {
            "name": "Your artist or organisation name",
            "website": "Your website URL (optional)",
            "mastodon": "Your Mastodon handle (optional), e.g. mastodon.social/@username",
            "bluesky": "Your Bluesky handle (optional), e.g. @username.bsky.social",
            "instagram": "Your Instagram handle (optional), e.g. @username",
        }
