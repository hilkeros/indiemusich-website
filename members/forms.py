from django import forms
from django.utils.safestring import mark_safe

from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["name", "website", "mastodon", "bluesky", "instagram"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "w-full p-2 my-4 border rounded-md"}
            ),
            "website": forms.URLInput(
                attrs={"class": "w-full p-2 my-4 border rounded-md"}
            ),
            "mastodon": forms.TextInput(
                attrs={"class": "w-full p-2 my-4 border rounded-md"}
            ),
            "bluesky": forms.TextInput(
                attrs={"class": "w-full p-2 my-4 border rounded-md"}
            ),
            "instagram": forms.TextInput(
                attrs={"class": "w-full p-2 my-4 border rounded-md"}
            ),
        }
        help_texts = {
            "name": mark_safe(
                '<span class="text-sm text-gray-500 pb-4 block">Your artist or organisation name</span>'
            ),
            "website": mark_safe(
                '<span class="text-sm text-gray-500 pb-4 block">Your website URL starting with https (optional)</span>'
            ),
            "mastodon": mark_safe(
                '<span class="text-sm text-gray-500 pb-4 block">Your Mastodon handle (optional), e.g. mastodon.social/@username</span>'
            ),
            "bluesky": mark_safe(
                '<span class="text-sm text-gray-500 pb-4 block">Your Bluesky handle (optional), e.g. @username.bsky.social</span>'
            ),
            "instagram": mark_safe(
                '<span class="text-sm text-gray-500 pb-4 block">Your Instagram handle (optional), e.g. @username</span>'
            ),
        }
